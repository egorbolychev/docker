from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', ExchangeView.as_view(), name='exchange_url')
]
