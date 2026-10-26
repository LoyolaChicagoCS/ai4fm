Can LLMs Write Correct TLA+ Specifications? Evaluating Natural-Language-to-TLA+ Generation
============================================================================================

:Status: Published
:Venue: ICSOFT 2026 — 21st International Conference on Software Technologies, Porto, Portugal, July 16–18, 2026, pp. 39–50
:Authors: Arslan Bisharat, Brian Ortiz, Eric Spencer, Khushboo Bhadauria, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, Mohammed Abuhamad
:DOI / PDF: `10.5220/0015070400004088 <https://doi.org/10.5220/0015070400004088>`__ | `View published PDF <https://www.scitepress.org/PublishedPapers/2026/150704/150704.pdf>`__



.. raw:: html
   :file: _figures/llm-evaluation-dots.html

Abstract
--------

TLA+ has supported industrial verification at companies such as Amazon and Microsoft,
yet writing correct TLA+ specifications from natural language still requires significant
time and expertise, which limits adoption. LLMs show promise, but no prior study measures
whether they produce semantically correct TLA+ specifications from natural language.

This paper presents the first systematic evaluation of LLM-based TLA+ specification
synthesis from natural language. Our study evaluates 30 LLMs across eight families on a
curated dataset of 205 TLA+ specifications: 25 open-weight models across four prompting
strategies (2,600 runs) and 5 proprietary models under few-shot prompting (130 runs),
all validated by the SANY parser and TLC model checker.


Key Results
-----------

.. list-table::
   :header-rows: 1

   * - Metric
     - Best Result
   * - Syntactic correctness (SANY)
     - **26.6%**
   * - Semantic correctness (TLC)
     - **8.6%**
   * - Prompting strategy enabling semantic success
     - Progressive prompting only


Surprising Findings
-------------------

**Model size does not predict quality.**
DeepSeek r1:8b outperforms its 70b variant across all prompting strategies.
This suggests that reasoning alignment for formal languages matters more than
raw parameter count.

**Code-specialized models consistently underperform.**
Models trained heavily on mainstream programming languages show negative transfer
when applied to TLA+. Familiarity with Python or Java does not generalize to
formal specification languages.

**Semantic success requires progressive prompting.**
Across all evaluations, semantic correctness - specifications that pass the TLC
model checker - was only achieved under progressive prompting strategies.
Direct and few-shot prompting failed to produce semantically valid outputs.


Why This Matters
----------------

TLA+ is not a niche language. It has been used to verify core distributed systems
at Amazon Web Services (DynamoDB, S3), Microsoft Azure, and other production environments.
If LLMs could reliably generate TLA+ from natural language, formal verification could
become far more accessible to engineers who understand their system but lack specification expertise.

This paper shows that current LLMs are not there yet. Reaching reliable TLA+ generation
will require targeted work on reasoning alignment, formal language training data,
and evaluation-driven prompting strategies - all active directions for AI4FM.


In Plain Words
--------------

TLA+ is a language for writing exact descriptions of how a system should behave, and a tool called TLC checks those descriptions. Big companies such as Amazon and Microsoft have used it to check important systems. But writing TLA+ well takes time and training, and that is one reason more people do not use it. It would help a lot if an AI model could write the first draft from a plain-English description.

This paper asks a simple question: can today's AI models do that? Nobody had measured it carefully, so the team did. They used 205 TLA+ specifications and tested 30 models from eight families. Twenty-five of the models were open-weight, and each was tried with four different prompting styles, for 2,600 runs. Five were proprietary models, tried with a few worked examples, for 130 runs. Every answer was checked twice. A parser called SANY checked that the text was in the right form, and TLC checked whether it behaved correctly.

The answer is "not yet." At best, about a quarter of the outputs (26.6%) were in the right form, and only 8.6% passed TLC.

Three results stood out. First, bigger was not better: a smaller DeepSeek model (8b) beat its own larger 70b version in every setup. Second, models trained mostly on programming code did worse, not better, on TLA+. Knowing Python or Java did not carry over to a very different kind of language. Third, passing TLC happened only with progressive prompting, a style the paper contrasts with asking directly or showing a few examples.

The lesson is that making AI useful for formal methods will need more than larger models. It will need better training data in formal languages, better reasoning, and careful testing that actually runs the results.

Citation
--------

Arslan Bisharat, Brian Ortiz, Eric Spencer, Khushboo Bhadauria, TaiNing Wang,
George K. Thiruvathukal, Konstantin Läufer, and Mohammed Abuhamad,
*Can LLMs Write Correct TLA+ Specifications? Evaluating Natural-Language-to-TLA+
Generation*, Proceedings of the 21st International Conference on Software Technologies
(ICSOFT 2026), pp. 39–50, 2026. https://doi.org/10.5220/0015070400004088


BibTeX
------

.. code-block:: bibtex

   @inproceedings{bisharat2026llmtla,
     title     = {Can {LLMs} Write Correct {TLA+} Specifications? Evaluating Natural-Language-to-{TLA+} Generation},
     author    = {Bisharat, Arslan and Ortiz, Brian and Spencer, Eric and Bhadauria, Khushboo and Wang, TaiNing and Thiruvathukal, George K. and Läufer, Konstantin and Abuhamad, Mohammed},
     booktitle = {Proceedings of the 21st International Conference on Software Technologies (ICSOFT 2026)},
     pages     = {39--50},
     year      = {2026},
     address   = {Porto, Portugal},
     doi       = {10.5220/0015070400004088}
   }
