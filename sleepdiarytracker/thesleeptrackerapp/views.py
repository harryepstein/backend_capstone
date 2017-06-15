# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render
from thesleeptrackerapp.models import SleepData
from thesleeptrackerapp.forms import MorningDiaryForm, EveningDiaryForm


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
        form_data = request.POST

        p = PaymentType(
            user=request.user,
            name=form_data['name'],
            account_number=form_data['account_number'])

        p.save()
        template_name = 'account/add_payment.html'
        return HttpResponseRedirect('/view_account')

def evening_diary(request):


    if request.method == 'GET':
        evening_diary_form = EveningDiaryForm()
        template_name = 'evening_diary.html'
        return render(request, template_name, {'evening_diary_form': evening_diary_form})

    # if POST, gather form_data, save, and redirect to account view.
    elif request.method == 'POST':
        form_data = request.POST

        p = PaymentType(
            user=request.user,
            name=form_data['name'],
            account_number=form_data['account_number'])

        p.save()
        template_name = 'account/add_payment.html'
        return HttpResponseRedirect('/view_account')

# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request, template_name)
