from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'webapp/index.html'

class AboutPageView(TemplateView):
    template_name = 'webapp/about.html'