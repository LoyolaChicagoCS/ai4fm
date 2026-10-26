TLA+ for All: Model Checking in a Python Notebook
==================================================

:Status: Preprint
:Venue: figshare, February 2025
:Authors: Konstantin Laufer, George K. Thiruvathukal
:DOI / PDF: `10.6084/m9.figshare.28376276.v1 <https://doi.org/10.6084/m9.figshare.28376276.v1>`__



Overview
--------

TLA+ is a powerful formal specification language for designing and verifying concurrent
and distributed systems. But for many students and practitioners, the ecosystem has felt
inaccessible - requiring specialized tooling, complex installation steps, and the
perception that formal methods are only for specialists.

This project changes that by embedding TLA+ model checking directly into a Python
notebook environment. Anyone who can open a browser can now write specifications,
run the TLC model checker, explore counterexamples, and visualize system behaviors.


The Problem: Accessibility Barriers in Formal Methods
------------------------------------------------------

Despite decades of success in verifying critical systems, TLA+ adoption remains limited.
The barriers are real:

- The TLC model checker requires a local Java installation and command-line setup
- The TLA+ Toolbox IDE is unfamiliar to students used to notebook-based workflows
- No standard way exists to combine specifications, narrative, and results in a
  reproducible and shareable format
- Workshop and classroom use requires every participant to install and configure tooling

These barriers disproportionately affect students encountering formal methods for the
first time and instructors at institutions without dedicated systems support.


The Solution: TLA+ in a Notebook
----------------------------------

By integrating TLA+ into a Python notebook environment (Jupyter/JupyterLite):

.. list-table::
   :header-rows: 1

   * - Feature
     - Description
   * - In-browser TLC execution
     - Run TLA+ model checker without installing anything
   * - Literate specifications
     - Mix TLA+ code, prose, and results in one notebook
   * - Trace visualization
     - Explore counterexamples and behaviors interactively
   * - Reproducibility
     - Share a URL and anyone can re-run the full analysis
   * - No setup friction
     - Classroom and workshop ready - open a link and start


Use Cases
----------

**Teaching and workshops** - No setup friction. Students open a URL and start writing specs.

**Research documentation** - Executable specifications embedded in research papers and reports.

**Exploratory modeling** - Engineers sketch system designs and check properties without
committing to a full tool installation.

**Tutorials and onboarding** - New team members explore a codebase's formal model
before touching the implementation.


In Plain Words
--------------

Formal methods have a reputation for being only for experts. Part of the reason is plain inconvenience. To check a TLA+ specification you normally install Java, set up the TLC model checker on the command line, or learn a separate program called the TLA+ Toolbox. If you are teaching a class, every student has to do this on their own machine, and something always goes wrong.

This project removes that wall. It puts TLA+ model checking inside a Python notebook, the kind of page that mixes text, code and results that many students already know. You open a link in your browser, write a specification, run TLC, and look at what happened, all in one place. Nothing has to be installed.

A few features follow from that. You can mix your specification with ordinary writing, so a reader sees the explanation next to the rules it describes. If TLC finds a problem, you can explore the example that breaks the rule and see how the system's behavior unfolded. And because everything lives in one shared page, anyone with the link can re-run the whole analysis and get the same answer.

The paper lists a few places this helps. In a class or workshop, students can begin writing specifications in the first minute. In research, a paper can carry specifications that readers can actually run. Engineers can sketch a design and test an idea without committing to a full tool setup. And new team members can explore the formal model of a codebase before touching the real code.

The idea is simple, but it lowers the cost of the first step. When trying something takes one click, many more people will try it.

Citation
--------

Konstantin Laufer and George K. Thiruvathukal,
*TLA+ for All: Model Checking in a Python Notebook*,
figshare, February 2025.
https://doi.org/10.6084/m9.figshare.28376276.v1


BibTeX
------

.. code-block:: bibtex

   @misc{laufer2025tlaforall,
     title        = {{TLA+} for All: Model Checking in a {Python} Notebook},
     author       = {Laufer, Konstantin and Thiruvathukal, George K.},
     year         = {2025},
     month        = feb,
     howpublished = {figshare},
     doi          = {10.6084/m9.figshare.28376276.v1}
   }
