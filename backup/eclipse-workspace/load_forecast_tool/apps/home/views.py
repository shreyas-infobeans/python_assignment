# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
import random
from apps import fetchDBData
import datetime


# @login_required(login_url="/login/")
# def index(request):
#     time_block_intra = [i for i in range(1,13)]
#     dt_intraday = str(datetime.datetime.now()).split()[0]
#     dt_day_ahead = str(datetime.datetime.now() + datetime.timedelta(1)).split()[0]
#     # dt_intraday = '2022-09-05'
#     values_completion,values_completion1,values_completion2 = fetchDBData.fetch_intraday_forecast(dt_intraday)
#     labels_avg_user_level = [i for i in range(1,97)]
#     values_avg_user_level = fetchDBData.fetch_dayAhead_forecast(dt_day_ahead)
#     mape,max_err,min_err,rmse,error_percent = fetchDBData.fetch_data(dt_intraday)[1:]
#     context = {
#         "time_block_intra": time_block_intra,
#         "values_completion": values_completion,
#         "values_completion1": values_completion1,
#         "values_completion2": values_completion2,
#         "labels_avg_user_level": labels_avg_user_level,
#         "values_avg_user_level": values_avg_user_level,
#         "date_intra" : " ("+dt_intraday+")",
#         "date_day_ahead" :" ("+dt_day_ahead+")",
#         "mape" : mape,
#         "max_err" : max_err,
#         "min_err" : min_err,
#         "rmse" : rmse,
#         "error_percent":error_percent,
#     }

