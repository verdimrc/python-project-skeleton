"""Demonstrate unintended effect on pytest!!!

When there're multiple `sourcedir` under a single git root, there will be many
bad_modename.py scattered across src/smep0?/.

On pytest, depending on the tests sequence, test results may be unpredictable:
the bad_modname.py imported by the first test will be used throughout different
smep0? even though each smep0? intends to use its own version.

Solution: if the multiple `sourcedir` co-exist under the same git repo, then
there must no be conflicting package names across `sourcedir`, otherwise pytest
may give inconsistent results.
"""

friendly_name = "SageMaker EntryPoint 01"
