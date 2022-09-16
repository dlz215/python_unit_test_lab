from unittest import TestCase
import functions_magic

class TestMagic8Ball(TestCase):

    def test_generate_url(self):
        test_url = 'https://8ball.delegator.com/magic/JSON/Will I get my degree?'
        self.assertEqual(test_url, functions_magic.generate_url_for_question('Will I get my degree?'))


    def test_extract_answer_from_response(self):
        example1 = {'magic': {'question': 'Will it be sunny tomorrow?', 'answer': 'Yes', 'type': 'Affirmative'}}
        self.assertEqual('Yes', functions_magic.extract_answer_from_response(example1))

        example2 = {'magic': {'question': 'Will I get my degree?', 'answer': 'Definitely not. Never ever EVER.', 'type': 'Negative'}}
        self.assertEqual('Definitely not. Never ever EVER.', functions_magic.extract_answer_from_response(example2))

    def test_extract_answer_from_response_different_structure(self):
        example1 = {'8ball': {'reply': 'Yes', 'type': 'Affirmative', 'question': 'Will it be sunny tomorrow?'}}
        self.assertEqual(None, functions_magic.extract_answer_from_response(example1))


""" TODO create a test case to test the following functions,

extract_answer_from_response

 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.

 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 


 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""
