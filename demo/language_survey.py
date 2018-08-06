import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):


    def test_store_single_response(self):
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.response)

    def setUp(self):
        question = 'Whats language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.response = ['English', 'Spanish', 'Mandarin']
        

unittest.main()


