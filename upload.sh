

# Automated script (be careful with the version of release)
# Increase release
release=$(cat release)
releaseplus=$(python -c "print $release+0.01")

#Adds the tag
git tag $releaseplus -m "Adds a tag so that we can put this on PyPI."
git push --tags origin master

#Modifies setup.py
python newsetup.py
python setup.py sdist
python setup.py sdist upload -r pypi

#Saves it to release file
echo $releaseplus > release

#Save in git
git add release
git add setup.py
git commit -m "Added files of release $release"
