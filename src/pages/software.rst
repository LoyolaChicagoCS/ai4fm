Software and Datasets
=====================

AI4FM develops its research artifacts in the open. Everything below lives under the
`LUC-AI4FM GitHub organization <https://github.com/LUC-AI4FM>`__, where our datasets,
model-training code, and evaluation harnesses are available for reuse and replication.

.. note::
   This page lists our publicly released repositories. Work that is still under
   submission or embargo is released once the associated paper is public.


Models and Fine-Tuning
----------------------

.. grid:: 1
   :gutter: 3

   .. grid-item-card::
      :margin: 0

      :octicon:`cpu;1em;sd-text-primary` **TLA-Prove (ChatTLA)**

      The training and evaluation code behind :doc:`TLA-Prover <../papers/tla-prover>`,
      accepted at ICSOFT 2026. The distinguishing choice is the training metric: success
      is measured by whether a generated specification passes the TLC model checker, not
      by perplexity. The resulting 20B model is derived from ``openai/gpt-oss-20b`` and
      released under Apache 2.0.

      `Repository <https://github.com/LUC-AI4FM/TLA-Prove>`__ |
      `Model on Hugging Face <https://huggingface.co/EricSpencer00/chattla-20b>`__

   .. grid-item-card::
      :margin: 0

      :octicon:`sync;1em;sd-text-primary` **ralph-tla**

      Experiments pairing the Ralph specification language with TLA+ in a self-correcting
      loop: the model drafts a specification, SANY and TLC check it, and the resulting
      errors are fed back to the model until the specification passes. A test of whether
      verifier feedback can substitute for human repair.

      `Repository <https://github.com/LUC-AI4FM/ralph-tla>`__


Datasets and Pipelines
----------------------

.. grid:: 1
   :gutter: 3

   .. grid-item-card::
      :margin: 0

      :octicon:`database;1em;sd-text-primary` **tla-dataset-pipeline**

      A pipeline that discovers TLA+ repositories across GitHub, extracts ``.tla``,
      ``.cfg``, and ``.tlaps`` files, parses them with LLM-based analysis, and archives
      the results to S3. Discovery runs nightly under CI with DVC-tracked state, so the
      corpus grows continuously rather than being frozen at collection time.

      `Repository <https://github.com/LUC-AI4FM/tla-dataset-pipeline>`__

   .. grid-item-card::
      :margin: 0

      :octicon:`checklist;1em;sd-text-primary` **tla_benchmark**

      The evaluation harness behind our LLM benchmarking work. Extracts real
      SANY-parsed ASTs, runs specifications through ``tla2tools``, and scores them on
      syntactic and semantic correctness alongside code-quality metrics. Includes a
      dashboard for reviewing runs.

      `Repository <https://github.com/LUC-AI4FM/tla_benchmark>`__


Generation Pipelines
--------------------

.. grid:: 1
   :gutter: 3

   .. grid-item-card::
      :margin: 0

      :octicon:`beaker;1em;sd-text-primary` **FormaLLM**

      A research pipeline for generating TLA+ specifications from natural language,
      orchestrated with ZenML and backed by OpenAI, Anthropic, or local Ollama models.
      Separates prompting, parsing, and evaluation into swappable pipeline steps so that
      backends and prompting strategies can be compared under identical conditions.

      `Repository <https://github.com/LUC-AI4FM/FormaLLM>`__

   .. grid-item-card::
      :margin: 0

      :octicon:`arrow-switch;1em;sd-text-primary` **FormaLLM-Reverse**

      The companion to FormaLLM, exploring the opposite direction: recovering readable
      natural-language documentation from existing formal models.

      `Repository <https://github.com/LUC-AI4FM/FormaLLM-Reverse>`__

   .. grid-item-card::
      :margin: 0

      :octicon:`file;1em;sd-text-primary` **paper-parse**

      Tooling for extracting structured data from research PDFs at scale, used to build
      the comment-ratio dataset supporting our empirical software engineering work.

      `Repository <https://github.com/LUC-AI4FM/paper-parse>`__


Contributing
------------

Our repositories are open to students and collaborators. If you are interested in
working on any of these projects, see :doc:`Get Involved <prospective-students>`.
