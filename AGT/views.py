from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .forms import ContactForm
from django.core.mail import send_mail
# Create your views here.

# AGT/views.py

def home(request):
    """Render the home page."""
    return render(request, "home.html")

def todos(request):
    """Render the todos page with a list of TodoItem objects."""
    # Retrieve all TodoItem objects from the database
    items = TodoItem.objects.all()
    # Pass the list of TodoItem objects to the template for rendering
    return render(request, "todos.html", {"todos": items })

def about(request):
    """Render the about page."""
    return render(request, "about.html")


def contact(request):
    """Handle the contact form submission."""
    if request.method == 'POST':
        # If the form is submitted, process the data
        form = ContactForm(request.POST)
        if form.is_valid():
            # If the form data is valid, handle the submission

            # Extract data from the form
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['sender_email']

            # Email sending logic
            send_mail(
                subject,
                message,
                sender_email,
                ['your@email.com'],  # Replace with the recipient's email address
                fail_silently=False,  # Set to True to suppress errors if email sending fails
            )
            print(form.cleaned_data)
            # Redirect or display a success message as needed
            # For now, let's redirect to the home page as an example
            return render(request, 'home.html')

    else:
        # If the form is not submitted, create a new instance of the form
        form = ContactForm()

    # Render the contact page with the form instance
    return render(request, 'contact.html', {'forms': form})
