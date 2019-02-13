import random

from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import ContactForm
from project.settings import EMAIL_HOST_USER


def index_page_view(request):
    context = {}

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            context['form_success'] = True
            recipients = [EMAIL_HOST_USER]
            if request.POST.get('sith') != request.POST.get('jedi'):
                send_mail(
                    "Spam caught from {}".format(form.cleaned_data['your_name']),
                    form.cleaned_data['your_message'],
                    EMAIL_HOST_USER,
                    recipients
                )
            else:
                recipients.append(form.cleaned_data['your_email'])
                send_mail(
                    "New contact form submitted by {}".format(form.cleaned_data['your_name']),
                    form.cleaned_data['your_message'],
                    EMAIL_HOST_USER,
                    recipients
                )
            return redirect('/contact')
        else:
            context['form_error'] = True

    context['form'] = ContactForm()
    context['a'] = random.randint(1, 20)
    context['b'] = random.randint(1, 20)
    context['jedi'] = context['a'] + context['b']

    return render(request, 'webapp/index.html', context)


def contact_page_view(request):
    context = {}

    return render(request, 'webapp/contact.html', context)


# def about_page_view(request):
#     context = {}
#     return render(request, 'webapp/about.html', context)
