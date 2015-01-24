from django.db import models
from djanco.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):		#__unicode__ on Python 2
		return self.question_text
	def was_published_rec(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __unique__(self):		#__unicode__ on Python 2
		return self.choice_text
