:blogpost:
   true

:date:
   Oct 10, 2020

:author:
   Nabil Freij

:location:
   World

:category:
   Manual

:language:
   English

#############################
 Back To Basics With ``git``
#############################

##################
 Not to brag, but
##################

I can use ``git`` (like everyone else). I've been using ``git`` since
~2016 and its been my primary VCS tooling throughout university. I've
also `published research <https://arxiv.org/abs/2207.11767>`__ that
leverages ``git`` and GitHub to derive project insights. I've been very
fond of the technology, but have come to realize that I'm not adequetly
leveraging both, and thus hindering my progress.

So for today's post, I want to optimize my ``git`` config to maximize my
productivity when using the tool.

###############
 Mr. Worldwide
###############

``git`` can be configured globally, system-wide, or on a per-project
basis. When configured globally, it affects every project for that
particular user. For me, this is my preferred configuration option as
I'm often working on solo-projects.

The ``git`` documentation for ``git config`` can be viewed `here
<https://git-scm.com/docs/git-config#Documentation/git-config.txt-alias>`__.
If you are following along, this is the file stored at:
``~/.gitconfig``. Each option can be configured with ``git config
--global --add KEY VALUE``, but I'll be displaying the output from the
file itself. To start, we'll configure ``git blame``

####################
 "It's Your Fault!"
####################

``git blame`` reports who contributed each line in a given file. This is
particularly useful when identifying who contributed a specific feature,
created a bug, or maliciously tampered with a file. There isn't much to
configure here, but I will turn on repeated line coloring (for repeated
lines contributed in a commit), using the UNIX Epoch as the time format,
and reporting author email addresses over names.

.. code:: text

   [blame]
       coloring = repeatedLines
       date = unix
       showEmail = true

#######################
 Color Makes It Cooler
#######################

I typically work in terminals that support ANSI color codes, so anytime
that I can add a splash of color to my development experience is
pleasant. I've made ``git`` output most of its UI in color if possible
using the ``ui.color`` config option set to ``auto``.

.. code:: text

   [color]
       ui = auto

##########################
 All My Ducks In A Column
##########################

Some of ``git``'s commands can be formatted as columnar output. However,
I don't know which commands they are? It's undocumented as to which
commands are affected, but it does affect ``git blame`` and I like
standardized output so I'm going to set it to always be on.

.. code:: text

   [column]
       ui = always

#############
 Signing Off
#############

I wrote a Dev.to post on why `you should sign your commits with GPG
<https://dev.to/nicholassynovic/why-sign-commits-1nlb>`__, and I still
stand by that post today. While tedious to setup and maintain across
workstations, it does provide a layer of collaborator authentication.

.. code:: text

   [commit]
       gpgSign = true

#############
 Speed Demon
#############

Some of the work that I do involves assessing the quality of software
repositories longitudinally. Thus, I'm often checking out many commits
sequentially in a ``git`` repository. Therefore, when I heard about the
``core.fsmonitor`` config option, I was ecstatic. This option, "can
speed up Git commands that need to refresh the Git index (e.g. git
status) in a working directory with many files. The built-in monitor
eliminates the need to install and maintain an external third-party
tool" (`Source
<https://git-scm.com/docs/git-config#Documentation/git-config.txt-corefsmonitor>`__).

In my testing, I found that when checking out 500 commits sequentially
from the ```numpy`` repository <https://github.com/numpy/numpy>`__,
disabling this feature required 13.8 seconds to complete on average
across 10 runs. Enabling this feature took on average 11.2 seconds
across 10 runs. Not an astounding difference in testing, but if
``core.fsmonitor`` can save me 2.6 seconds per 500 commits, on a project
with 37,775 commits that could add up to a time savings of 211.54
seconds, or 3 minutes and 32 seconds! More testing on my end needs to be
done if this feature scales linearly, but for now I will keep it on and
use version 1 of the tool.

.. code:: text

   [core]
           fsmonitor = true
           fsmonitorHookVersion = 1

###############
 Core Defaults
###############

In addition to the ``fsmonitor`` config, I also leverage ``nvim`` and
``less`` as my editor and pager of choice.

.. code:: text

   [core]
           fsmonitor = true
           fsmonitorHookVersion = 1
           editor = nvim
           pager = less

############################
 Optimizing Nodes And Edges
############################

``git`` can create a graph of how every commit relates to one another.
This allows for efficiently applying patches to a commit once checked
out. However, this has to be done manually with ``git commit-graph
write``. We can automate some of this by enabling the commit graph to be
written anytime ``git fetch`` is called.

.. code:: text

   [fetch]
       writeCommitGraph = true

##############################
 Don't Forget About The User!
##############################

Finally, I'll configure my name and email for ``git``.

.. code:: text

   [user]
       name = Nicholas M. Synovic
       email = ***

#############
 Wrapping Up
#############

I know that I've skipped over many different configuration options that
``git`` has to offer. So consider this post and my config a jumping off
point that you can extend.

My full config is:

.. code:: text

   [blame]
           coloring = repeatedLines
           date = unix
           showEmail = true
   [color]
           ui = auto
   [column]
           ui = always
   [commit]
           gpgSign = true
   [core]
           fsmonitor = true
           fsmonitorHookVersion = 1
           editor = nvim
           pager = less
   [fetch]
       writeCommitGraph = true
   [user]
       name = Nicholas M. Synovic
       email = ***
