# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from thesleeptrackerapp.models import MorningSleepData, EveningSleepData
from thesleeptrackerapp.forms import MorningDiaryForm, EveningDiaryForm
from django.http import HttpResponseRedirect
from django.db.models import Avg
import itertools

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
# from bokeh.sampledata.iris import flowers
from bokeh.models.widgets import Select
from bokeh.resources import CDN
from bokeh.models import SingleIntervalTicker, LinearAxis
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

    morning_diary_bedtime_and_date_tuple = list(MorningSleepData.objects.values_list('date','bedtime'))
    chart_values_x = []
    chart_values_y = []
    for item in morning_diary_bedtime_and_date_tuple:
        morning_diary_google_charts_compatible_container = []
        chart_values_x.append(item[0])
        chart_values_y.append(item[1])
        # chart_values.append(morning_diary_google_charts_compatible_container)

    # print("chart values_x,y:", chart_values_y[0])




    title = 'Bedtime Over Time'

    plot = figure(title= title,
        x_axis_label= 'Date',
        x_axis_type= 'datetime',
        y_axis_label= 'Bedtime',
        y_axis_type='datetime',
        plot_width =1000,
        plot_height=400)

    plot.scatter(chart_values_x, chart_values_y, legend= 'f(x)', line_width = 2)
    #Store components
    script, div = components(plot, CDN)

    # ticker = SingleIntervalTicker(interval=1, num_minor_ticks=0)
    # xaxis = LinearAxis(ticker=ticker)
    # plot.add_layout(xaxis, 'below')

    template_name = 'index.html'


    return render(request, template_name, {'all_morning_data': all_morning_data, 'all_evening_data': all_evening_data, 'morning_diary_bedtime_and_date_tuple': morning_diary_bedtime_and_date_tuple,'script' : script , 'div' : div})


# """NOT CURRENTLY IN USE"""
# def bokeh(request):
#     x= [1,3,5,7,9,11,13]
#     y= [1,2,3,4,5,6,7]
#     title = 'y = f(x)'

#     plot = figure(title= title,
#         x_axis_label= 'X-Axis',
#         y_axis_label= 'Y-Axis',
#         plot_width =400,
#         plot_height=400)

#     plot.line(x, y, legend= 'f(x)', line_width = 2)
#     #Store components
#     script, div = components(plot, CDN)

#    #Feed them to the Django template.
#     return render_to_response( 'bokeh.html', {'script' : script , 'div' : div} )

# def bokeh(request):
#     # s = Select(title="test", value="a", options=['a','b','c'])
#     plot = figure()
#     plot.circle([1,2], [3,4])
#     script,div = components(plot)
#     return render_to_response(request,'bokeh.html',{'script':script,'div':div})
