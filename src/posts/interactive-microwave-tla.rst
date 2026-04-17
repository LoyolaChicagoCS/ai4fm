:blogpost: true
:date: April 17, 2026
:author: Eric Spencer
:category: Research Update
:tags: Formal Methods, TLA+, Stuttering
:nocomments:

Interactive Microwave: TLA+ in the Browser
==========================================

We published a browser-native version of the
`interactive-microwave-tla <https://github.com/EricSpencer00/interactive-microwave-tla>`_
simulator. It mimics a Java microwave runtime and a small TLA+ model checker
that is a literal transcription of the project's ``Microwave.tla`` spec, so
users can experiment with the state machine and see every safety obligation
enforced — without installing Java, Maven, or TLC.

The stuttering fix
------------------

The TLA+ spec of the microwave is

.. code-block:: text

   Spec == Init /\ [][Next]_<<door, time, radiation, power>>

The ``[Next]_vars`` square-bracket form admits two kinds of step at every
position in a behavior: a real ``Next`` disjunct *or* a stuttering step where
``vars' = vars``. The earlier web demo never emitted a stutter step — every
logged trace row corresponded to a real action — so behaviors rendered as a
sequence of discrete transitions rather than the action/stutter alternation the
spec actually defines.

The new build fixes this presentation error. A dedicated ``Stutter``
pseudo-action (always enabled, ``step(v) = v``) realizes ``[Next]_vars`` as a
concrete successor list, and the simulation engine emits a stutter row on
every wall-clock tick where no user action fires. A vitest suite verifies that
``Safe`` is closed under stuttering (``Safe(v) ⇔ Safe(Stutter(v))``) and that
``[Next]_vars`` is never empty — behaviors cannot deadlock in the TLA+ sense
because stuttering is always available.

Try it
------

.. raw:: html

   <div id="microwave-root" style="min-height: 560px;"></div>
   <link rel="stylesheet" href="../_static/demos/microwave/assets/index.css" />
   <script type="module" src="../_static/demos/microwave/assets/index.js"></script>

Source and details
------------------

Source, design spec, and implementation plan live in the project repository:

- `Repository <https://github.com/EricSpencer00/interactive-microwave-tla>`_
- `Design spec <https://github.com/EricSpencer00/interactive-microwave-tla/blob/main/docs/superpowers/specs/2026-04-17-web-port-design.md>`_
- `Browser port (web/) <https://github.com/EricSpencer00/interactive-microwave-tla/tree/main/web>`_
