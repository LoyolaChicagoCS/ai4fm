###################
 Table of contents
###################

-  `Table of contents <#table-of-contents>`__

-  `Prerequisites <#prerequisites>`__

-  `The idea <#the-idea>`__

-  `The ``VersionControlSystem`` interface
   <#the-versioncontrolsystem-interface>`__

-  `Implementing ``Git`` <#implementing-git>`__

   -  `The ``__init__`` function <#the-__init__-function>`__
   -  `Counting the number of revisions
      <#counting-the-number-of-revisions>`__
   -  `Extracting revision logs <#extracting-revision-logs>`__
   -  `Parsing revision logs <#parsing-revision-logs>`__

-  `Results <#results>`__

-  `Wrapping up <#wrapping-up>`__

###############
 Prerequisites
###############

I recommend reading my previous article `Version Control Mining Basics
<version-control-mining-basics.md>`__ which explains what is version
control mining, the definitions of base and derived metrics, and why we
care about this with respect to software engineering.

Additionally, we will be computing longitudinal metrics in this series
from the `torvalds/linux
<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/>`__
repository.

Finally, we will be using ``git``, ``python3.13``, and ``gitpython`` to
interface with the software repository. However, we will be developing
tooling that should be easily extensible and modular to support
different ``git`` implementations and libraries, or even different
version control systems entirely.

##########
 The idea
##########

For this post, we are going to extract all of the ``git`` revision log
information into a SQLite3 relational database. This is to showcase how
to extract data from a ``git`` repository and showcase how much faster
it is to store revision log infomration outside of ``git`` for future
processing.

########################################
 The ``VersionControlSystem`` interface
########################################

To start this project off, we are going to creat a generic
``VersionControlSystem`` class that our version control system
implementations can inherit from. This generic will have methods to:

-  Get the total number of revisions in a repository,
-  Get revision log objects, and
-  Parse revision logs,

Since we are using ``python`` for this work, we can implement this class
as follows:

.. code:: python

   from abc import ABC, abstractmethod
   from collections.abc import Iterator


   class VersionControlSystem(ABC):
       def __init__(self) -> None:
           pass

       @abstractmethod
       def count_repository_revisions(self) -> int: ...

       @abstractmethod
       def get_revision_logs(self) -> list | Iterator: ...

       @abstractmethod
       def parse_revision_logs(self) -> list[dict]: ...

######################
 Implementing ``Git``
######################

Now that we have an interface, we can implement it to support ``git``.
To do so, we will be utilizing the ``gitpython`` library as it provides
performant ``python`` tooling for working with ``git`` repositories.

***************************
 The ``__init__`` function
***************************

Our ``__init__`` is fairly simple:

.. code:: python

   from vcs import VersionControlSystem
   from pathlib import Path
   from git import Repo, Commit
   from collections.abc import Iterator


   class Git(VersionControlSystem):
       def __init__(self, repository_path: Path) -> None:
           self.repository_path: Path = repository_path.resolve()
           self.repository: Repo = Repo(path=self.repository_path)

We start by importing our ``VersionControlSystem`` interface we created
in the previous section, as well as the ``pathlib.Path`` and
``git.Repo`` objects. ``pathlib.Path`` enables us to resolve relative
file paths to absolute file paths. ``git.Repo`` provides ``gitpython``
functionality. We then connect to a ``git`` repository using a
filesystem path, and create the ``git.Repo`` object.

**********************************
 Counting the number of revisions
**********************************

While our ``__init__`` method was fairly simple, our
``count_repository_revisions`` implementation is even simpler.

.. code:: python

   ...


   def count_repository_revisions(self) -> int:
       return int(self.repository.git.rev_list("--count", "--all"))

This method utilizes a feature of ``gitpython`` to readily call ``git``
commands. Here we leverage ``git rev-list --all`` which returns a list
of all ``git`` revisions. Adding the ``--count`` flag then counts all of
the revisions for us. We then wrap the output of the command in an
``int`` method to type-cast to an integer value.

**************************
 Extracting revision logs
**************************

``gitpython`` once again makes our lives easy. One of the libraries
methods, ``Repo.iter_commits`` provides trivial access to a ``git``
repository's revision logs.

.. code:: python

   ...


   def get_revision_logs(self) -> Iterator[Commit]:
       return self.repository.iter_commits(rev=self.repository.head.commit)

``iter_commits`` enables the application to ``yield`` commit information
from a repository. This enables both concise application writing (in our
case), but also memory effeciancy as we do not have to buffer all of the
revision logs prior to reading them.

***********************
 Parsing revision logs
***********************

Here is where we need to do some work. Once we get a revision loaded
into memory, we now need to parse the metadata. However, this is also
pretty simple to do thanks to ``iter_commits``.

.. code:: python

   ...


   def parse_revision_logs(self, revision_logs: list | Iterator[Commit]) -> list[dict]:
       data: list[dict] = []
       revision_log: Commit
       for revision_log in revision_logs:
           data.append(
               {
                   "author": revision_log.author,
                   "authored_date": revision_log.authored_date,
                   "author_tz_offset": revision_log.author_tz_offset,
                   "committer": revision_log.committer,
                   "committed_date": revision_log.committed_date,
                   "committer_tz_offset": revision_log.committer_tz_offset,
                   "message": revision_log.message,
                   "encoding": revision_log.encoding,
                   "parents": revision_log.parents,
                   "sha": revision_log.hexsha,
               }
           )

       return data

#########
 Results
#########

Here is an example output from the ``torvalds/linux`` project using the
code we wrote:

.. code:: json

   {
     'author': <git.Actor "Linus Torvalds <torvalds@linux-foundation.org>">,
     'author_tz_offset': 25200,
     'authored_date': 1755270154,
     'committed_date': 1755270154,
     'committer': <git.Actor "Linus Torvalds <torvalds@linux-foundation.org>">,
     'committer_tz_offset': 25200,
     'encoding': 'UTF-8',
     'message': "Merge tag 'io_uring-6.17-20250815' of git://git.kernel.dk/linux\n"
                '\n'
                'Pull io_uring fixes from Jens Axboe:\n'
                '\n'
                ' - Tweak for the fairly recent changes of minimizing io-wq '
                'worker\n'
                "   creations when it's pointless to create them.\n"
                '\n'
                ' - Fix for an issue with ring provided buffers, which could '
                'cause issues\n'
                '   with reuse or corrupt application data.\n'
                '\n'
                "* tag 'io_uring-6.17-20250815' of git://git.kernel.dk/linux:\n"
                '  io_uring/io-wq: add check free worker before create new '
                'worker\n'
                '  io_uring/net: commit partial buffers on retry\n',
     'parents': (<git.Commit "8d084337a32fde0ffa59d5f70d07a54987911ba1">,
                 <git.Commit "9d83e1f05c98bab5de350bef89177e2be8b34db0">),
     'sha': '4ad976b0e8ea3247c607cd37abb09440806f898d'}

While this output does not stringify ``gitpython`` captured objects
(e.g., ``git.Commit``, ``git.Actor``), it is perfectly usable for future
contexts.

#############
 Wrapping up
#############

We've successfully leveraged ``gitpython`` to mine revision log
information from a ``git`` repository. Additionally, we created a
generic ``VersionControlSystem`` class that we will extend later on.

Hopefully this blog post provides a practical introduction to mining
version control systems. The next post will focus on extracting metrics
from ``git`` repositories as well
