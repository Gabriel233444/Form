from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView,UpdateView, DeleteView, TemplateView
from django.conf import settings
import os

from .models import Form, FileUpload
from .forms import ReportForm, FileUploadForm
from .utils import send_file_upload_email, render_to_pdf

class DashboardView(TemplateView):
    template_name = 'home.html'

class FileUploadFormView(LoginRequiredMixin, CreateView):
    template_name = 'file_upload.html'
    queryset = FileUpload.objects.all()
    form_class = FileUploadForm
    login_url ='/login'
        
    def form_valid(self, form):
        file_upload = form.save(commit=False)
        file_upload.user = self.request.user
        file_upload.save()
        send_file_upload_email(file_upload)
        return super().form_valid(form)


class ReportFormView(LoginRequiredMixin, CreateView):
    template_name = 'report_form.html'
    queryset = Form.objects.all()
    form_class = ReportForm
    success_message = 'report submitted successfully'
    login_url ='/login'
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ReportForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/list_report_form_view')
        else:
            form = ReportForm()
            
        return render(request, self.template_name, {'form': form})
    
    
def send_pdf(request):
    data = Form.objects.all()
    context = {'report': data}
    
    pdf = render_to_pdf('list_report.html', context)
    
    temp_pdf_path = 'temp_pdf.pdf'
    with open(temp_pdf_path, 'wb') as temp_pdf:
        temp_pdf.write(pdf.content)
        
    subject = 'Weekly Report'
    message = 'Attached is the PDF file.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['gabrielwilliams@torbitalimited.com']
    
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.attach_file(temp_pdf_path)
    email.send()
    
    os.remove(temp_pdf_path)
        
    return HttpResponse('PDF sent to email successfully')
    
    
def download_pdf(request):
    data = Form.objects.all()
    context = {'report': data}
    pdf = render_to_pdf('list_report.html', context)
    return pdf

class ChoosePage(LoginRequiredMixin, TemplateView):
    template_name = 'choose.html'
    login_url ='/login'
            
    
class ListFileUploadFormView(LoginRequiredMixin, ListView):
    template_name = 'list_fileupload.html'
    context_object_name = 'fileupload'
    login_url = '/login'

    def get_queryset(self):
        return FileUpload.objects.filter(user=self.request.user)


class ListReportFormView(LoginRequiredMixin, ListView):
    template_name = 'list_report.html'
    context_object_name = 'report'
    login_url ='/login'
    
    def get_queryset(self):
        return Form.objects.filter(user=self.request.user)
    
class UpdateFileUploadFormView(LoginRequiredMixin, UpdateView):
    template_name = 'update_fileupload.html'
    queryset = FileUpload.objects.all()
    form_class = FileUploadForm
    login_url ='/login'
    
    def form_valid(self, form):
        file_upload = form.save(commit=False)
        file_upload.user = self.request.user
        file_upload.save()
        send_file_upload_email(file_upload)
        return super().form_valid(form)
    
class UpdateReportFormView(LoginRequiredMixin, UpdateView):
    template_name = 'update_report.html'
    queryset = Form.objects.all()
    form_class = ReportForm
    success_message = 'report updated successfully'
    login_url ='/login'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ReportForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/list_report_form_view')
        else:
            form = ReportForm()
            
        return render(request, self.template_name, {'form': form})
    
class DeleteFileUploadFormView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_fileupload.html'
    queryset = FileUpload.objects.all()
    context_object_name = 'fileupload'
    success_url = '/fileupload_form_view'
    login_url ='/login'

    
class DeleteReportFormView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_report.html'
    queryset = Form.objects.all()
    context_object_name = 'delete'
    success_url = '/report_form_view'
    login_url ='/login'
    