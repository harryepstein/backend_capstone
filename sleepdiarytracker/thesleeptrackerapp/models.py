# -*- coding: utf-8 -,*-
from __future__ import unicode_literals

from django.db import models
from django import forms
import arrow
from datetime import timedelta, datetime, time
from time import mktime, localtime

# Create your models here.

class MorningSleepData(models.Model):
	"""Define and Create A Sleep Data table in the database."""

	date = models.DateField(auto_now=True, auto_now_add=False)
	bedtime = models.TimeField()
	exit_bed_time = models.TimeField()


	EASILY = 1
	AFTER_SOME_TIME = 2
	WITH_DIFFICULTY = 3
	ease_of_sleep_choices = (
		(EASILY, 'Easily'),
		(AFTER_SOME_TIME, 'After Some Time'),
		(WITH_DIFFICULTY, 'With Difficulty'),
	)

	ease_of_sleep = models.IntegerField(choices=ease_of_sleep_choices, default=AFTER_SOME_TIME)
	times_awoken = models.IntegerField()
	minutes_awake = models.IntegerField()

	#NEED TO CALCULATE TOTAL SLEEP TIME FROM THE DIFFERENCE BETWEEN THE BEDTIME AND THE EXIT_BED_TIME
	# this is what I really want


	def total_sleep_time_differece(self):


		# bedtime_dt = datetime.fromtimestamp(mktime(localtime(self.bedtime)))
		# exit_bed_time_dt = datetime.fromtimestamp(mktime(localtime(self.exit_bed_time)))
		bedtime_dt = datetime(2012,1,1, self.bedtime.hour, self.bedtime.minute, self.bedtime.second)
		exit_bed_time_dt = datetime(2012,1,1, self.exit_bed_time.hour, self.exit_bed_time.minute, self.exit_bed_time.second)


		total_sleep_time_delta = bedtime_dt - exit_bed_time_dt
		print("Thus follows total_sleep_time_delta:", total_sleep_time_delta)
		return total_sleep_time_delta



	total_sleep_time = models.DurationField()



	factors_disturbing_sleep = models.TextField()


	REFRESHED = 'RE'
	SOMEWHAT_REFRESHED = 'SR'
	FATIGUED = 'FA'
	subjective_waking_mood_rating_choices = (
		(REFRESHED, 'Refreshed'),
		(SOMEWHAT_REFRESHED, 'Somewhat Refreshed'),
		(FATIGUED, 'Fatigued'),
	)
	subjective_waking_mood_rating = models.CharField(max_length=2, choices=subjective_waking_mood_rating_choices, default=SOMEWHAT_REFRESHED 	)
	notes = models.TextField()

	def get_fields(self):
	  return [(field.name, field.value_to_string(self)) for field in MorningSleepData._meta.fields]

	#Evening Diary
class EveningSleepData(models.Model):

	date = models.DateField(auto_now=True, auto_now_add=False)
	caffeine_consumption_morning = models.BooleanField()
	caffeine_consumption_evening = models.BooleanField()
	caffeine_consumption_afternoon = models.BooleanField()
	exercised_morning = models.BooleanField()
	exercised_afternoo = models.BooleanField()
	exercised_evening = models.BooleanField()
	todays_medications = models.TextField()
	took_a_nap = models.BooleanField()
	length_of_nap = models.IntegerField()

	NO_CHANCE = 'NC'
	SLIGHT_CHANCE = 'SC'
	MODERATE_CHANCE = 'MC'
	HIGH_CHANCE = 'HC'
	likelihood_of_dosing_choice = (
		(NO_CHANCE, 'No Chance'),
		(SLIGHT_CHANCE, 'Slight Chance'),
		(MODERATE_CHANCE, 'Moderate_Chance'),
		(HIGH_CHANCE, 'High Chance'),
	)
	likelihood_of_dosing = models.CharField(max_length=2, choices=likelihood_of_dosing_choice,default=SLIGHT_CHANCE)
	VERY_PLEASANT = 'VP'
	PLEASANT = 'PL'
	UNPLEASANT = 'UP'
	VERY_UNPLEASANT = 'VU'
	days_mood_choice = (
		(VERY_PLEASANT, 'Very Pleasant'),
		(PLEASANT, 'Pleasant'),
		(UNPLEASANT, 'Unpleasant'),
		(VERY_UNPLEASANT, 'Very Unpleasant'),
	)
	days_mood = models.CharField(max_length=4, choices=days_mood_choice, default=PLEASANT)

	ALCOHOL = 'AL'
	HEAVY_MEAL = 'HM'
	CAFFEINE = 'CA'
	NOT_APPLICABLE = "NA"
	pre_bedtime_consumption_choices = (
		(ALCOHOL, 'Alcohol'),
		(HEAVY_MEAL, 'Heavy Meal'),
		(CAFFEINE, 'Caffeine'),
		(NOT_APPLICABLE, 'Not Applicable'),
	)
	pre_bedtime_consumption = models.CharField(max_length=4, choices=pre_bedtime_consumption_choices, default=NOT_APPLICABLE)
	bedtime_routine = models.TextField()
