import perspective as p
import pytest


def test_gen2d():
    assert p.gen2d(1,1)==[[0]]
    assert p.gen2d(-1,-1)==[]
    assert p.gen2d(2,3)==[[0,0],[0,0],[0,0]]
