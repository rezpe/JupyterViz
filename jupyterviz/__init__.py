from IPython.display import IFrame
import pkg_resources, os
import json
import yaml

resource_package = __name__

def viz(d,conf=None):
    dest="temp_plot.html"
    viz=d['type']
    data=d["data"]
    width=600
    height=550
    if "width" in d:
        width=d["width"]
    if "height" in d:
        width=d["height"]
    resource_path = os.path.join('templates', viz+".html")
    template = pkg_resources.resource_string(resource_package, resource_path)
    template=template.replace("{data}",json.dumps(data))
    template=template.replace("{width}",str(width))
    template=template.replace("{height}",str(height))
    if conf:
        for key in conf.keys():
            template=template.replace("{"+key+"}",json.dumps(conf[key]))

    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    with open("tmp/plot_viz.html","w") as output:
        output.write(template)
    return IFrame("tmp/plot_viz.html",width+50,height+50)

def help():
    resource_path = os.path.join('help', "help.yaml")
    template = pkg_resources.resource_string(resource_package, resource_path)
    return viz({"type":"json","data":yaml.load(template)})
