# After modifying setup.py
git tag 0.10 -m "Adds a tag so that we can put this on PyPI."
git push --tags origin master

# Builds
python setup.py sdist
python setup.py sdist upload -r pypi
