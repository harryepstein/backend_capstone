# -*- coding: utf-8 -,*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SleepData(models.Model):
	"""Define and Create A Sleep Datajkl table in the database"""
	date = models.DateField()
	bedtime = models.TimeField()
	exit_bed_time = models.TimeField()
	ease_of_sleep = models.Choices()
	times_awoken = models.IntegerField()
	minutes_awake = models.IntegerField()
	total_sleep_time = models.IntegerField()
	factors_disturbing_sleep = models.TextField()
	subjective_waking_mood_rating = models.Choices()
	notes = model.TextField()
	#Evening Diary
	caffeine_consumption_morning = models.BooleanField()
	caffeine_consumption_evening = models.BooleanField()
	caffeine_consumption_afternoon = models.BooleanField()
	exercised_morning = models.BooleanField()
	exercised_afternoo = models.BooleanField()
	exercised_evening = models.BooleanField()
	todays_medications = models.BooleanField()
	took_a_nap = models.BooleanField()
	length_of_nap = models.IntegerField()
	likelihood_of_dosing = models.Choice()
	days_mood = models.Choice()
	pre_bedtime_consumption = models.Choices()
	bedtime_routine = models.TextField()
