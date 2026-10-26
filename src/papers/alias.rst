ALIAS: Evaluating Performance and Memorization in LLM-Written TLA+ Specifications
=================================================================================

:Status: Preprint
:Date: October 2026
:Authors: Arslan Bisharat, Mujtaba Nazari, Khushboo Bhadauria, Brian Ortiz, Eric Spencer, Beatriz Santos, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, Mohammed Abuhamad
:Institution: Loyola University Chicago
:Paper: `arXiv:2610.29767 <https://arxiv.org/abs/2610.29767>`__ | `PDF <https://arxiv.org/pdf/2610.29767>`__
:DOI: `10.48550/arXiv.2610.29767 <https://doi.org/10.48550/arXiv.2610.29767>`__
:Artifact: `Code and data <https://github.com/LUC-AI4FM/ALIAS>`__


Abstract
--------

A common way to test whether a language model has memorized its benchmark is to rename
every identifier in each task and see whether performance drops. ALIAS examines whether
that test can be trusted for TLA+ specifications. It uses 111 TLA+ tasks and the TLA+
model checker to confirm that renamed tasks keep the behavior of the original. Renaming
lowers correctness for Claude Opus 4.8 and GPT-5, but much of the drop comes from grading
that requires exact names, and behavior-based grading shrinks the gap substantially. In
fine-tuned Qwen and Gemma models, renaming removes about half of the training gain in
likelihood and lowers accuracy on unseen tasks. A lower score after renaming therefore
mixes memorization, name-based grading, and the cost of unfamiliar names. The full
abstract is on `arXiv <https://arxiv.org/abs/2610.29767>`__.


Why This Matters
----------------

Benchmarks are only useful if a good score reflects skill and not recall of the answer.
Renaming is a cheap and popular check, but this paper shows that its result is easy to
misread. Separating the three causes makes memorization claims about LLMs and formal
methods more reliable.


In Plain Words
--------------

AI models learn from huge amounts of text, and some of that text may include the very
problems used to test them. When that happens, a model can score well because it has
seen the answer before, not because it can solve the problem. This is called
memorization, and it makes a test score look better than it should.

A popular way to check for memorization is to rename things. In a TLA+ task, you change
the names of the variables and other identifiers everywhere, but keep the meaning
exactly the same. If the model only remembered the old answer, the new names should
throw it off, and its score should drop.

This paper asks whether that test is as clear as it seems. The team used 111 TLA+ tasks.
Because TLA+ has a model checker, they could check that a renamed task still behaves
exactly like the original. That is hard to do with ordinary code, and it is one reason
TLA+ is a good place to study the question.

Renaming did lower the scores of Claude Opus 4.8 and GPT-5. But much of that drop came
from the way the answers were graded. If a grader asks for the exact names, then an
answer that behaves correctly but uses different names counts as wrong. When the team
graded by behavior instead, the gap shrank a lot.

They also tested fine-tuned Qwen and Gemma models, which were trained further on TLA+
tasks. Renaming took away about half of what the training had gained, measured by how
likely the model found the correct text, and it lowered accuracy on tasks the model had
not seen before.

The takeaway is that a lower score after renaming is not proof of memorization. It mixes
three things: memorization, grading that depends on names, and the extra difficulty of
unfamiliar names. To understand what a model really knows, those three need to be pulled
apart.


Citation
--------

Arslan Bisharat, Mujtaba Nazari, Khushboo Bhadauria, Brian Ortiz, Eric Spencer,
Beatriz Santos, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, and
Mohammed Abuhamad. *ALIAS: Evaluating Performance and Memorization in LLM-Written
TLA+ Specifications*. arXiv:2610.29767, 2026. https://doi.org/10.48550/arXiv.2610.29767


BibTeX
------

.. code-block:: bibtex

   @misc{bisharat2026alias,
     title         = {{ALIAS}: Evaluating Performance and Memorization in {LLM}-Written {TLA+} Specifications},
     author        = {Bisharat, Arslan and Nazari, Mujtaba and Bhadauria, Khushboo and Ortiz, Brian and Spencer, Eric and Santos, Beatriz and Wang, TaiNing and Thiruvathukal, George K. and Läufer, Konstantin and Abuhamad, Mohammed},
     year          = {2026},
     eprint        = {2610.29767},
     archivePrefix = {arXiv},
     doi           = {10.48550/arXiv.2610.29767},
     url           = {https://arxiv.org/abs/2610.29767}
   }
