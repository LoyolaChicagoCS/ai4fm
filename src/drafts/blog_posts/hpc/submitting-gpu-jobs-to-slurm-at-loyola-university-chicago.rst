Slurm logo taken from [0]

#########
 Context
#########

The Computer Science department at Loyola University Chicago [1]
utilizes a high-performance computing cluster to support both research
and teaching initiatives with particular interest in running HPC and AI
applications with efficiency and effectiveness. As our department's
needs have grown and changed over time, it has become clear that we
require a more structured approach to allocating computational resources
to individual projects. Our current method of running scripts as
background processes thereby leveraging shared resources across all
users, has limitations and does not scale effectively for ongoing
projects. Specifically, our reliance on shared resources often results
in computational bottlenecks due to multiple concurrent jobs competing
for limited system resources.

To effectively manage the execution of jobs, resource allocation, and
job order within our department, we are exploring the use of a job
scheduler [2] as a solution. Specifically, Slurm [3] is currently under
consideration due to its ability to meet our computational needs.
However, given that not all members of the department have experience
with job scheduling, and no formal training process currently exists,
this blog post aims to serve as a brief, informal introduction to the
technology and its applications, providing a foundation for readers to
pursue further research into the applications of job schedulers and
their benefits.

################
 What is Slurm?
################

Slurm is an open-source job scheduler software package that enables
efficient management of workload execution on shared computing
resources, such as cluster computers [3]. A job scheduler like Slurm
manages the order in which programs or applications (referred to as
"jobs") are executed on these resources. By queuing jobs and allocating
access to computational resources on a managed basis (e.g.,
first-in-first-out, last-in-last-out, or when specific hardware becomes
available), Slurm ensures that each job has exclusive access to the
required resources, preventing conflicts between multiple concurrent
processes.

More information about Slurm can be found here [3]. The user guide and
documentation for Slurm can be found here [4]. Slurm's source code is
available on GitHub here [5].

#########
 Problem
#########

Our department aims to integrate AI methods into our research and
teaching programs, with a current focus on batch inferencing, training,
and fine-tuning large language models (LLMs). To achieve this, we
require access to significant GPU resources. However, our current setup
limits individual users from fully utilizing the available GPUs for
these computationally intensive tasks, as multiple users are often
competing for simultaneous access to the same or related resources.

Our cluster computer has the necessary hardware and software
infrastructure to execute AI and HPC codes efficiently. However, due to
shared resource allocation among multiple users, these codes often take
longer than expected to complete. In some cases, they may even stall or
be terminated by the system, as it prioritizes freeing resources for
other users over allowing a single task to run for an extended period.

##########
 Solution
##########

With Slurm, we can utilize a set of fully available computational
resources to schedule jobs efficiently. Users can configure their jobs
to take advantage of specific resources and allocate a specified number
of each resource as needed. Additionally, if a job does not require
exclusive access to system capabilities, Slurm enables parallel
execution by running multiple jobs simultaneously on separate hardware
units.

The rest of this post is a tutorial that provides a step-by-step guide
on how to submit jobs to Slurm. We'll use a real-world example -
training a simple Convolutional Neural Network model on the MNIST
dataset using TensorFlow [6] and Keras [7] in Python.

While our focus is on using Slurm, it's essential to write your code
with concurrency and parallelism in mind. This means designing your
program to take advantage of multiple computational resources
simultaneously. If your code isn't optimized for concurrent execution,
scaling its performance will be challenging. We assume prior knowledge
of writing high-performance computing (HPC) codes and focus on using
Slurm to manage and execute them efficiently.

**NOTE**: The code utilized in this tutorial is not optimized for
running on multiple GPUs by default and will not scale with additional
resources. To scale the code, you'll need to extend the code to support
a multi-GPU, distributed training strategy as outlined in [8].

**********
 Tutorial
**********

   This tutorial will guide you through submitting jobs to Slurm in a
   series of easy-to-follow steps. Important notes and considerations
   will be highlighted in block quotes.

-  Connect to the cluster computer.
-  Clone your code from GitHub to a directory on the cluster computer.

..

   You are using ``git`` and GitHub to keep track of versions, right?

-  Configure, build, and test your software.

..

   Here is where the tutorial will begin, I will be using this code
   provided by the Tensorflow team for training CNN model on the MNIST
   dataset [9].

-  Create a ``bash`` script called ``job.bash``

``touch job.bash``

   You can name this file whatever you want, but it will have to be a
   ``bash`` script

-  Add the following code to ``job.bash``:

.. code:: shell

   #!/bin/bash

   #SBATCH --gres=gpu:1

   module load python/3.10

   srun python train.py

..

   Here's what the code is doing line-by-line:

   #. ``#!/bin/bash``: shebang to inform the operating system what
      interpreter to use

   #. ``#SBATCH --gres=gpu:1``: This defines an ``sbatch`` directive to
      set Slurm to use a general resource (``--gres``) of a single GPU
      (``gpu:1``). If multiple GPUs are required, you would replace 1
      with the number of GPUs needed.

   #. ``module load python/3.10``: Configure the user environment to use
      ``python3.10``.

   #. ``srun python train.py``: Submit the job (``python``) to the Slurm
      queue with its arguments (``train.py``) and configure the job with
      the aforementioned directives (see 2).

-  Run ``sbatch job.bash`` to queue the job.
-  Run ``squeue`` to see the queued Slurm jobs.
-  Wait for the job to execute. A ``slurm-$(JOB_NUMBER).out`` file will
   be created with any standard output or error piped into it.

############
 Conclusion
############

And that's it! You now have a basic understanding of how to use Slurm
for running GPU-related jobs. For a comprehensive guide on directives,
configuration options, and more advanced usage, please refer to the
official Slurm documentation here [10 - 12].

############
 References
############

[0] https://slurm.schedmd.com/slurm_logo.png [1] https://www.luc.edu/cs/
[2] https://en.wikipedia.org/wiki/Job_scheduler [3]
https://www.schedmd.com/slurm [4]
https://slurm.schedmd.com/documentation.html [5]
https://github.com/SchedMD/slurm [6] https://www.tensorflow.org/ [7]
https://keras.io/ [8]
https://www.tensorflow.org/guide/distributed_training [9]
https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py
[10] https://slurm.schedmd.com/sbatch.html [11]
https://slurm.schedmd.com/srun.html [12]
https://slurm.schedmd.com/squeue.html
