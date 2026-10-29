TLA+-Bench Leaderboard
======================

How well do language models write TLA+ specifications that actually run? This page
reports models on the gold specifications of :doc:`TLA+-Bench <../papers/tla-bench>`.
A model reads an English description of a system and writes a complete TLA+ module.
The module is then checked by the TLA+ tools themselves, not compared with a
reference answer.


Results
-------

.. leaderboard::


What Is Measured
----------------

The benchmark uses the 348 gold specifications of TLA+-Bench version 2. Each one is
model-checked with TLC in the folder it came from.

- **Gold A** (232 specifications) passes TLC in its upstream folder, reaches more than
  one state, draws no random values, checks a named property, and comes from an example
  folder. This is the main benchmark.
- **Gold B** (116 specifications) passes TLC the same way, but checks no named property
  or comes from a test folder.

Each specification has four English descriptions. Two are declarative: they name the
variables, actions and properties. Two state intent only: what the system must do,
without the specification's names. One of each pair was written by GPT-5 and the other
by Claude Opus 4.5.

A model is run with two prompts. The default prompt gives the description only. The
configuration-aware prompt adds the names the TLC configuration will look for.

For each generated module the grader records whether SANY parses it and whether TLC
checks it without error. A model's main result uses the default prompt, the declarative
GPT description, temperature 0 and one sample. The same setting is repeated five times
at temperature 0.8 to show how much results move from run to run.


Reproduce a Result
------------------

The tasks, prompts and runner are public in the
`tla_benchmark repository <https://github.com/LUC-AI4FM/tla_benchmark/tree/benchmark-v2-runs>`__:
``experiments/benchmark-v2/gold_tasks.jsonl`` lists the 348 specifications with their
descriptions, and ``experiments/rebuttal-20261007/run_generation.py`` builds the prompts
and saves each model's output for grading.
