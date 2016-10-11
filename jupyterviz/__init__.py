from IPython.display import IFrame
import pkg_resources, os
import json
import yaml

resource_package = __name__

def viz(d,width=600,height=500,conf=None):
    dest="temp_plot.html"
    viz=d['type']
    data=d["data"]
    resource_path = os.path.join('Itemplates', viz+".html")
    template = pkg_resources.resource_string(resource_package, resource_path)
    template=template.replace("{data}",json.dumps(data))
    template=template.replace("{width}",str(width))
    template=template.replace("{height}",str(height))
    if conf:
        for key in conf.keys():
            template=template.replace("{"+key+"}",json.dumps(conf[key]))

    with open("tmp/tmpbox.htm","w") as output:
        output.write(template)
    return IFrame("tmp/tmpbox.htm",width+50,height+50)

def help():
    resource_path = os.path.join('help', "help.yaml")
    template = pkg_resources.resource_string(resource_package, resource_path)
    return viz({"type":"json","data":yaml.load(template)})
