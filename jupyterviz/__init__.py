from IPython.display import IFrame, HTML
import pkg_resources, os
import json
import yaml

resource_package = __name__

def viz(**kwargs):
    dest="temp_plot.html"
    viz=kwargs['type']
    if "width" not in kwargs.keys():
        kwargs["width"]=600
    if "height" not in kwargs.keys():
        kwargs["height"]=600
    if "datadf" in kwargs.keys():
        kwargs["data"]=kwargs["datadf"].to_dict(orient="records")
        kwargs.pop("datadf", None)
    resource_path = os.path.join('templates', viz+".html")
    template = pkg_resources.resource_string(resource_package, resource_path)

    for key,value in kwargs.iteritems():
        template=template.replace("{"+key+"}",json.dumps(value))

    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    with open("tmp/plot_viz.html","w") as output:
        output.write(template)

    return IFrame("tmp/plot_viz.html",kwargs["width"]+50,kwargs["height"]+50)

def help():
    resource_path = os.path.join('help', "help.yaml")
    template = pkg_resources.resource_string(resource_package, resource_path)
    return viz(type="json",data=yaml.load(template))

def secretInput(varName):
    resource_path = os.path.join('templates', "secret.html")
    template = pkg_resources.resource_string(resource_package, resource_path)
    template=template.replace("{varName}",varName)
    return HTML(template)

##Once executed, the data will be available on http://localhost:8090/api/db
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
import pandas as pd

def serve(df):
    if len(df)>100000:
        raise ValueError("Data Frame should be smaller")

    df=pd.DataFrame(df)
    
    app = Flask(__name__)
    api = Api(app)
    CORS(app)

    class pandarequest(Resource):
        def get(self):
            return df.reset_index().to_dict(orient="records")

    api.add_resource(pandarequest, '/api/db')
    print "URL: https://localhost:8090/api/db"
    app.run(host="0.0.0.0",port=8090,ssl_context='adhoc',threaded=True,)
