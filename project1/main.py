from project1.demographic_data_analyzer import calculate_demographic_data
import unittest
import project1.test_module as test_module

calculate_demographic_data()

unittest.main(module='test_module', exit=False)