from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message =( f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

            send_mail(
                subject=f"New Contact Form Message from {name}",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  
                fail_silently=False,
            )

            send_mail(
                subject="Thanks for contacting us",
                message = f"""
                    Hi {name},

                    Thank you for contacting us.

                    We have received your message and will respond as soon as possible.

                    Best regards,
                    Your Website Team
                    """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            return render(request, 'contact_success.html')
           
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form})
