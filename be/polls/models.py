import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    queston_text = models.CharField(max_length=200)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.queston_text

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
