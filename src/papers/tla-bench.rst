TLA+-Bench: An Execution-Grounded Benchmark and Dataset for Natural-Language to TLA+ Specification Generation
=============================================================================================================

:Date: July 2026
:Authors: Arslan Bisharat, Eric Spencer, Brian Ortiz, Khushboo Bhadauria, Mujtaba Nazari, Beatriz Santos, Anisa Ramos, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, Mohammed Abuhamad
:Institution: Loyola University Chicago
:Paper: `arXiv:2607.23425 <https://arxiv.org/abs/2607.23425>`__ | `PDF <https://arxiv.org/pdf/2607.23425>`__
:DOI: `10.48550/arXiv.2607.23425 <https://doi.org/10.48550/arXiv.2607.23425>`__
:Artifact: `Benchmark, dataset, and reproduction code <https://github.com/LUC-AI4FM/tla_benchmark/tree/reviewer-release>`__
:BibTeX: :download:`Download citation </_static/bibtex/tla-bench.bib>`


.. figure:: /_static/images/PXL_20260511_164300028.jpg
   :alt: AI4FM presenting research at GCASR 2026.
   :class: paper-figure

   AI4FM presenting research at GCASR 2026.


.. raw:: html

   <figure class="paper-workflow" aria-label="Natural-language task to Generated TLA+ specification to SANY parsing to TLC model checking"><ol><li>Natural-language task</li><li>Generated TLA+ specification</li><li>SANY parsing</li><li>TLC model checking</li></ol><figcaption>Research workflow</figcaption></figure>


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


Citation
--------

Arslan Bisharat, Eric Spencer, Brian Ortiz, Khushboo Bhadauria, Mujtaba Nazari,
Beatriz Santos, Anisa Ramos, TaiNing Wang, George K. Thiruvathukal, Konstantin
Läufer, and Mohammed Abuhamad. *TLA+-Bench: An Execution-Grounded Benchmark and
Dataset for Natural-Language to TLA+ Specification Generation*. arXiv:2607.23425,
2026. https://doi.org/10.48550/arXiv.2607.23425
