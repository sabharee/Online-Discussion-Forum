from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=50)
class Discussions(models.Model):
    post_text = models.CharField(max_length=500)
    post_id = models.ForeignKey(Topic)
