#We should create some tests for every possible combination scenario
import pytest

#Tests for answer one
from CardSearch.card_search import locate_card_with_linear_search

#_card_to_find occurs in the middle
def test_locate_card_with_linear_search_with_card_to_find_at_the_middle():
    # Given.
    cards=[13, 11, 10, 7, 4, 3, 1, 0]
    card_to_find = 1
    # When.
    result = locate_card_with_linear_search(cards,card_to_find)
    # Then.
    assert result == 6

def test_locate_card_with_linear_search_with_card_to_find_at_the_beginning():
    # Given.
    cards=[4, 2, 1, -1]
    card_to_find = 4
    # When.
    result = locate_card_with_linear_search(cards,card_to_find)
    # Then.
    assert result == 0

def test_locate_card_with_linear_search_with_card_to_find_at_the_end():
    # Given.
    cards=[3, -1, -9, -127]
    card_to_find = -127
    # When.
    result = locate_card_with_linear_search(cards,card_to_find)
    # Then.
    assert result == 3

def test_locate_card_with_linear_search_with_only_one_card():
    # Given.
    cards=[6]
    card_to_find = 6
    # When.
    result = locate_card_with_linear_search(cards,card_to_find)
    # Then.
    assert result == 0

def test_locate_card_with_linear_search_with_card_to_find_not_contained_in_cards():
    # Given.
    cards=[9, 7, 5, 2, -9]
    card_to_find = 3
    # When.
    result = locate_card_with_linear_search(cards,card_to_find)
    # Then.
    assert result == -1

def test_locate_card_with_linear_search_with_cards_empty():
    # Given.
    cards=[]
    card_to_find = 7
    # When.
    result = locate_card_with_linear_search(cards,card_to_find)
    # Then.
    assert result == -1

def test_locate_card_with_linear_search_with_repeated_cards_but_only_one_card_to_find():
    # Given.
    cards=[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
    card_to_find = 3
    # When.
    result = locate_card_with_linear_search(cards,card_to_find)
    # Then.
    assert result == 7

def test_locate_card_with_linear_search_with_repeated_cards_with_desired_card_to_find():
    # Given.
    cards=[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
    card_to_find = 6
    # When.
    result = locate_card_with_linear_search(cards,card_to_find)
    # Then.
    assert result == 2
