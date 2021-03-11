
=========================================
Opinionated Product Developer Automation
=========================================

Tool for opinionated proudct development

------------
Installation
------------

On macOS, the easiest way to install pinkbelt is via `Homebrew  <https://brew.sh/>`_::

	$ brew install apiaryio/formulae/pinkbelt

On other platforms you can install pinkbelt with ``pip install pinkbelt`` providing you have Python and pip installed. Consult your platform for documentation on how to install Python and pip.

.. note::
   Python 3.6+ is default now and Python 2.7 will be deprecated.

-----
Setup
-----

With that, you should have ``bb`` command. Run interactive ``bb init`` and follow instructions. This is going to connect to services we are using in Apiary for further interaction:

* GitHub
* Trello
* Slack

Retrieved tokens and configuration is stored in ``~/.pinkbelt``. Format is now just dumped JSON, don't rely on it; it's probably going to change in the future.

If you are using ``bash``, you want to enable autocompletion. You can try it with::

        eval "$( _BB_COMPLETE=source bb)"

and if it's working properly, put it into your :file:`~/.bashrc`::

        echo '_BB_COMPLETE=source bb > /tmp/_black_belt_autocompletion.sh'  >> ~/.bashrc
        echo 'source /tmp/_black_belt_autocompletion.sh' >> ~/.bashrc


See `click's documentation <http://click.pocoo.org/3/bashcomplete/>`_ for more information.


-------
Upgrade
-------

If you used Homebrew on macOS, use::

	$ brew update
	$ brew upgrade

Otherwise::

	$ pip install -U pinkbelt

If you get error along the lines of::

	OSError: [Errno 1] Operation not permitted: '/tmp/pip-IYiPfC-uninstall/

you have a problem in your system installation (probably Mac OS X). You can either::

	sudo pip install -U --ignore-installed pinkbelt

or::

	pip uninstall pinkbelt
	pip install pinkbelt


---------
Structure
---------

`pb` has subcommands that stand for an area of expertise. View help or command reference on how to use those.

This documents focus more on intended workflow from the perspective of two roles (those may be the same person, of course): Developer and Story Owner.


.. toctree::
   :maxdepth: 2

   developer
   story-owner
   glossary



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

