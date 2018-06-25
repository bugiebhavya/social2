from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms
from django.views.generic import TemplateView

# Create your views here.
class TestPage(TemplateView):
    template_name='test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/signup.html"
