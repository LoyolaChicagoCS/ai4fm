I don't know about you, but every time that I check out a static site
generator's example GitHub page, I'm both over and underwhelmed at the
same time. On one hand, the Github page often has great technical
details and depth to allow me to leverage and extend the example to fit
my needs. On the other hand, feature's such as GitHub Action
integration, or deploying to GitHub pages is often left to the engineer
to figure out. And in some cases, the example site is not longer in line
with current revisions of the tool!

And look, I know that every project is different, and that your
preferred static site generator probably has better documentation and
examples than what I've seen. But of the projects that I have seen,
GitHub pages deployment or recommended project repository layouts are
sidelined to focus on technical documentation.

Is this good or bad? I don't know. Am I too unexperienced to work within
these constraints? Maybe. But I can't be the only engineer to have faced
these issues. And for projects aimed at quickly and rapidly creating
websites from limited format text documents (e.g., Markup, ReStructured
Text), I'd think that features such as starter or template GitHub
repositories would be more common.

Because of my frustrations, I've released two example GitHub
repositories for two popular static site generators: `MkDocs
<https://www.mkdocs.org/>`__ and `Sphinx
<https://www.sphinx-doc.org/en/master/index.html>`__. The goal with
these repositories is to be focussed on a minimal project using the
static site generator, that builds into a Read The Docs theme compatible
website, and provide supporting tooling regarding formatting of the
underlying formatting language. It also provides the tooling needed to
deploy to GitHub Pages both from the command line and via GitHub Actions
(both are powered by the ```ghp-import``
<https://pypi.org/project/ghp-import/>`__ project).

Now I understand that my examples are not going to be complete to
everyone. So I'd like to open my issue boards to the community to
suggest how to better improve these examples. I think it's a real shame
that better examples of minimal static sites don't exist, and I think
projects like mine address low hanging fruit on their issue boards.

MkDocs example site: https://github.com/NicholasSynovic/example_mkdocs

Sphinx example site: https://github.com/NicholasSynovic/example_sphinx
