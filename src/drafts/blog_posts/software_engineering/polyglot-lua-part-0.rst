I've been interested in expanding my toolkit of programming languages
for some time now. I would currently say that I am proficient in Java,
C, and C++ and have expertise in Python. But this clearly isn't the full
range of programming languages or experiences out there. For example, I
have very little knowledge of functional or embedded languages.

To encourage me to write more posts, I'm going to start documenting my
experience learning different programming languages and the projects
that I write with them. To start this series, I will begin with the Lua
scripting language.

##############
 What Is Lua?
##############

Lua is an `"efficient, lightweight, embeddable scripting language"
<https://www.lua.org/about.html>`__ in active development since 1993. It
claims to be fast, but most importantly the interpreter is very small at
only a few 552Kb for the latest (5.4.7) binary.

Personally, this doesn't matter a whole lot to me. Binary size and speed
mean less than if I can glean a new technique or experience from using
the language. But I also don't want to waste time learning a dead
language either. So every language that I learn needs to meet the
following criteria:

-  Must have a package manager,
-  Must be able to test code,
-  Must have development tooling (e.g. LSP support, code formatting,
   linting) and,
-  (Optional) Must support static typing

Lua supports most of this primarily through community packages.
```luarocks`` <https://luarocks.org/>`__ is the Lua package manager. Lua
does not ship with a unit testing framework by default, but the
community seems to have selected ```luaunit``
<https://luarocks.org/modules/bluebird75/luaunit>`__ as the defacto
testing library. LSP and linting support is provided through the
```lua-language-server`` <https://luals.github.io/>`__ and code
formatting is handled through ```stylua``
<https://github.com/JohnnyMorganz/StyLua>`__. However, I can't find
tooling similar to Python's ```bandit``
<https://github.com/PyCQA/bandit>`__ to perform security audits. I
believe this to be an open area of Lua library development.

Lua does not support static typing. But, given the minimal keywords and
language features of Lua, the community has come up with different
interpreters and programming languages that generate Lua code that
implement static typing. ```typedlua``
<https://github.com/andremm/typedlua>`__ seemed promising, as it
promised to implement a type system on top of Lua (like TypeScript), but
hasn't received a commit in 5 years. ```ravi``
<https://github.com/dibyendumajumdar/ravi>`__ also seemed promising, but
leverages a modified Lua VM which breaks compatibility with some Lua
libraries. I would prefer the TypeScript-like approach to implementing
static types to not break compatibility with existing libraries.

##############
 Learning Lua
##############

… Will have to wait for the next post. This post took me longer than
expected to compile all of my sources. As a sneak peak, I intend to
release a GitHub Lua template following my `other templates
<https://github.com/NicholasSynovic?tab=repositories&q=template&type=&language=&sort=>`__
and another repo that is focussed on solving code kata from `Rosetta
Code <https://rosettacode.org/wiki/Rosetta_Code>`__.
