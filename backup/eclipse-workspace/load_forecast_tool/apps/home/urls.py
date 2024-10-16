# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('reports/', views.reports, name='reports'),
    path('creports/', views.creports, name='creports'),
    path('charts/', views.charts, name='charts'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