#     html_template = loader.get_template('home/index.html')
#     return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def index(request):
    time_block_intra = [i for i in range(1,13)]
    dt_intraday = str(datetime.datetime.now()).split()[0]
    dt_day_ahead = str(datetime.datetime.now() + datetime.timedelta(1)).split()[0]
    # dt_intraday = '2022-09-05'
    values_completion,values_completion1,values_completion2 = fetchDBData.fetch_intraday_forecast(dt_intraday)
    labels_avg_user_level = [i for i in range(1,97)]
    values_avg_user_level = fetchDBData.fetch_dayAhead_forecast(dt_day_ahead)
    mape,max_err,min_err,rmse,error_percent = fetchDBData.fetch_data(dt_intraday)[1:]
    l1 = [0.719, 0.607, 0.777, 0.152, 0.103, 0.728, 0.562, 0.741, 0.581, 0.537, 0.889]
    l2 = [0.947, 0.206, 0.5, 0.739, 0.356, 0.806, 0.141, 0.872, 0.493, 0.376, 0.388]
    tm1 = "10:06 PM"
    low_toll_1 = [-0.23, -0.23, -0.23, -0.23, -0.23, -0.23, -0.23, -0.23, -0.23, -0.23, -0.23]
    high_lim_1 = [0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23]

    l1_2 = [0.515, 0.871, 0.618, 0.539, 0.06, 0.051, 0.405, 0.77, 0.598, 0.156, 0.288]
    l2_2 = [0.899, 0.507, 0.062, 0.946, 0.688, 0.268, 0.417, 0.578, 0.437, 0.284, 0.48]
    tm1_2 = "10:12 PM"
    low_toll_1_2 = [-0.12 for i in range(12)]
    high_lim_1_2 = [0.12 for i in range(12)]

    l1_3 = [0.711, 0.725, 0.196, 0.16, 0.478, 0.773, 0.118, 0.973, 0.125, 0.084, 0.943]
    l2_3 = [0.268, 0.942, 0.554, 0.422, 0.434, 0.901, 0.31, 0.396, 0.614, 0.057, 0.093]
    tm1_3 = "10:17 PM"
    low_toll_1_3 = [-0.2 for i in range(12)]
    high_lim_1_3 = [0.2 for i in range(12)]

    l1_4 = [0.772, 0.868, 0.126, 0.382, 0.369, 0.27, 0.973, 0.897, 0.661, 0.689, 0.577]
    l2_4 = [0.261, 0.407, 0.933, 0.433, 0.393, 0.9, 0.702, 0.532, 0.727, 0.881, 0.2]
    tm1_4 = "10:22 PM"
    low_toll_1_4 = [-0.09 for i in range(12)]
    high_lim_1_4 = [0.09 for i in range(12)]

    context = {
        "time_block_intra": time_block_intra,
        "values_completion": values_completion,
        "values_completion1": values_completion1,
        "values_completion2": values_completion2,
        "labels_avg_user_level": labels_avg_user_level,
        "values_avg_user_level": values_avg_user_level,
        "date_intra" : " ("+dt_intraday+")",
        "date_day_ahead" :" ("+dt_day_ahead+")",
        "mape" : mape,
        "max_err" : max_err,
        "min_err" : min_err,
        "rmse" : rmse,
        "error_percent":error_percent,
        "l1":l1,
        "l2":l2,
        "tm1":tm1,
        "low_toll_1":low_toll_1,
        "high_lim_1":high_lim_1,

        "l1_2":l1_2,
        "l2_2":l2_2,
        "tm1_2":tm1_2,
        "low_toll_1_2":low_toll_1_2,
        "high_lim_1_2":high_lim_1_2,

        "l1_3":l1_3,
        "l2_3":l2_3,
        "tm1_3":tm1_3,
        "low_toll_1_3":low_toll_1_3,
        "high_lim_1_3":high_lim_1_3,

        "l1_4":l1_4,
        "l2_4":l2_4,
        "tm1_4":tm1_4,
        "low_toll_1_4":low_toll_1_4,
        "high_lim_1_4":high_lim_1_4,
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def reports(request):
    labels_completion = [i for i in range(1,97)]
    values_completion = [random.randint(1245,1455) for i in range(1,97)]
    labels_avg_user_level = [i for i in range(1,97)]
    values_avg_user_level = [random.randint(1245,1455) for i in range(1,97)]
    res = []
    if request.method == "POST":
        ddate = request.POST.get('forecastDate')
        print(ddate)
        res = fetchDBData.fetch_data(ddate)[0]
    # print(res)
        context = {
            'data':res,
            'date':res[0]['date']
        }
        print("test")
        html_template = loader.get_template('home/ui-tables.html')
        return HttpResponse(html_template.render(context, request))
        # return render(request, 'report.html',context)
    else:
        context = {
            'data':res
        }
        html_template = loader.get_template('home/ui-tables.html')
        return HttpResponse(html_template.render(context, request))
        # return render(request, 'report.html',context)

@login_required(login_url="/login/")
def creports(request):
    labels_completion = [i for i in range(1,97)]
    values_completion = [random.randint(1245,1455) for i in range(1,97)]
    labels_avg_user_level = [i for i in range(1,97)]
    values_avg_user_level = [random.randint(1245,1455) for i in range(1,97)]
    res = []
    if request.method == "POST":
        ddate = request.POST.get('forecastDate')
        print(ddate)
        res = fetchDBData.fetch_data_crep(ddate)[0]
        print(res)
    # print(res)
        context = {
            'data':res
        }

        html_template = loader.get_template('home/creports.html')
        return HttpResponse(html_template.render(context, request))
    else:
        context = {
            'data':res
        }
        html_template = loader.get_template('home/creports.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

 ###################################from original file ######################################   
# Create your views here.

@login_required(login_url="/charts/")
def charts(request):
    time_block_intra = [i for i in range(1,97)]
    res = []
    if request.method == "POST":
        dt_intraday = request.POST.get('forecastDate')
        res = fetchDBData.fetch_data(dt_intraday)[0]
        mape,max_err,min_err,rmse,error_percent = fetchDBData.fetch_data(dt_intraday)[1:]

        # print(dt_intraday)
    else:
        dt_intraday = str(datetime.datetime.now()).split()[0]
        res = fetchDBData.fetch_data(dt_intraday)[0]
        mape,max_err,min_err,rmse,error_percent = fetchDBData.fetch_data(dt_intraday)[1:]
        # dt_day_ahead = str(datetime.datetime.now() + datetime.timedelta(1)).split()[0]
    # dt_intraday = '2022-09-05'
    values_completion,values_completion1,values_completion2 = fetchDBData.fetch_intraday_forecast(dt_intraday)
    labels_avg_user_level = [i for i in range(1,97)]
    # values_avg_user_level = fetchDBData.fetch_dayAhead_forecast(dt_day_ahead)
    context = {
        "time_block_intra": time_block_intra,
        "values_completion": values_completion,
        "values_completion1": values_completion1,
        "values_completion2": values_completion2,
        "labels_avg_user_level": labels_avg_user_level,
        # "values_avg_user_level": values_avg_user_level,
        "date_intra" : " ("+dt_intraday+")",
        'data':res,
        "mape" : mape,
        "max_err" : max_err,
        "min_err" : min_err,
        "rmse" : rmse,
        "error_percent":error_percent,
        # "date_day_ahead" :" ("+dt_day_ahead+")",
    }

    html_template = loader.get_template('home/charts.html')
    return HttpResponse(html_template.render(context, request))