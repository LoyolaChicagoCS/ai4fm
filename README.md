# AI4FM Website

> Source for [ai4fm.cs.luc.edu](https://ai4fm.cs.luc.edu) — the AI for Formal Methods research group at Loyola University Chicago.

[![Visit ai4fm.cs.luc.edu](https://img.shields.io/badge/Website-ai4fm.cs.luc.edu-darkred?style=for-the-badge)](https://ai4fm.cs.luc.edu)

## Table of Contents

- [AI4FM Website](#ai4fm-website)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Getting Started](#getting-started)
    - [Requirements](#requirements)
    - [Creating The Dev Environment](#creating-the-dev-environment)
    - [Building The Sphinx Site](#building-the-sphinx-site)
    - [Serving The Sphinx Site](#serving-the-sphinx-site)
  - [Hosting On GitHub Pages](#hosting-on-github-pages)

## About

This is a template repository that is intended to be inherited by other template
repositories *to ensure consistent common tool deployment Sphinx projects*.

Additionally, while projects can leverage this template or its content,
extending this template is encouraged.

## Getting Started

### Requirements

This template is dependent upon Python 3.13 and `uv`.

It is recommended to install `pre-commit` as well for per-commit formatting and
linting checks.

### Creating The Dev Environment

`make create-dev`

### Building The Sphinx Site

`make build_project`

### Serving The Sphinx Site

`make serve`

## Hosting On GitHub Pages

Any time that a commit is pushed to GitHub from the `main` branch, the
[`build.yml`](.github/workflows/build.yml) workflow is executed which builds the
project and deploys it to GitHub Pages.

You will need to modify the ReStructured Text directory in the
[`build.yml`](.github/workflows/build.yml) from `template_sphinx` to the name of
your project's directory. You can find the line to modify by searching for
`# TODO` in the [`build.yml`](.github/workflows/build.yml) file. An example of
what to look for is this code block:

```yaml
- name: Build the site
  run: |
    ./.venv/bin/sphinx-build --write-all template_sphinx build
    # TODO: Change `template_sphinx` to the source directory
```

You can also deploy the project from the `main` branch at any time (so long as
the `workflow_dispatch` event is included in the
[`build.yml`](.github/workflows/build.yml) file) from the GitHub Actions page

