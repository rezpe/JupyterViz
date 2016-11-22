# After modifying setup.py
#git tag 0.10 -m "Adds a tag so that we can put this on PyPI."
#git push --tags origin master

# Builds
#python setup.py sdist
#python setup.py sdist upload -r pypi

# Automated script

release=$(cat release)
releaseplus=$(python -c "print $release+0.01")
git tag $releaseplus -m "Adds a tag so that we can put this on PyPI."
git push --tags origin master
python setup.py sdist
python setup.py sdist upload -r pypi
echo $releaseplus > release
