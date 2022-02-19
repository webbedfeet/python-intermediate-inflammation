"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_zeros():
    """Test that the max function works for an array of zeros"""
    from inflammation.models import daily_max

    test_input = np.zeros((6,2))
    test_result = np.zeros(2)

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_floats():
    from inflammation.models import daily_max

    test_input = np.linspace(start = [0, 5],
                             stop = [1, 10],
                             num = 11,
                             endpoint=True)
    test_result = np.array([1,10])
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_min_zeros():
    """Test that the max function works for an array of zeros"""
    from inflammation.models import daily_min

    test_input = np.zeros((10,3))
    test_result = np.zeros(3)

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)

# @pytest.mark.parametrize(
#     "test, expected",
#     (np.meshgrid(np.linspace(0,1,5),np.linspace(0,1,5))[0], np.linspace(0,1,5)),
# )
# def test_daily_min(test, expected):
#     from inflammation.models import daily_max
#     npt.assert_array_equal(daily_max(test), expected)

# def test_daily_min_string():
#     """Test for TypeError when passing strings"""
#     from inflammation.models import daily_min
#
#     with pytest.raises(TypeError):
#         error_expected = daily_min([['Hello','there'], ['General','Kenobi']])

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

