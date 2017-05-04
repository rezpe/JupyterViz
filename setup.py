from distutils.core import setup

release = 0.35

setup(
  name = 'jupyterviz',
  packages = ['jupyterviz'], # this must be the same as the name above
  version = str(release),
  description = 'Visualization charts for jupyter',
  author = 'Sebastien Perez',
  author_email = 'sebastien.perezvasseur@gmail.com',
  url = 'https://github.com/rezpe/JupyterViz', # use the URL to the github repo
  download_url = 'https://github.com/rezpe/JupyterViz/tarball/'+str(release), 
  keywords = ['jupyter', 'visualization'], # arbitrary keywords
  package_data={'jupyterviz': ['templates/*.html','help/help.yaml']},
  classifiers = [],
)
