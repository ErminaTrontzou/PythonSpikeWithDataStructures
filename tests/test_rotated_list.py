#We should create some tests for every possible combination scenario
import pytest

from RotatedList.rotated_list import count_rotations_of_a_list

def test_a_list_of_5_with_2_rotations():
    # Given
    num_list = [3,4,0,1,2]
    # When
    rotations = count_rotations_of_a_list(num_list)
    # Then
    assert rotations == 2

def test_a_list_that_was_not_rotated():
    # Given
    num_list = [5,6,7,8]
    # When
    rotations = count_rotations_of_a_list(num_list)
    # Then
    assert rotations == 0

def test_a_list_that_was_rotated_once():
    # Given
    num_list = [8,2,3,4,5,6,7]
    # When
    rotations = count_rotations_of_a_list(num_list)
    # Then
    assert rotations == 1

def test_an_empty_list():
    # Given
    num_list = []
    # When
    rotations = count_rotations_of_a_list(num_list)
    # Then
    assert rotations == 0

def test_a_list_that_was_rotated_n_minus_one_times():
    # Given
    num_list = [4,5,6,7,8,3]
    # When
    rotations = count_rotations_of_a_list(num_list)
    # Then
    assert rotations == 5

def test_a_list_with_negative_numbers_with_positive():
    # Given
    num_list = [5,7,-3,-2]
    # When
    rotations = count_rotations_of_a_list(num_list)
    # Then
    assert rotations == 2

def test_a_list_with_only_negative_numbers():
    # Given
    num_list = [-5,-7,-6]
    # When
    rotations = count_rotations_of_a_list(num_list)
    # Then
    assert rotations == 1