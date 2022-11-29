#web

from django.contrib import admin
from django.urls import path
from web import views



urlpatterns = [
   path('', views.main),
   path('question/', views.quest),
   path('answer/', views.answ),
   path('table/', views.tbl),
]