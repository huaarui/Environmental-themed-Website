'''
@-*- coding: utf-8 -*-
@ python：python 3.9
@ 创建人员：魏汶桦
@ 创建时间：2025/4/24
'''
from django.urls import path
from .views import home, soil_water_health, pollution_causes, actions_to_take, forum, more, industrial_pollution, \
    domestic_pollution, agricultural_pollution, create_post, create_comment

urlpatterns = [
    path('', home, name='home'),
    path('soil_water_health/', soil_water_health, name='soil_water_health'),
    path('pollution_causes/', pollution_causes, name='pollution_causes'),
    path('actions_to_take/', actions_to_take, name='actions_to_take'),
    path('forum/', forum, name='forum'),
    path('more/', more, name='more' ),
    path('industrial_pollution/', industrial_pollution, name='industrial_pollution'),
    path('domestic_pollution/', domestic_pollution, name='domestic_pollution'),
    path('agricultural_pollution/', agricultural_pollution, name='agricultural_pollution'),
    path('create_post/', create_post, name='create_post'),
    path('create_comment/<int:post_id>/', create_comment, name='create_comment'),
]