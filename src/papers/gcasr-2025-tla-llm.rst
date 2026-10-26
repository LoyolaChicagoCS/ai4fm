Automating TLA+ Model Synthesis with Large Language Models and Formal Verification Pipelines
============================================================================================

*Work in Progress*

:Status: Presented
:Venue: GCASR 2025 - 12th Greater Chicago Area Systems Research Workshop, May 8, 2025, Loyola University Chicago
:Authors: Brian Ortiz, Mohammed Abuhamad, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer
:Institution: Loyola University Chicago
:DOI / Poster: `10.6084/m9.figshare.31896151.v3 <https://doi.org/10.6084/m9.figshare.31896151.v3>`__



Abstract
--------

This work-in-progress presents a pipeline for automating TLA+ model synthesis
using large language models, coupled with formal verification via the SANY parser and
TLC model checker. The system takes natural language descriptions of concurrent or
distributed systems and attempts to generate syntactically and semantically correct
TLA+ specifications, evaluated through automated verification pipelines.


Why This Matters
----------------

TLA+ specification writing requires significant expertise, limiting adoption in
industry and academia. Automating synthesis with LLMs - while ensuring correctness
through formal verification - could make TLA+ accessible to a much broader audience
of engineers and researchers.


In Plain Words
--------------

This is an early, work-in-progress poster. It shows an early version of the group's approach to TLA+ and language models.

The goal is to let a person describe a system in ordinary language, for example how several computers should share a resource, and have an AI model write the matching TLA+ specification. TLA+ is a language for describing systems exactly, and a tool called TLC can check them. Writing TLA+ well takes real skill, and that skill is rare. This slows down its use in companies and in classrooms.

The catch is that AI models make mistakes, and a specification that looks right can still be wrong. So the poster does not just ask the model for an answer. It builds a pipeline that checks the answer automatically. First, a parser called SANY checks that the text is written in the right form. Then the TLC model checker checks that the specification behaves as intended. The system is evaluated through these automated checks.

Because tools run the checks and not a person reading the result, the verdict does not depend on anyone's opinion.

At this stage the poster describes the plan and the setup, not final results. Its value is the direction: if AI-written specifications can be verified automatically, a much wider group of engineers and researchers might be able to use formal methods.

Citation
--------

Brian Ortiz, Mohammed Abuhamad, TaiNing Wang, George K. Thiruvathukal, and Konstantin Läufer,
*Automating TLA+ Model Synthesis with Large Language Models and Formal Verification Pipelines (WIP)*,
GCASR 2025, May 8, 2025.
https://doi.org/10.6084/m9.figshare.31896151.v3


BibTeX
------

.. code-block:: bibtex

   @misc{ortiz2025gcasr,
     title        = {Automating {TLA+} Model Synthesis with Large Language Models and Formal Verification Pipelines ({WIP})},
     author       = {Ortiz, Brian and Abuhamad, Mohammed and Wang, TaiNing and Thiruvathukal, George K. and Läufer, Konstantin},
     year         = {2025},
     month        = may,
     howpublished = {Poster, 12th Greater Chicago Area Systems Research Workshop (GCASR), Loyola University Chicago},
     doi          = {10.6084/m9.figshare.31896151.v3}
   }
