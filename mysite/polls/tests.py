from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_question = Question(pub_date=timezone.now()+datetime.timedelta(days=30))
        self.assertIs(future_question.was_published_recently(), False)
    
    # should return false
    def test_was_published_recently_with_past_questions(self):
        past_question = Question(pub_date=timezone.now()-datetime.timedelta(days=2))
        self.assertIs(past_question.was_published_recently(),False)
    
    def test_was_published_recently_with_recent_questions(self):
        recent_question = Question(pub_date=timezone.now())
        self.assertIs(recent_question.was_published_recently(),True)
        