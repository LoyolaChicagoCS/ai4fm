######################################
 Hugo, Gopher, Gemini, and Annoyances
######################################

   My story with setting up a Gopher and Gemini compatible website
   powered by Hugo.

----

A little while ago, I wanted to create my own website. I struggle with
creating frontends for websites, so I choose to use the Hugo [0] static
site generator as it has many great themes. Learning Hugo was simple
enough since the most basic sites are just ``md`` content files and
``toml`` config files. So, after a brief learning period, I built my
website, got it hosted on GitHub Pages [1], and setup a domain from
Google Domains [2] to link to it all.

That should be it, right?

Well then I saw these two videos from DistroTube [3] [4] and got
interested in creating and hosting my own Gopher [5] phlog and Gemini
[6] capsule. This is where the annoyances began.

#####################################################
 Gopher: The Bane of my Existence (for about a week)
#####################################################

I wanted to create a Gopher phlog because I thought it was just plain
cool. Who wouldn't want a text only mirror of their site not indexed by
modern search engines (probably everyone)? I was aware the Hugo could
output my website in a variety of different formats. But, I had no idea
how to do that.

Luckily, Jason F. McBrayer had already figured this out in a blog post
on his website [7]. So I copied and pasted away. I ran the Hugo site
generator and I got output! Huzzah! But when I tested the site with the
``gophernicus`` [8] server, the site was malformed. Links to blog pages
lead to nowhere or returned error message.

So I deleted my edits, re-copied, re-pasted (?), and ran the generator.
Still, no dice. Even manually typing in his work into my project didn't
work.

At this point it was getting late, so I put the project into the back of
my head and would continue to work on it for the next week. My
stuborness was because I knew it was possible to do this conversion,
after all, I had gotten output. But there was a syntax error somewhere
that I just couldn't find.

Eventually, I found documentation for the ``gophermap`` syntax [9] and
it all clicked. I use ``neovim`` [10] as my editor of choice. I use
spaces instead of tabs. ``gophermaps``, as a product of the 90s, require
tabs for link formatting.

Insert face palm here.

The fix for this problem was to ``:set noexpandtab`` and then paste in
McBrayer's work.

After that, the links worked. I then spent some time setting the Gopher
template that he provided to what I wanted, but that was minor work.

In all, it took me a week to RTFM and move on from this arguably
ridiculous project.

##################################
 Gemini: A lot easier than Gopher
##################################

It was significantly easier to create the Gemini capsule than a Gopher
Phlog.

But before that, I had to create the templates and output settings for
Gemini in Hugo. This, again, was taken care of by Sylvain Durand [11].
With my\ ``:set noexpandtab`` option, I copied and pasted his work into
my project… And boom! It worked.

That was anticlimatic wasn't it? Again, some formatting of the provided
template was necessary, but that was minor.

The new problem, was how to distribute this site.

#################################
 PubNix: What's Old is New Again
#################################

In my research of both the Gopher and Gemini protocols, I found out
about PubNixs: community ran servers that run on low powered machines.
These servers are a modern implementation of the time sharing servers of
yore where there were a few large mainframes in the country that only a
few people could log into at a time. A subset of these PubNixs is the
``tildeverse`` [12]. These are **very** community oriented servers that
offer free webhosting of the Gemini, Gopher, HTTP, and Spartan sites.
All that's required is to create an account and start uploading.

For those that are interested in hosting a Gemini and/or Gopher site, I
encourage the usage of these servers as it takes the problems of hosting
content (maintainence, privacy, port forwarding, etc.) off of your
shoulders

#########
 The End
#########

If you ware interested in doing something similar, here is a link to my
websites source code on GitHub [13]. There you can see my templates,
scripts, and config options for generating Gemini, Gopher and HTTP
sites. Best of luck, and happy hacking!

----

###########
 Citations
###########

Citations availible at
https://nsynovic.dev/posts/hugo-gopher-gemini-annoyance/
