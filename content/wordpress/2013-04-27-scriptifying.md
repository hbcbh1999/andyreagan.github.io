Title: Scriptifying
Date: 2013-04-27 07:33
Author: andyreagan
Category: code
Tags: alias, aliasing, bash, bash alias, command-m, dos2unix, grad school, mac, osx, perl, scriptifying, scripting
Slug: scriptifying

I bet you've been wondering where grad students spend their time. You
would think they're in their offices in the basement, the library, or
the coffee shop. But you'd be wrong, grad students spend their time at
the command line.

If you don't know where that is, you can imagine Mouse hacking the
matrix, and probably stop reading.

Given that we spend so much time there, here a few scripts that can make
your life better. Perl comes with MAC OSX, so these guys should run
right away on OSX, or any unix machine.

### Making aliases

If you type something a lot (or just more than once), it can help to
make a shortcut (alias) for that.  This perl scripts makes them for you:

[code language="perl"]  
\#!/usr/bin/perl

if (\$\#ARGV != 1){  
print "bad arguments, need at least 2\\n";  
exit;  
}

\`echo \\"alias \$ARGV[0]=\\\\\\"\$ARGV[1]\\\\\\"\\" \>\>
\~/.bash\_profile\`;

print "made alias for \$ARGV[0]\\n";  
[/code]

To get this to work, we're going to use it to make it's own alias!!
Download it and put in it /Users/yourusername/bin, make it executable
with

[code language="bash"]  
chmod +x \~/bin/makealias  
[/code]

Now run it, to make itself an alias. First, this will look like

[code language="bash"]  
\~/bin/makealias makealias \~/bin/makealias  
[/code]

which is a little bit weird. Now make any alias you want (in a new
shell) with

[code language="bash"]  
makealias foo bar  
[/code]

or more usefully

[code language="bash"]  
makealias mroe more  
[/code]

which will execute more whenever you type mroe!

### Cleaning up files

Sometimes when you download files, or \*shudder\* edited them on a
windows computer, there are Command-M characters at the end of each
line. Put this little guy (thanks to [Davy
Schmeits](http://schmeits.wordpress.com/ "Davy Schmeits")) in your bin
directory and make it an alias

[code language="perl"]  
\#!/usr/bin/perl

if (\$\#ARGV != 1){  
print "bad arguments, need at least 2\\n";  
exit;  
}

\`cat \$ARGV[0] | col -b \$ARGV[1]\`;

print "thank me later\\n"  
[/code]

Remove the last line if you're so inclined. To make this run, all we
need to do now is use makealias:

[code language="bash"]  
chmod +x \~/bin/dos2unix; makealias dos2unix \~/bin/dos2unix  
[/code]

### Archiving

This bit of wisdom thanks to [Peter Dodds](http://www.uvm.edu/~pdodds/).
Back up the tex and pdf of your work using this script. The default is
the local directory, and you can pass it any directory to back up.

[code language="perl"]  
\#!/usr/bin/perl

(\$day,\$month,\$year) = (localtime)[3,4,5];  
\$year = \$year + 1900;  
\$month = \$month+1;  
if (\$month \< 10) {  
\$month = "0\$month";  
}  
if (\$day \< 10) {  
\$day = "0\$day";  
}

if (\$\#ARGV == 0){  
\`cd \$ARGV[0]\\; mkdir archive/\$year-\$month-\$day\\; cp -v \*.pdf
\*.tex \*.bib archive/\$year-\$month-\$day/\`;  
}  
else{  
\`mkdir archive/\$year-\$month-\$day\\; cp -v \*.pdf \*.tex \*.bib
archive/\$year-\$month-\$day/\`;  
}  
[/code]
