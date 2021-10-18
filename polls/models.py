from django.db import models
from django.utils import timezone
import datetime

STATUS_CHOICES =[
    ('1', 'Draft'),
    ('2', 'Published'),
    ('0', 'Withdrawn'),
]

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return self.question_text

    # 是否在当前（一天内）发布的问卷
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text