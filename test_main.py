import unittest
from main_project import *


class tddTests(unittest.TestCase):

    def test_sort_str_list1(self):
        # given: an list of numbers as strings, i/e/. ["1", "5", "15", "9", "4"]
        # Task: sort the numbers
        # Restriction: the numbers must stay strings - no converting to integers
        # Rule: None values should be removed from list
        # Rule: empty strings should be treated as zero
        # Rule: should be able to handle null lists
        # Rule: 
        # result: return an array of string numbers lowest to highest: "1", "4", "5", "9"

        # expected: ["1", "4", "5", "9", "15"]

        # given
        given = ["1", "5", "15", "9", "4"]
        expected = ["1", "4", "5", "9", "15"]

        # when
        actual = sort_str_list(given)

        # then
        self.assertListEqual(expected, actual)

    def test_sort_str_list_with_one_element(self):
        # given
        given = ["5"]
        expected = ["5"]

        # when
        actual = sort_str_list(given)

        # then
        self.assertListEqual(expected, actual)

    ####### edge cases

    def test_sort_str_list_with_negative(self):
        # given
        given = ["1", "5", "15", "9", "4", "-2"]
        expected = ["-2", "1", "4", "5", "9", "15"]

        # when
        actual = sort_str_list(given)

        # then
        self.assertListEqual(expected, actual)

    def test_sort_str_list_with_empty_string(self):

        given = ["1", "5", "15", "9", "4", ""]
        expected = ["", "1", "4", "5", "9", "15"]

        # when
        actual = sort_str_list(given)

        # then
        self.assertListEqual(expected, actual)


    def test_sort_str_list_with_none(self):
        given = ["1", "5", "15", "9", "4", None]
        expected = ["1", "4", "5", "9", "15"]

        # when
        actual = sort_str_list(given)

        # then
        self.assertListEqual(expected, actual)


######## sub method tests

    def test_current_is_less_than_previous_true(self):
        # given
        given = ("1", "5")
        expected = True

        # when
        actual = current_is_less_than_previous(*given)

        # then
        self.assertEquals(expected, actual)


    def test_current_is_less_than_previous_false(self):
        # given
        given = ("5", "1")
        expected = False

        # when
        actual = current_is_less_than_previous(*given)

        # then
        self.assertEquals(expected, actual)


    def test_current_is_less_than_previous_equal(self):
        # given
        given = ("5", "5")
        expected = False

        # when
        actual = current_is_less_than_previous(*given)

        # then
        self.assertEquals(expected, actual)

    def test_current_is_less_than_previous_decimal(self):
        # given
        given = ["5.15", "99"]
        expected = ["99", "5.15"]

        # when
        actual = current_is_less_than_previous(*given)

        # then
        self.assertEquals(expected, actual)

    def test_current_is_less_than_previous_characters(self):
        # given
        given = ["5.15", "a"]
        expected = ["5.15"]

        # when
        actual = current_is_less_than_previous(*given)

        # then
        self.assertEquals(expected, actual)

    def test_current_is_less_than_previous_leading_zeros(self):
        # given
        given = ["5.15", "a"]
        expected = ["99", "5.15"]

        # when
        actual = current_is_less_than_previous(*given)

        # then
        self.assertEquals(expected, actual)







# def test_sort_str_list2(self):
#     # given: an list of numbers as strings, i/e/. ["1", "5", "15", "9", "4"]
#     # Task: sort the numbers
#     # Restriction: the numbers must stay strings - no converting to integers
#
#     # result: return an array of string numbers lowest to highest: "1", "4", "5", "9"
#
#     # expected: ["1", "4", "5", "9", "15"]
#
#     # given
#     given = ["1", "5", "15", "9", "4", "-2"]
#     expected = ["-2", "1", "4", "5", "9", "15"]
#
#     # when
#     actual = sort_str_list(given)
#
#     # then
#     self.assertListEqual(expected, actual)
