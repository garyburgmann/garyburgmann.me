from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    your_email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    your_number = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': 'Your number'}))   
    your_message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}))