=====
sites
=====

Yet another attempt to get my various sites under control.

The aim is for everything except `my blog`_ and `bethisad.talideon.com`_ to
go here, which have their own repos.

.. _my blog: https://github.com/kgaughan/blog
.. _bethisad.talideon.com: https://github.com/kgaughan/bethisad.talideon.com

Setup
=====

Ensure uv_ and just_ is installed, and run::

    just tools

To deploy a site, run::

    just deploy <site>

To do a local build of a site with mkdocs, run::

    just build <site>

.. _uv: https://docs.astral.sh/uv/
.. _just: https://just.systems/

.. vim:set ft=rst:
