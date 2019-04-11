Title: Installing OpenFOAM 2.0.x on Mac OSX Lion (10.7.5)
Date: 2013-06-20 14:14
Author: andyreagan
Category: Uncategorized
Slug: installing-openfoam-2-0-x-on-mac-osx-lion-10-7-5

I am just finishing an installation of OpenFOAM on Mac OSX and it was no
straighforward task.

First, try to work through this very helpful post:

http://www.optimulation.com/2011/09/01/installing-openfoam-2-0-x-on-mac-os-x-lion/

This all went just fine for me, (remember to update your MacPorts first,
and do an upgrade) until it came time to compile OpenFOAM again. I kept
getting lots of "could not open file globalMeshData.H" stuff, and went
back to see what was wrong.

Turns out that whatever happened, although having GCC 4.5, my machine
still used GCC 4.2 when I type "gcc."

After much headaching, I was able to scrap together a working solution
by using MacPorts' select, and updating my hash. These two pages helped
me with each:

http://stackoverflow.com/questions/837992/update-gcc-on-osx

http://superuser.com/questions/423254/macports-gcc-select-error-trying-to-exec-i686-apple-darwin11-llvm-gcc-4-2/448132\#448132

The crucial commands were

[code language="bash"]  
port select --list gcc  
[/code]  
[code language="bash"]  
port select --set gcc mp-gcc45  
[/code]

then

[code language="bash"]  
hash gcc  
[/code]

Hope that helps!
