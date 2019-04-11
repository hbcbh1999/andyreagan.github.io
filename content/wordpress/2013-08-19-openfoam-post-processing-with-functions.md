Title: OpenFOAM post-processing with functions
Date: 2013-08-19 21:40
Author: andyreagan
Category: Uncategorized
Slug: openfoam-post-processing-with-functions

I had to really search to find examples of using the built-in utilities
in OpenFOAM to post-process while running a case.

In my case, I want to output the mass flow rate through a
cross-sectional patch in my simulation. Anyway, find all of the examples
with:

*find \$FOAM\_TUTORIALS -name controlDict | xargs grep -A 25 functions*

I recommend you direct this to a file (i.e. end it with
*"\> some-file.txt"*)
