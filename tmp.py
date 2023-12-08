# def concat(a, b):
#     return f"{a}, {b}"
#
#
# def sum_numbers(a: int, b: int, c: int) -> int:
#     return sum((a, b, c))
#
#
# def test_concat():
#     assert concat(1, 2) != "1, 3"
#     assert concat('a', 'b') == "a, b"
#
#
# def test_sum_numbers():
#     assert sum_numbers(1, 5, 8) == 14
#     assert isinstance(sum_numbers(1, 2, 3), int)
#
#
# functions = [test_concat, test_sum_numbers]
#
#
# if __name__ == '__main__':
#     for function in functions:
#         try:
#             function()
#             print(f"{function.__name__} SUCCESS")
#         except Exception as error:
#             print(f"{function.__name__} FAILED -> {error}")


# import unittest
# import datetime
# import sqlite3
#
#
# class UserTestCase(unittest.TestCase):
#     def setUp(self) -> None:
#         print("setUp")
#         self.current_time = datetime.datetime.now()
#         self.connection = sqlite3.Connection()
#
#     def tearDown(self) -> None:
#         print("tearDown")
#         self.connection.close()
#
#     def test_example_1(self):
#         print("example_1")
#         print(self.current_time)
#
#     def test_example_2(self):
#         print("example_2")
#         print(self.current_time)


# class UserTest(unittest.TestCase):
#
#     def test_example_3(self):
#         self.assertEqual(20, 20)
#         self.assertAlmostEqual(0.011, 0.01, 2, "Ok")
#         self.assertGreater(20, 10)
#         self.assertGreaterEqual(20, 20)
#         self.assertIsInstance(10, int)
#
#         # with self.assertRaises(AssertionError):
#         #     raise AssertionError
#
#         self.assertRegex("test test", r'^test')

