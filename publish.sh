# push the output folder into the local gh-pages branch
pyenv/bin/ghp-import output -b master
git push origin master

# push local content to the remote
# git push origin gh-pages
