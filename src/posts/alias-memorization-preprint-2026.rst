:blogpost: true
:date: October 26, 2026
:author: AI4FM
:category: Research Update
:tags: Formal Methods, TLA+, LLMs, Preprint
:nocomments:

New Preprint: Does Renaming Reveal Memorization in LLM-Written TLA+?
====================================================================

We have posted a new preprint, **ALIAS: Evaluating Performance and Memorization in
LLM-Written TLA+ Specifications**, on arXiv.

A common way to test whether a language model has memorized a benchmark is to rename
every identifier in each task and see whether the score drops. Using 111 TLA+-Bench tasks,
and the TLC model checker to confirm that renamed tasks keep the behavior of the original,
we find that renaming does lower the scores of Claude Opus 4.8 and GPT-5. Most of that drop,
however, comes from grading that requires exact names the descriptions never state. Grading
by behavior shrinks the drop to about 3 points for Opus 4.8 and to 0 for GPT-5.

We release the renamed tasks, the model outputs, and the behavior-based grader.

`Read the full paper details <../../papers/alias/>`__
