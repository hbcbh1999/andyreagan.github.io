Title: The Peter Dodds MATLAB Image Machine
Date: 2013-09-26 13:00
Author: andyreagan
Category: Uncategorized
Slug: the-peter-dodds-matlab-image-machine

The man, the myth, Peter Dodds has shared
with me his MATLAB image making scripts.

The idea is to make beautiful images quickly and reproducibly.

Find all of the scripts, and a README.md for installing those at
github.com/andyreagan/d0dds-image-machine.git

Adding paths to ghostscipt, imagemagick, mactex in MATLAB's startup
script.

http://atchieu.wordpress.com/2012/04/08/adding-system-paths-tousing-external-unix-tools-from-the-matlab-command-line/

These don't work:

http://www.mathworks.com/help/matlab/matlab\_env/startup-options.html\#brlkmbe-1

Don't use this, because the export command needs to go into the MATLAB
script at the beginning, but this is the general idea.

chmod 755 /Applications/MATLAB\_R2013a.app/bin/matlab  
echo "export PATH=\\"\\\$PATH:\\/usr\\/texbin\\"" \>\>
/Applications/MATLAB\_R2013a.app/bin/matlab  
chmod 555 /Applications/MATLAB\_R2013a.app/bin/matlab






