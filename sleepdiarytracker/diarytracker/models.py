# -*- coding: utf-8 -,*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EveningDiary(models.Model):
	"""Define and Create An Evening Diary table in the database"""
	date = models.Datefield()

		