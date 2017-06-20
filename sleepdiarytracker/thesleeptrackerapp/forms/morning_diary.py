from django import forms
from thesleeptrackerapp.models import MorningSleepData

class MorningDiaryForm(forms.ModelForm):
  bedtime = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'class': 'timepicker'}))
  class Meta:
    model = MorningSleepData

    fields = ('bedtime', 'exit_bed_time', 'ease_of_sleep', 'times_awoken', 'minutes_awake', 'total_sleep_time', 'factors_disturbing_sleep', 'subjective_waking_mood_rating', 'notes')
