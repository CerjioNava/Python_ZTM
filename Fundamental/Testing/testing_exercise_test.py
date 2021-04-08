#testing_exercise_test

import unittest
import testing_exercise

class TestGame(unittest.TestCase):

	def test_input(self):
		answer = 5
		guess = 5
		result = testing_exercise.guessing(guess, answer)
		self.assertTrue(result)

	def test_input_wrong_guess(self):
		result = testing_exercise.guessing(1, 3)
		self.assertFalse(result)

	def test_input_wrong_number(self):
		result = testing_exercise.guessing(11, 4)
		self.assertFalse(result)

	def test_input_wrong_type(self):
		result = testing_exercise.guessing(5, '5')
		self.assertFalse(result)


if __name__ == '__main__':
	unittest.main()