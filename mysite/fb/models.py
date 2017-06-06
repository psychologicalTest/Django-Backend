
from django.db import models
from django.utils import timezone
#### Create your models here.

class Main_question(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    apply_num = models.IntegerField(null=True)
    classification = models.TextField(null=True)
    subtitle = models.TextField(null=True)
    main_quest = models.TextField(null=True)



class Sub_question(models.Model):
    main_question_id= models.IntegerField()
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    main_quest = models.TextField(null=True)



class Option(models.Model):
    sub_question_id= models.IntegerField()
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    option = models.TextField(null=True)
    score = models.IntegerField(null=True)



class Answer(models.Model):
    main_question_id= models.IntegerField()
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    answer = models.TextField(null=True)
    score_range = models.IntegerField(null=True)
