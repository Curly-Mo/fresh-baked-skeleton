"""
test_fresh_baked_skeleton
----------------------------------
Tests for `fresh_baked_skeleton` module.
"""


# Fresh Baked Skeleton
from fresh_baked_skeleton import fresh_baked_skeleton


def test_fresh_baked_skeleton():
    assert fresh_baked_skeleton.main() == "hello"
