TLA+-Bench: An Execution-Grounded Benchmark and Dataset for Natural-Language to TLA+ Specification Generation
=============================================================================================================

*Preprint / Under review*

:Status: Preprint / Under review
:Date: July 2026
:Authors: Arslan Bisharat, Eric Spencer, Brian Ortiz, Khushboo Bhadauria, Mujtaba Nazari, Beatriz Santos, Anisa Ramos, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, Mohammed Abuhamad
:Institution: Loyola University Chicago
:Paper: `arXiv:2607.23425 <https://arxiv.org/abs/2607.23425>`__ | `PDF <https://arxiv.org/pdf/2607.23425>`__
:DOI: `10.48550/arXiv.2607.23425 <https://doi.org/10.48550/arXiv.2607.23425>`__
:Artifact: `Benchmark, dataset, and reproduction code <https://github.com/LUC-AI4FM/tla_benchmark/tree/reviewer-release>`__
:Leaderboard: :doc:`Model results on the gold specifications <../pages/leaderboard>`



.. raw:: html
   :file: _figures/tla-bench-dots.html

Abstract
--------

TLA+-Bench is an execution-grounded benchmark for measuring whether models can
produce correct TLA+ specifications from natural-language descriptions. It contains
1,300 specifications drawn from 13 public repositories: 403 TLC-model-checked gold
specifications and 897 parse-only silver specifications. Each gold specification
ships with a model-checker configuration, allowing evaluation to measure execution
rather than similarity to a reference answer.


Why This Matters
----------------

Parsing a generated specification is not the same as establishing that it is correct.
TLA+-Bench makes that distinction measurable and exposes how much results change when
evaluation choices are made explicit. It supplies a reproducible dataset, grader, and
model outputs for research on natural-language-to-TLA+ generation.

The benchmark follows the earlier :doc:`GCASR 2026 structured-benchmarking poster
<../posts/gcasr-2026-posters>`.


In Plain Words
--------------

Imagine asking a computer to write down the rules of a system, such as how several computers agree on one answer. The rules have to be exact, because a small mistake can hide a big problem. TLA+ is a language for writing rules like these. A tool called TLC can then try the ways the system could run and tell you if a rule is ever broken.

Today, people ask AI models to write TLA+ rules from a plain-English description. The hard question is how to tell whether the AI did a good job. One easy check is whether the file is written in the right form. That is like checking spelling. A sentence can be spelled perfectly and still say the wrong thing. A better check is to actually run the rules through TLC and see what happens.

TLA+-Bench is a collection built for that purpose. It holds 1,300 TLA+ specifications taken from 13 public projects. Of these, 403 are "gold": each was run through TLC, and each comes with the settings needed to run it again. The other 897 are "silver": we only checked that they are written in a valid form.

When a model is tested, its answer is graded by running it, not by comparing its words with a reference answer. This matters because the same system can be described correctly in many different ways, and a word-by-word match would punish good answers.

The paper also points out that results can change a lot depending on small choices in how a test is run. By making those choices visible, the benchmark lets people see why two studies might disagree. The team released the data, the grader and the models' answers, so other researchers can repeat the work and compare their own models fairly.

Citation
--------

Arslan Bisharat, Eric Spencer, Brian Ortiz, Khushboo Bhadauria, Mujtaba Nazari,
Beatriz Santos, Anisa Ramos, TaiNing Wang, George K. Thiruvathukal, Konstantin
Läufer, and Mohammed Abuhamad. *TLA+-Bench: An Execution-Grounded Benchmark and
Dataset for Natural-Language to TLA+ Specification Generation*. arXiv:2607.23425,
2026. https://doi.org/10.48550/arXiv.2607.23425


BibTeX
------

.. code-block:: bibtex

   @misc{bisharat2026tlabench,
     title         = {{TLA+-Bench}: An Execution-Grounded Benchmark and Dataset for Natural-Language to {TLA+} Specification Generation},
     author        = {Bisharat, Arslan and Spencer, Eric and Ortiz, Brian and Bhadauria, Khushboo and Nazari, Mujtaba and Santos, Beatriz and Ramos, Anisa and Wang, TaiNing and Thiruvathukal, George K. and Läufer, Konstantin and Abuhamad, Mohammed},
     year          = {2026},
     eprint        = {2607.23425},
     archivePrefix = {arXiv},
     doi           = {10.48550/arXiv.2607.23425},
     url           = {https://arxiv.org/abs/2607.23425}
   }
