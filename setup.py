from distutils.core import setup

release = "1.0.3"

#http://sherifsoliman.com/2016/09/30/Python-package-with-GitHub-PyPI/
setup(
  name = 'jupyterviz',
  packages = ['jupyterviz'], # this must be the same as the name above
  version = release,
  description = 'Visualization charts for jupyter',
  author = 'Sebastien Perez',
  author_email = 'sebastien.perezvasseur@gmail.com',
  url = 'https://github.com/rezpe/JupyterViz', # use the URL to the github repo
  download_url = 'https://github.com/rezpe/JupyterViz/tarball/'+ release, 
  keywords = ['jupyter', 'visualization'], # arbitrary keywords
  package_data={'jupyterviz': ['templates/*.html','help/help.yaml']},
  classifiers = [],
)
