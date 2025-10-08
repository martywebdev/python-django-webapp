from .emails import send_confirmation_email
from .forms import ApplicationForm
from .models import Form

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Form.objects.create(**form.cleaned_data)
            
            
            # message_body = f"A new job application was submitted. Thank you, {form.cleaned_data.get('first_name')}"
            # email_message = EmailMessage("Form submission confirmation", message_body, to={form.cleaned_data.get('email')})
            # email_message.send()
            
            send_confirmation_email(form.cleaned_data)
            
            messages.success(request, "Form submitted successfully!")
            return redirect('index')  # ← redirect after saving
    else:
        form = ApplicationForm()

    return render(request, 'index.html', {'form': form})
