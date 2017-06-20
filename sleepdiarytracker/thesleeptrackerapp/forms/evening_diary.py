from django import forms
from thesleeptrackerapp.models import EveningSleepData

class EveningDiaryForm(forms.ModelForm):

  class Meta:
    model = EveningSleepData
    fields = ('caffeine_consumption_morning', 'caffeine_consumption_afternoon', 'caffeine_consumption_evening', 'exercised_morning', 'exercised_afternoo', 'exercised_evening', 'todays_medications','took_a_nap', 'length_of_nap', 'likelihood_of_dosing', 'days_mood', 'pre_bedtime_consumption')
