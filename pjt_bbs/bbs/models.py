from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    target = models.IntegerField(default=1)
    target2 = models.IntegerField(default=1)

class hey(models.Model):
    target = models.IntegerField(default=1)
    target2 = models.IntegerField(default=3)
    target3 = models.PositiveIntegerField(default=5)

class Bbs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=20, blank=True, default='')
    pw = models.CharField(max_length=12, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ('created',)

class Post(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)