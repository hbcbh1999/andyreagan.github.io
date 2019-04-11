Title: Making computers talk (via ssh keys)
Date: 2013-04-22 10:29
Author: andyreagan
Category: code
Tags: keygen, no password, no passwords, password, rsync, ssh, ssh-copy-id, ssh-keygen
Slug: making-computers-talk-via-ssh-keys

So you're tired of typing in passwords every time you ssh to a remote
computer. Or you want scripts that login and do things (or rsync, etc).
There is a better way. Use ssh keys.

On the local machine, do this only once:

[code language="bash"]  
ssh-keygen  
[/code]

And then for each machine you want to ssh into (do this on your local
machine as well):

[code language="bash"]  
cat \~/.ssh/id\_rsa.pub | ssh user@machine "mkdir \~/.ssh; cat \>\>
\~/.ssh/authorized\_keys"  
[/code]

The above may complain that the directory already existed, but it will
work regardless. On some machines there is a built-in "copy-ssh-id" but
I like the above because you can see what it's doing.

That's it, you're done. Things to note: only "ssh-keygen" once on a
machine, and you can run the second command as many times as you like
(to connect your local computer to lots of servers).

Final bit of good-ness: if don't even want to type out "ssh
user@machine" every time, try this on for size (this would make the
command "MACHINE" ssh onto user@machine):

[code language="bash"]  
echo "alias MACHINE=\\"ssh user@machine\\"" \>\> \~/.bash\_profile  
[/code]

Cheers.
