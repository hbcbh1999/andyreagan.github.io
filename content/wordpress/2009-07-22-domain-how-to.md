Title: Domain How-To
Date: 2009-07-22 17:50
Author: andyreagan
Category: General updates
Slug: domain-how-to

### This will be my all-in-one how-to get your own domain name, and set it up with a webpage and email.

So I never really got time to finish this to the degree that I would
like...so maybe I will someday (July 30).

All of this imformation is available elsewhere...where I once upon a
time read it, but I hope this puts it all in one place. Looking back at
where I got all of this information...pretty much all of it is
on [aboutdebian.com](http://aboutdebian.com/), just ignore the linux
parts...although it gets pretty in-depth.

What you'll need need:  
1. \$10, which works out to 2.73 cents per day....worth it!!  
2. Brain  
3. Free Space (most ISP's and colleges give you about 30MB of space)  
4. Content (a blog...resume...something worthy of sharing)  
5. Time (a few hours...not a whole lot of time, really)

You may want to have:  
1. More time, to do fun stuff with your site  
2. [Twitter](http://twitter.com/), because it's super easy to include
on your page  
3. [Dreamweaver](http://www.adobe.com/products/dreamweaver/) (a program
from Adobe to create the web pages) or other web-page generating
software (MS Frontpage...). Notepad works though.  
4. [Audi R8](http://www.audiusa.com/us/brand/en/models/r8.html)  
5. Advanced knowledge of the [IP
Protocol](http://en.wikipedia.org/wiki/Internet_Protocol)

First, some basics of the internet. I'll keep it really really simple.

We'll use the example of andyreagan.com. The journey begins when you
open your web browser (Internet Explorer, Mozilla Firefox, Google
Chrome...), and type andyreagan.com in. Maybe this is a bad example, so
we'll pretend that my site is hosted on a dedicated server. Your browser
can't really do anything with that name, so what it does is contacts a
DNS, domain name server, to resolve that hostname to an IP address, with
which your computer can contact the server hosting my site. This is one
of the reasons that internet explorer sucks, bc when you hit "go" it
just says opening page the whole time, it doesn't tell you what's it's
really doing, Firefox and Chrome both give you better information. And
that imformation may be useful in troubleshooting your site, it doesn't
interperet my images correctly, so just don't use IE... Where was I....
Oh so your computer now has the IP address of the site it would like to
contact. It will also need the MAC (a unique physical address) of that
server, so it'll send a request to get that, and the server will reply
with that information. Then, finally, your computer will send a "get"
request to the server of which it knows the IP and MAC address, and that
server will respond with a directory, and your browser will know to open
the file named "index.html". And there you have it. The process is
really the same for email too, but yeah different. It's not really that
important that you understand all of this, either...just know that there
is a DNS server and that it has a purpose of resolving hostnames.

#### Registering Your Domain Name

Using a site like [godaddy.com](http://www.godaddy.com/), the one with
the super bowl ads, or the one which I would
recommend [networksolutions.com](http://www.networksolutions.com/) you
can find an avaible domain name (i.e. yourname.net or yourname.com or
many others) and register that name for around (or less than) \$10. For
convenience, you may want to go two or more years out...

[EasyDNS.com](http://www.easydns.com/) is a much better all-in-one
solution than either of those sites above, but it is also more
expensive. If you would be willing to pony up \$40/year, coming to
almost 11 cents per day, this would be a muuuch better way to go. Still
not the cheapest it could've been done, but DEFINITELY the easiest. The
service that this includes for a cost is custom DNS hosting, which we
could be getting for free, but yeah this would keep everything in one
place...I think I might even make the switch next year when my
registration runs out. I don't know why I really need to...but it would
be nice to have everything in one place. And I was just poking around
their site about their stealth website redirection and it was super
helpful, I think I even learned some stuff. I'm going to link to them
later on that, they explain it so well.

#### Changing your registered nameservers

To give us more flexibility with our Zone File, the file that is stored
on a (well, at minimum 2) DNS servers, we will change our nameservers
over to zoneedit.com's. If you did go with EasyDNS, then you can totally
skip this step, although it's simple.

At zoneedit.com, we will be both be able to use a "cloaked web forward"
to point yourname.com to the free hosting, and to use GMail for Domains
for all email needs.

#### Setting up Email

Look under links at the bottom for GMail for Domains. Open that guy up,
and read it. What you'll need to do is open a Google Apps account. I
don't remember the process exactly, but I do remember that it required
that I verify ownership of the domain...there were three choices, and as
long as it is still one, you're going to want to use a CNAME record to
do it.

Once you have the account at Google, don't worry about getting that
warning about getting it verified right away, we'll take care of that
next. Just keep the CNAME that they wanted you to include. And now dig
around until you find the nameservers that Google needs you to put in
your MX record. Copying and saving both those MX entries and the CNAME
entry into a text document, we're ready to go to the next step.

#### Configuring Zone File

This is going to be by far the most technical part, and is definitely
the part that I think I struggled with the most. It comes down to
understanding what a zone record is (which I may have referred to as a
zone file, same thing) and what is in it. All it does is resolve your
hostname to an IP address, but in our case we're not actually going to
be putting in any IP addresses. The types of records we'll deal with are
A, MX and CNAME. A's are the standard hostname resolution....bad
explanation but they'll deal with andyreagan.com and www.andyreagan.com
and m.andyreagan.com to point the web address to some server. The MX
records are mail exchange records, and we'll point them to Google's mail
servers. The CNAME record is the fanciest of them all (there are others)
and it is simply an alias. By alias I mean that it can make
something.andyreagan.com point to google.com or to
somethingelse.andyreagan.com...it's not actually pointing at a server
but is rather an "alias". So, go ahead and drop in the MX and CNAME
records from the text file from Google. Now, since we won't really be
entering "A" records in a traditional sense, we will set up a webforward
to where our site is hosted. This is pretty slick really. What
zoneedit.com will do is actually point the A record to their own server,
on which is a file that simple contains a frame with no border of the
address to which you are web forwarding. As opposed to redirecting, this
will keep andyreagan.com in the address bar instead of the true location
of the
files, [filebox.vt.edu/users/areagan](http://filebox.vt.edu/users/areagan)
(try it, that'll show the real site in the address bar). For an
additional and perhaps clearer explanation of this service, I'll leave
you to the guys at EasyDNS.com for
their [take](http://easytest.com/%22), on this page they're using what
they call stealth redirection (the same thing as a cloaked webfoward) to
make it appear as though you are looking at easytest.com when in reality
you are still on EasyDNS.

#### Creating the Webpage

This part will be pretty skimpy, since I'm not really an expert and this
is stuff that is really easy to look up/play around with. You can't
screw it up... There are professions that deal with just this part, and
those people are called "web designers". The easiest thing to do if
you're a small business needing a web presence is to hire one of these
groups, and they'll make the page sweet, I mean it's what they do.

If you have Dreamweaver, or are familiar with torrents and can get it,
this will be easy to make a great looking page. It's what the pros use.
Just go to justdreamweaver.com and download a sweet free template,
change the names and content of the pages...and you're set!

If you're working with any other software for creating webpages, I'm no
help, so just have at.

If you're stuck with notepad, don't panic quite yet. HTML is really easy
to write, and with the understanding of tables, you can do pretty much
anything. All sites used to be written in straight HTML with extensive
use of tables at some point....I think. Well, to start, you may want to
look at W3 Schools or right click on any webpage and click "view
source". OK, I just found a page on W3 with examples of everything that
you would ever want to
do. [This](http://www.w3schools.com/html/html_examples.asp) should
actually be all you need. Just move down the page one example at a time
and you'll end up with frames, tables, and forms. You may want to skip
ahead and read images really quickly. It's all just learning the syntax
of the tags...

### Links, links, links

[Domaintools.com](http://www.domaintools.com/) - You can do some neat
stuff like traceroute and ping...  
[AndyReagan.com](http://www.andyreagan.com/) - Just a sweet example of
how TO make a site.  
[NetworkSolutions.com](http://www.networksolutions.com/) - A good
registrar...  
[EasyDNS.com](http://www.easydns.com/) - If money is no object, the
perfect registrar+DNS, and it's not that unreasonable  
[JustDreamweaver.com](http://www.justdreamweaver.com/) - Great
templates for dreamweaver, even the free ones are good  
[W3 Schools](http://www.w3schools.com/html/html_examples.asp) -
Examples of everything you would ever want to do in HTML  
[Google Checkout](https://checkout.google.com/seller/integrate.html) -
One way to accept money for donations/services on your site  
[The Internet (Wiki)](http://en.wikipedia.org/wiki/Internet) - Good
background on the internet and how it works...by following the links to
TCP/IP and packet-switching and DNS and stuff there is wealth of
information  
[AboutDebian.com](http://aboutdebian.com/) - Tutorials on how to set up
a server in Linux, and great, detailed information on many of the
technical aspects of everything network-related  
[GMail for
Domains](http://the-gadgeteer.com/2009/01/12/im-floating-in-the-clouds-now-with-gmail-for-domains/)
- An Article on how to set up GMail for Domains, which is how I use my
email and is frickin sweet...I would never want to use anything else  
[Making Website Logo](http://www.chami.com/tips/internet/110599I.html)
- How to make that little logo that shows up for bookmarks and on the
side of the browser bar for your site  
[Building Mobile
Site](http://groups.google.com/group/google-checkout-api-mobile/browse_thread/thread/e3f42b40f19ce167#e59965c2075a1f69)
- If I ever wanted to make m.andyreagan.com for ease of viewing on
blackberry or iPhones, I would start here  
[mail.andyreagan.com](http://mail.andyreagan.com/) - what my login for
GMail for Domains looks like...and the slick link to get there  
[Stealth Redirection Explanation](http://easytest.com/) - This is the
best I could explain it for sure, the tips they gave about overcoming
associated problems were great (I had to figure it out on my own...)  
[Google Apps](http://www.google.com/a/cpanel/domain/new) - THIS IS THE
LINK YOU WANT! for signing up for your domain.
