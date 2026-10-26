TLA-Prover: Verifiable TLA+ Specification Synthesis via Preference-Optimized Low-Rank Adaptation
=================================================================================================

:Status: Published
:Venue: ICSOFT 2026 — 21st International Conference on Software Technologies, Porto, Portugal, July 16–18, 2026, pp. 627–636
:Authors: Eric Spencer, Arslan Bisharat, Brian Ortiz, Mujtaba Nazari, Khushboo Bhadauria, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, Mohammed Abuhamad
:DOI / PDF: `10.5220/0015234600004088 <https://doi.org/10.5220/0015234600004088>`__ | `View published PDF <https://www.scitepress.org/PublishedPapers/2026/152346/152346.pdf>`__



.. raw:: html
   :file: _figures/tla-prover-dots.html

Abstract
--------

TLA+ is a formal specification language for verifying distributed systems and safety-critical
protocols. Large language models (LLMs) frequently produce TLA+ specifications that fail the TLC
model checker for semantic reasons. Across 25 LLMs, the best public baseline is 26.6% syntactic
parse and 8.6% semantic model-check. We present TLA-Prover, a 20-billion-parameter model for
TLA+ specification synthesis. Training combines supervised fine-tuning (SFT) on verified examples
with repair-based group-relative policy optimization (GRPO). In the GRPO stage, the model learns
to fix its own rejected specifications. We also train a direct preference optimization (DPO)
variant from the same SFT checkpoint as an ablation. TLC provides the reward signal directly,
with no learned reward model.

Four tiers grade each output: Bronze (parses), Silver (no warnings), Gold (passes TLC), and
Diamond. To reach Diamond, the model's correctness property is automatically altered in a small
way; TLC must then detect a violation. If TLC still passes, the property was always-true and
contributes nothing; the output fails Diamond. TLA-Prover reaches 9/30 (pass@1 = 30%) at both
Gold and Diamond on a held-out 30-problem benchmark. This is roughly 3.5× the 8.6% untuned
baseline. The DPO variant reaches 20% at Diamond. Gold and Diamond coincide at every checkpoint,
preventing the trivial-property failure mode.


Key Results
-----------

.. list-table::
   :header-rows: 1

   * - Metric
     - Result
   * - Syntactic correctness — best public baseline
     - 26.6%
   * - Semantic correctness — best public baseline (8.6% untuned)
     - 8.6%
   * - TLA-Prover Gold (passes TLC) pass@1
     - **30%**
   * - TLA-Prover Diamond pass@1
     - **30%**
   * - DPO variant Diamond pass@1
     - 20%
   * - Improvement over untuned baseline
     - ~3.5×



Training Approach
-----------------

**Supervised Fine-Tuning (SFT)**
The model is first trained on a curated set of verified TLA+ specifications to establish a
strong syntactic and semantic foundation.

**Group-Relative Policy Optimization (GRPO)**
In the GRPO stage, the model generates multiple candidate specifications per prompt. Rejected
outputs are used as repair targets, teaching the model to iteratively correct its own mistakes.
TLC model-checker output serves as the reward signal — no learned reward model is involved.

**Direct Preference Optimization (DPO) ablation**
A DPO variant is trained from the same SFT checkpoint to compare preference-optimization
strategies. It reaches 20% at Diamond, versus 30% for the GRPO variant.


Grading Tiers
-------------

.. list-table::
   :header-rows: 1

   * - Tier
     - Criterion
   * - Bronze
     - Specification parses (SANY)
   * - Silver
     - No parser warnings
   * - Gold
     - Passes TLC model checker
   * - Diamond
     - Gold, plus TLC detects a violation when the correctness property is deliberately mutated

Diamond prevents the trivial-property failure mode: a specification whose correctness
property is always true passes TLC by vacuity and contributes nothing meaningful. The
mutation test catches this. Gold and Diamond coincide at every checkpoint in TLA-Prover,
indicating the model never falls back to trivial properties.


Relationship to Prior Work
--------------------------

This paper extends the findings of our evaluation study
:doc:`Can LLMs Write Correct TLA+ Specifications? </papers/llm-tla-evaluation>`,
which established the 8.6% semantic correctness baseline across 25 LLMs. TLA-Prover
demonstrates that targeted fine-tuning with verifiable reward signals can close much
of that gap.


In Plain Words
--------------

When people ask AI models to write TLA+ rules for a system, most of the answers fail. In the group's earlier study, the best public models wrote a file in the right form about 26.6% of the time, but only 8.6% of the answers passed the TLC model checker. In other words, the models know how TLA+ looks but not what it means.

TLA-Prover is a model built to do better. It has 20 billion parameters, which is a way of saying it is large. It is trained in two steps. First comes supervised fine-tuning, which is like studying a book of worked, checked examples. Second comes a practice stage called GRPO. Here the model writes several tries at the same task, and TLC checks each one. Answers that pass are rewarded. Answers that fail become repair exercises, so the model learns to fix its own mistakes. TLC itself acts as the judge, so no extra scoring model is needed.

The team also tried a second way to practice, called DPO, which learns from pairs of better and worse answers. Both ways start from the same first step, so the comparison is fair.

Passing TLC alone can be misleading. If a model writes a rule that is always true, TLC will happily pass it, and the rule says nothing useful. To catch this, the grading has four tiers: Bronze for a file that parses, Silver for no parser warnings, Gold for passing TLC, and Diamond for Gold plus a check that TLC complains when the rule is deliberately broken a little. A rule that never complains is empty, so it fails Diamond.

On a test of 30 held-out problems, TLA-Prover solved 9, or 30%, at both Gold and Diamond. That is about 3.5 times the 8.6% baseline. The DPO version reached 20% at Diamond. Gold and Diamond matched at every checkpoint, so the model did not seem to be cheating with empty rules. The test set is small, so these numbers are an encouraging first step and not a final answer.

Citation
--------

Eric Spencer, Arslan Bisharat, Brian Ortiz, Mujtaba Nazari, Khushboo Bhadauria,
TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, and Mohammed Abuhamad,
*TLA-Prover: Verifiable TLA+ Specification Synthesis via Preference-Optimized
Low-Rank Adaptation*, Proceedings of the 21st International Conference on Software
Technologies (ICSOFT 2026), pp. 627–636, 2026.
https://doi.org/10.5220/0015234600004088


BibTeX
------

.. code-block:: bibtex

   @inproceedings{spencer2026tlaprover,
     title     = {{TLA-Prover}: Verifiable {TLA+} Specification Synthesis via Preference-Optimized Low-Rank Adaptation},
     author    = {Spencer, Eric and Bisharat, Arslan and Ortiz, Brian and Nazari, Mujtaba and Bhadauria, Khushboo and Wang, TaiNing and Thiruvathukal, George K. and Läufer, Konstantin and Abuhamad, Mohammed},
     booktitle = {Proceedings of the 21st International Conference on Software Technologies (ICSOFT 2026)},
     pages     = {627--636},
     year      = {2026},
     address   = {Porto, Portugal},
     doi       = {10.5220/0015234600004088}
   }
