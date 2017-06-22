# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from thesleeptrackerapp.models import MorningSleepData, EveningSleepData
from thesleeptrackerapp.forms import MorningDiaryForm, EveningDiaryForm, UserForm, ProfileForm
from django.http import HttpResponseRedirect
from django.db.models import Avg
from django.template import RequestContext

import itertools

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
# from bokeh.sampledata.iris import flowers
from bokeh.models.widgets import Select
from bokeh.resources import CDN
from bokeh.models import SingleIntervalTicker, LinearAxis
from bokeh.charts import Scatter, output_file, show, Bar
import arrow
import pandas as pd



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

    #GRAPH 1 query and extraction
    morning_diary_bedtime_and_date_tuple = list(MorningSleepData.objects.values_list('date','bedtime'))

    #GRAPH 2 data query and extraction
    morning_diary_bedtime_and_subjective_waking_mood_rating_tuple = list(MorningSleepData.objects.values_list('date', 'ease_of_sleep'))

    chart_values_x_graph1 = []
    chart_values_y_graph1 = []

    chart_values_x_graph2 = []
    chart_values_y_graph2 = []

    for item in morning_diary_bedtime_and_date_tuple:

        chart_values_x_graph1.append(item[0])
        chart_values_y_graph1.append(item[1])

    for item in morning_diary_bedtime_and_subjective_waking_mood_rating_tuple:

        chart_values_x_graph2.append(item[0])
        chart_values_y_graph2.append(item[1])





    title1 = 'Bedtime Over Time'
    title2 = 'Subjective Waking Mood Rating Over Time'

    plot1 = figure(title= title1,
        x_axis_label= 'Date',
        x_axis_type= 'datetime',
        y_axis_label= 'Bedtime',
        y_axis_type='datetime',
        plot_width =400,
        plot_height=400)

    plot2 = figure(title= title2,
        x_axis_label= 'Date',
        x_axis_type= 'datetime',
        y_axis_label= 'Ease of Sleep',
        y_axis_type='linear',
        plot_width =400,
        plot_height=400)

    plot1.scatter(chart_values_x_graph1, chart_values_y_graph1, legend= 'f(x)', line_width = 2)
    script1, div1 = components(plot1, CDN)

    plot2.scatter(chart_values_x_graph2, chart_values_y_graph2, legend= '1 = Easily; 2 = After Some Time; 3 = With Difficulty', line_width = 2)
    script2, div2 = components(plot2, CDN)



    template_name = 'index.html'

    return render(request, template_name, {'all_morning_data': all_morning_data, 'all_evening_data': all_evening_data, 'morning_diary_bedtime_and_date_tuple': morning_diary_bedtime_and_date_tuple,'script' : script1 , 'div' : div1, 'script2': script2, 'div2': div2})

def login_user(request):
    '''
    purpose: Handles the creation of a new user for authentication

    author: steve brownlee

    args: request -- The full HTTP request object

    returns: render index view or error if invalid login
    '''

    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username = request.POST['username']
        password = request.POST['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('/recommendations')

        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    return render(request, 'login.html', {}, context)

def register(request):
    """
    purpose: Handles the creation of a new user for authentication

    author:

    args: request -- The full HTTP request object

    returns: render of a registration from or invocation of django's login() method
    """

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            user.profile.phone_number = profile_form.cleaned_data['phone_number']
            user.profile.address = profile_form.cleaned_data['address']
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        profile_form = ProfileForm()
        template_name = 'register.html'
        return render(request, template_name, {
            'user_form': user_form,
            'profile_form': profile_form})

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage. Is there a way to not hard code
    # in the URL in redirects?????
    return HttpResponseRedirect('/')
