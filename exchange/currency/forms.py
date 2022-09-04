from django import forms
from .models import *
import requests


def get_currencies():
    url = "https://api.apilayer.com/exchangerates_data/latest"

    payload = {
        'symbols': '',
        'base': 'USD'
    }
    headers = {
        "apikey": "0G61uJfxj02q8S841GPAoPZeUOC6up7J"
    }

    response = dict(requests.request("GET", url, headers=headers, params=payload).json()['rates'])
    response_list = tuple([(a, b) for b, a in dict.items(response)])
    return response_list


class CurrencyForm(forms.Form):
    CHOISES = get_currencies()
    amount = forms.FloatField(label='Количество:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    before = forms.ChoiceField(label='До:', choices=CHOISES, widget=forms.Select(attrs={'class': 'form-control'}))
    after = forms.ChoiceField(label='После:', choices=CHOISES, widget=forms.Select(attrs={'class': 'form-control'}))
