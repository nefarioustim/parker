========================================
Parker
========================================

Parker is a Python-based web spider for collecting specific data
across a set of configured sites.

Non-Python requirements:

- Redis - for task queuing and visit tracking
- libxml - for HTML parsing of pages

Installation
----------------------------------------

Install using ``pip``::

    $ pip install parker

Configuration
----------------------------------------

To configure Parker, you will need to install the configuration
files in a suitable location for the user running Parker. To do
this, use the ``parker-config`` script. For example::

    $ parker-config ~/.parker

This will install the configuration in your homedir and will output
the related environment variable for you to set in your ``.bashrc``.
