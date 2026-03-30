#############################################
 Formal Methods in the Field
#############################################

Welcome to **FMitF** - the Formal Methods in the Field research group at
`Loyola University Chicago <https://luc.edu>`__, part of the
`Department of Computer Science <https://luc.edu/cs>`__.
We advance formal methods, rigorous system design, and reproducible tools at the
intersection of logic, mathematics, AI, and real-world computing.

Featured Research
-----------------

.. grid:: 1
   :gutter: 2

   .. grid-item-card::
      :margin: 0

      :octicon:`beaker;1em;sd-text-primary` **Can LLMs Write Correct TLA+ Specifications?**

      *Evaluating Natural-Language-to-TLA+ Generation* - Under Submission

      The first systematic evaluation of LLM-based TLA+ specification synthesis from
      natural language. We evaluate 30 LLMs across eight families on a curated dataset of
      205 TLA+ specifications, validated by both the SANY parser and TLC model checker.
      LLMs achieve up to 26.6% syntactic correctness but only 8.6% semantic correctness.
      Results show model size does not predict quality and code-specialized models
      consistently underperform on formal languages.

      .. button-link:: papers/llm-tla-evaluation.html
         :color: primary

         Read More

      .. button-link:: posts/llm-tla-evaluation-2025.html
         :color: secondary

         Research Update


Research Areas
--------------

.. grid:: 2
   :gutter: 2

   .. grid-item-card::
      :margin: 0

      :octicon:`beaker;1em;sd-text-primary` **Formal Specification and Verification**

      Building datasets, tooling, and infrastructure around **TLA+** and other formal
      specification languages. Making model checking accessible through open pipelines
      and notebook-based workflows.

   .. grid-item-card::
      :margin: 0

      :octicon:`cpu;1em;sd-text-primary` **LLMs for Formal Methods**

      Evaluating whether large language models can generate semantically correct formal
      specifications. Identifying where LLMs fail on rigorous specification tasks and why.

   .. grid-item-card::
      :margin: 0

      :octicon:`graph;1em;sd-text-primary` **Empirical Software Engineering**

      Studying software artifacts at scale: pre-trained model naming conventions,
      supply chain security, and development practices in real-world open-source systems.

   .. grid-item-card::
      :margin: 0

      :octicon:`shield;1em;sd-text-primary` **Security and Systems**

      IoT security research including signal injection attacks on pairing protocols,
      plus HPC education tools and agentic tutoring systems for parallel computing.


Meet the Team
-------------

.. grid:: 4
   :gutter: 2

   .. grid-item-card::
      :margin: 0
      :text-align: center
      :img-top: _static/images/people/laufer.jpg

      **Konstantin Laufer**

      Professor

      Programming Languages, Formal Methods

      `Website <https://laufer.cs.luc.edu/>`__

   .. grid-item-card::
      :margin: 0
      :text-align: center
      :img-top: _static/images/people/abuhamad.jpg

      **Mohammed Abuhamad**

      Assistant Professor

      Security, AI/ML, IoT

      `Website <https://abuhamad.cs.luc.edu/>`__

   .. grid-item-card::
      :margin: 0
      :text-align: center
      :img-top: _static/images/people/thiruvathukal.png

      **George K. Thiruvathukal**

      Professor and Chair

      HPC, Software Engineering, AI

      `Website <https://gkt.sh/>`__

   .. grid-item-card::
      :margin: 0
      :text-align: center
      :img-top: _static/images/people/wang.jpg

      **TaiNing Wang**

      Assistant Professor

      Databases, Formal Methods, AI/ML

      `Website <https://taining.github.io/>`__


.. grid:: 1
   :gutter: 2

   .. grid-item-card::
      :margin: 3 0 0 0
      :text-align: center

      :octicon:`file;1em` **Research Papers**

      .. button-link:: papers/index.html
         :color: primary
         :expand:

         Browse Papers


***************************
 Research Updates
***************************

.. postlist:: 5
   :category: Blog Post
   :date: %A, %B %d, %Y
   :format: {date}: {title}
   :excerpts:
   :expand: Read more ...

..
   Toctrees for the side bars

.. toctree::
   :glob:
   :hidden:
   :maxdepth: 2
   :caption: Pages

   Pages <pages/index>
   pages/*

.. toctree::
   :glob:
   :hidden:
   :maxdepth: 2
   :caption: Research Papers

   All Papers <papers/index>
   papers/*

.. toctree::
   :glob:
   :hidden:
   :maxdepth: 2
   :caption: Research Updates

   All Posts <posts/index>
   posts/*
