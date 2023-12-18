# AGT/forms.py

from django import forms

class ContactForm(forms.Form):
    # Define fields for the contact form
    your_name = forms.CharField(label='Your Name', max_length=100)
    your_email = forms.EmailField(label='Your Email', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def clean_your_name(self):
        # Validate the 'your_name' field if needed
        your_name = self.cleaned_data['your_name']
        # Add custom validation logic here if necessary
        return your_name

    def clean_your_email(self):
        # Validate the 'your_email' field if needed
        your_email = self.cleaned_data['your_email']
        # Add custom validation logic here if necessary
        return your_email

    def clean_message(self):
        # Validate the 'message' field if needed
        message = self.cleaned_data['message']
        # Add custom validation logic here if necessary
        return message

