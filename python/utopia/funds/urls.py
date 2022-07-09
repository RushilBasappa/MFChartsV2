from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^funds/$', views.fund_list, name="list"),
    re_path(r'^navs/$', views.nav_list, name="nav"),
    re_path(r'^dates/$', views.date_list, name="date"),
    path('navs/<int:id>', views.nav_detail),
    path('funds/<int:id>', views.fund_detail),
    path('dates/<int:id>', views.date_detail),

]
