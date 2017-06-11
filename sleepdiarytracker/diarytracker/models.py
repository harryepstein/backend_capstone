# -*- coding: utf-8 -,*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SleepData(models.Model):
	"""Define and Create A Sleep Datajkl table in the database"""
	date = DateField()
	bedtime = TimeField()
	exit_bed_time
	ease_of_sleep
	times_awoken
	minutes_awake
	total_sleep_time = exit_bed_time - bedtime
	factors_disturbing_sleep
	subjective_waking_mood_rating
	notes
	#Evening Diary
	caffeine_consumption_morning
	caffeine_consumption_evening
	caffeine_consumption_afternoon
	exercised_morning
	exercised_afternoon
	exercised_evening
	todays_medications
	took_a_nap
	length_of_nap
	likelihood_of_dosing
	days_mood
	pre_bedtime_consumption
	bedtime_routine
	pass

