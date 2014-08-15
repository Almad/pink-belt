
============
Developer
============

:term:`Developer` processes :term:`Work Card`s, develops them and deploys them to production.

Those live on the :term:`Work Board`.

Those are the task :term:`Developer` may want to perform. 

------------------------------------
Code review
------------------------------------

Code review ensures the quality of the code and disperses the knowledge about the code and features through the team.

Merging Pull Request
^^^^^^^^^^^^^^^^^^^^^

	bb gh merge https://github.com/apiaryio/apiary/pull/1234

This:

# Inspects the current repository and the pull request
# Switches to master and brings it up to date
# Merges the PR locally and pushes to master
# Deletes the merged branch from the remote repository/github
