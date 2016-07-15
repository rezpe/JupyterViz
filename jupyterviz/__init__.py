from IPython.display import IFrame
import pkg_resources, os
import json

resource_package = __name__  

def viz(dest,viz,data,width,height,conf=None):
    resource_path = os.path.join('Itemplates', viz+".html")
    template = pkg_resources.resource_string(resource_package, resource_path)
    template=template.replace("{data}",json.dumps(data))
    template=template.replace("{width}",str(width))
    template=template.replace("{height}",str(height))
    with open("tmp/tmpbox.htm","w") as output:
        output.write(template)
    return IFrame("tmp/tmpbox.htm",width+50,height+50)