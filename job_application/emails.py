from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(form_data):
    subject = "Job Application Confirmation"
    body = (
        f"Hi {form_data['first_name']},\n\n"
        "Thanks for applying! We've received your application and will review it soon.\n\n"
        "Best regards,\nHR Team"
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [form_data['email']],
        fail_silently=False,
    )
