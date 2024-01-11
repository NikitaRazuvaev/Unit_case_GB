import pytest
from list_comparer import ListComparer

def test_compare_lists():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    comparer = ListComparer(list1, list2)
    assert comparer.compare_lists() == "Второй список имеет большее среднее значение"

def test_compare_lists_equal():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    comparer = ListComparer(list1, list2)
    assert comparer.compare_lists() == "Средние значения равны"

def test_compare_lists_empty():
    list1 = []
    list2 = [1, 2, 3, 4, 5]
    comparer = ListComparer(list1, list2)
    assert comparer.compare_lists() == "Первый список имеет большее среднее значение"