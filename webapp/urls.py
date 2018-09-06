# webapp/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('contact', views.contact_page_view, name='contact'),
]
