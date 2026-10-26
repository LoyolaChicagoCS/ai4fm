Large Language Models (LLM) and Temporal Logic of Actions (TLA): How Effective are LLMs for Verification Systems
===================================================================================================================

:Status: Presented
:Venue: GSIRS 2026 - Graduate School Interdisciplinary Research Symposium, April 11, 2026, Loyola University Chicago
:Authors: Brian Ortiz, Arslan Bisharat, Mohammed Abuhamad, Konstantin Läufer, Eric Spencer, Khushboo Bhadauria, George K. Thiruvathukal, TaiNing Wang
:Institution: Loyola University Chicago
:DOI / Poster: `10.6084/m9.figshare.31988706.v1 <https://doi.org/10.6084/m9.figshare.31988706.v1>`__



Abstract
--------

TLA+ has supported industrial verification at companies such as Amazon and Microsoft,
yet writing correct TLA+ specifications from natural language still requires time and
expertise, which limits adoption. LLMs show promise, but no prior study measures whether
they produce semantically correct TLA+ specifications from natural language.

This paper presents the first systematic evaluation of LLM-based TLA+ specification
synthesis from natural language. Our study evaluates 30 LLMs across eight families on a
curated dataset of 205 TLA+ specifications: 25 open-weight models across four prompting
strategies (2,600 runs) and 5 proprietary models under few-shot prompting (130 runs),
all validated by the SANY parser and TLC model checker. LLMs achieve up to 26.6%
syntactic correctness but only 8.6% semantic correctness, with successes exclusive to
progressive prompting. Results show that model size does not predict quality, and
code-specialized models consistently underperform due to negative transfer from mainstream
language training.


Based On
--------

This poster is based on the :doc:`published ICSOFT 2026 paper
<../papers/llm-tla-evaluation>`.


In Plain Words
--------------

This poster is a short, visual version of the group's ICSOFT 2026 paper. It was shown at the Graduate School Interdisciplinary Research Symposium at Loyola in April 2026.

The question is whether AI models can write TLA+ specifications, which are exact descriptions of how a system should behave, starting from a plain-English description. Companies like Amazon and Microsoft use TLA+ to check important systems, but it takes skill and time to write. If AI could do the first draft, more engineers could use it.

To find out, the team tested 30 models on 205 TLA+ specifications. Each answer went through two checks. A parser called SANY asked whether the text was written in the right form. The TLC model checker asked whether it behaved correctly. Passing the first check is like having correct spelling. Passing the second is like having a sentence that actually makes sense.

The results are on the poster in three points. First, the models did much better on form than on meaning: up to 26.6% passed the parser, but only 8.6% passed TLC. Second, a bigger model is not automatically a better one. A smaller DeepSeek model beat its own larger version. Third, models built mainly to write code did worse on TLA+, probably because the habits they learned from popular programming languages do not carry over. And the only runs that passed TLC used progressive prompting.

In short, the poster says that today's AI is not ready to write formal specifications on its own, and it points to where to work next: better training for formal languages and better ways of asking.

Citation
--------

Brian Ortiz, Arslan Bisharat, Mohammed Abuhamad, Konstantin Läufer, Eric Spencer,
Khushboo Bhadauria, George K. Thiruvathukal, and TaiNing Wang,
*Large Language Models (LLM) and Temporal Logic of Actions (TLA): How Effective are LLMs for Verification Systems*,
GSIRS 2026, April 11, 2026.
https://doi.org/10.6084/m9.figshare.31988706.v1


BibTeX
------

.. code-block:: bibtex

   @misc{ortiz2026gsirs,
     title        = {Large Language Models ({LLM}) and Temporal Logic of Actions ({TLA}): How Effective are {LLMs} for Verification Systems},
     author       = {Ortiz, Brian and Bisharat, Arslan and Abuhamad, Mohammed and Läufer, Konstantin and Spencer, Eric and Bhadauria, Khushboo and Thiruvathukal, George K. and Wang, TaiNing},
     year         = {2026},
     month        = apr,
     howpublished = {Poster, Graduate School Interdisciplinary Research Symposium (GSIRS), Loyola University Chicago},
     doi          = {10.6084/m9.figshare.31988706.v1}
   }
