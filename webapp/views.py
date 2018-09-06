from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from myproject.settings import EMAIL_HOST_USER


def index_page_view(request):
    context = {}

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            context['form_success'] = True
            recipients = [EMAIL_HOST_USER]
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

    return render(request, 'webapp/index.html', context)


def contact_page_view(request):
    context = {}

    return render(request, 'webapp/contact.html', context)


# def about_page_view(request):
#     context = {}
#     return render(request, 'webapp/about.html', context)