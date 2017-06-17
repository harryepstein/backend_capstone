# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render
from thesleeptrackerapp.models import MorningSleepData, EveningSleepData
from thesleeptrackerapp.forms import MorningDiaryForm, EveningDiaryForm
from django.http import HttpResponseRedirect
import numpy as np


def morning_diary(request):
    """
    purpose: Allows user to add a payment type to their account, from a submenu in the acount information view.

    author: Harry Epstein

    args: name: (string), acount number of credit card

    returns: (render): a view of of the request, template to use, and product obj
    """
    # if GET, create a payment form based on our model and render that form.
    if request.method == 'GET':
        morning_diary_form = MorningDiaryForm()
        template_name = 'morning_diary.html'
        return render(request, template_name, {'morning_diary_form': morning_diary_form})

    # if POST, gather form_data, save, and redirect to account view.
    elif request.method == 'POST':


        f = MorningDiaryForm(request.POST)
        newsleepdata = f.save()

        template_name = 'morning_diary.html'
        return HttpResponseRedirect('/morning_diary')

def evening_diary(request):


    if request.method == 'GET':
        evening_diary_form = EveningDiaryForm()
        template_name = 'evening_diary.html'
        return render(request, template_name, {'evening_diary_form': evening_diary_form})

    # if POST, gather form_data, save, and redirect to account view.
    elif request.method == 'POST':

        f = EveningDiaryForm(request.POST)
        if f.is_valid():
          f.save()
        else:
          return HttpResponseRedirect('/evening_diary')
        return HttpResponseRedirect('/evening_diary')

# Create your views here.

def index(request):
    all_evening_data = EveningSleepData.objects.all()
    all_morning_data = MorningSleepData.objects.all()
    '''
    Fetch and convert all bedtimes to seconds in order to dynamically calculate total sleep time from the differnce between bedtime and
    '''
    def average_bedtime():
      all_bedtimes = MorningSleepData.objects.values_list('bedtime')
      bedtime_array = []
      for time in all_bedtimes:
        bedtime_array.append(time[0])

        # print(time[1])

    template_name = 'index.html'
    return render(request, template_name, {'all_morning_data': all_morning_data, 'all_evening_data': all_evening_data})
