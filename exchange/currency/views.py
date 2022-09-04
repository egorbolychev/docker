from django.shortcuts import render
import requests
from django.urls import reverse_lazy

from django.views.generic import CreateView, FormView

from .forms import CurrencyForm


class ExchangeView(FormView):
    form_class = CurrencyForm
    template_name = 'currency/index.html'
    success_url = reverse_lazy('exchange_url')

    def get_context_data(self, *args, **kwargs):
        context = super(ExchangeView, self).get_context_data(**kwargs)
        context['title'] = 'Конвертер валюты'
        return context

    def form_valid(self, form):
        before = float(form.cleaned_data.get('before'))
        after = float(form.cleaned_data.get('after'))
        amount = float(form.cleaned_data.get('amount'))
        answer = round(after/before * amount, 2)
        return render(self.request, 'currency/index.html', context={'form': CurrencyForm(form.cleaned_data), 'answer': answer})
# Create your views here.
