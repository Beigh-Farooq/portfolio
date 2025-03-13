from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"New Contact from {name}",
                message=f"Email: {email}\nPhone: {phone}\n\nMessage:\n{message}",
                from_email='your-email@gmail.com',
                recipient_list=['your-email@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'index.html', {'message': 'Message sent successfully!'})
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

