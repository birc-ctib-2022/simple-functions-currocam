# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from unittest.mock import patch

import pytest
from funcs import (
    prod,
    prod2,
    longest,
    dist
)

    
def test_prod():
    assert prod(1, 2, 3) == 6

a = 5
@patch('funcs.a', a)
def test_prod2():
    assert prod2(2) == 50


def test_longest():
    assert longest([1, 2, 3], [4, 5]) == [1, 2, 3]


def test_dist():
    assert dist((1, 2), (3, 4)) == pytest.approx(2.828427)