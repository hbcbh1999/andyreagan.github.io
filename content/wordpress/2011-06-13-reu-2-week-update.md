Title: REU: 2 Week Update
Date: 2011-06-13 20:49
Author: andyreagan
Category: General updates
Slug: reu-2-week-update

Figured I'd take a quick time out to write about how the first two weeks
of research have been going.  As I've mentioned before, I love my group
and it's awesome that a lot of them are into active things and cool
people.  Getting to know them all has been a blast.

For me, the first week and a half was somewhat slow, because I'm working
on the same project that I had been: building a discrete model of iron
metabolism.  This is something that I thought I had finished during the
semester, and was somewhat surprised when I learned that there were four
of that are going to spend a whole summer working on it.  We're going to
work on expanding it though, and perhaps revisit the ODE model.  So,
we've been learning about the biology involved in iron metabolism, and
how to build a discrete mathematical framework to describe this biology.
 Here is a brief overview of our goals from the [google
group](https://sites.google.com/site/ironmetabolism/home?pli=1) that
[Julia Chifman](http://www.ms.uky.edu/~jchifman/), our research advisor,
has set up:

> <div dir="ltr">
> <span style="font-family:arial, sans-serif;">Welcome to the Iron
> metabolism Project!</span>
> </div>
> <div dir="ltr">
> <span style="font-family:arial, sans-serif;">Computational systems
> biology has brought many new insights to cancer biology through the
> quantitative analysis of molecular networks. </span>
> </div>
> <div dir="ltr">
> <span style="font-family:arial, sans-serif;">The goal of this project
> is to apply a systems biology approach to the understanding of
> intracellular iron metabolism in normal breast epithelium and the
> changes the network undergoes as cells transition to malignancy.
> </span>
> </div>
> <div dir="ltr">
> <span style="font-family:arial, sans-serif;">Our ultimate goal is to
> identify key nodal points that may represent new therapeutic targets
> in the future</span>
> </div>

Here is a picture of the core network:

![](https://2258292711817828768-a-1802744773732722657-s-sites.googlegroups.com/site/ironmetabolism/home/iron_network_small-1.png?attachauth=ANoY7crnsDU2Oyb74otuyhsSz5RIoXeH_2jLqkOivkLZwZeuH6O33jS1xJLJ9HDWdOAS2Vn9NInXJ8tF5gPJn6VNeP5JMPtnn9kKOS5L02R7ugmnZ23FOwLjMBR911FCG5s3fTtxl7B2qaaS_OxrT2LWttM9o57YdSzsZTBxkN0avng8EU2P37o1LnFng-Xu5_4wMETMZ8u-6ObHsGYYFVNRsXxtetMN3X8qq0ec27fa5pqx7QxHul4%3D&attredirects=0 "Iron Metabolism Core Network Cartoon")

After learning about those things, and personally gaining an even better
understanding of the biology, we learned about making truth tables. It
has been truly amazing how working with a group, explaining things, and
being able to dedicate  time to thinking through issues has really
deepened my understanding of modelling as a whole, the biology involved,
and how it comes together.

This past Friday, Julia came to Blacksburg from MBI, and we set to work
on truth tables (the first step in building a mathematical model).  But,
we had problems, in that the tables we made did lead to networks that
had single components with one fixed point, which had been the goal.
 Jim, Emily, and I worked to fix the tables, by trying different effects
while Paul worked on a program to automate the process all Friday
afternoon, but we didn't get anything to really work out.  Over the
weekend, we didn't get a chance to work on it, but instead went over our
presentation for this week, which is supposed to always be on Monday but
it was pushed back to Tuesday.

Today I was really excited because long story short (omitting all of the
math and biology), I got the tables to work.  Paul was still
programming, and Emily and Jim had moved on to the ODE model after we'd
tried a few more things that didn't work.  What I ended up doing was to
throw out the algorithm that Reinhard had developed to make the
polynomials continuous, and instead do that part by hand for more
control in making the tables better reflect biology.  This led me to
making many tables, and after one (massively, I got 35 components when
we're trying for one, the most we've ever got) failed attempt, I even
surprised myself when my second try worked perfectly.  It's paining me a
little to not be able to explain the methods in text sentences, but
basically we're looking at the effect of a handful of protiens on the
Labile Iron Pool (an intracellular pool of loosely bound iron, available
to metabolism (which it needs to be, but too large of an amount is
reactive and harmful to cells, so it is tightly controlled...hence the
entire metabolic network to achieve this)), and using truth tables to
describe the effect that different combinations of the levels of these
protiens have on LIP.  But, we're not considering what LIP's current
state is, just using an algorithm to make the current state move
continuously to the new state, and this is the algorithm I tossed out by
adding LIP's current state as an input to it's future state directly,
and made the tables make more sense biologically, and it all worked out.
This means that the table has 81 entries, instead of 27, but it is
definitely better.  Now, Julia and I are going to see what Reinhard
thinks about all of this (which includes throwing out his own polynomial
algebra paper's algorithm because it doesn't make sense biologically
(according to me)).

So, I'm excited, feeling like I've done some real research, and hope to
accomplish much much more in 9 more weeks!!
