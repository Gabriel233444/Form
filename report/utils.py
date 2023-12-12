# utils.py
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from xhtml2pdf import pisa
import os

def render_to_pdf(template_path, context, filename='weekly_report.pdf'):
    template = get_template(template_path)
    html = template.render(context)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f"filename='{filename}'"
    
    result = pisa.CreatePDF(
        html,
        dest=response,
        link_callback=lambda uri, _: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    )
    
    if result.err:
        return HttpResponse('We had some errors during PDF generation. Please check your HTML content and try again.')
    
    return response
 
def send_file_upload_email(file_upload):
    subject = 'Weekly Report'
    message = 'A new file has been uploaded.'
    from_email = settings.EMAIL_HOST_USER
    to_email = 'gabrielwilliams@torbitalimited.com'

    email = EmailMessage(subject, message, from_email, [to_email])

    # Attach the uploaded file to the email
    if file_upload.files:
        email.attach_file(file_upload.files.path)

    email.send()

