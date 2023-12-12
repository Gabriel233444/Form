from django.urls import path
from .views import ReportFormView, FileUploadFormView, ListReportFormView, ListFileUploadFormView, \
    UpdateFileUploadFormView, UpdateReportFormView, DeleteFileUploadFormView, DeleteReportFormView, \
    DashboardView, ChoosePage, send_pdf, download_pdf

app_name = 'report'

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('choose', ChoosePage.as_view(), name='choose'),
    #Pdf
    path('pdf_view', send_pdf, name='pdf_view'),
    path('pdf_download', download_pdf, name='pdf_download'),
    #ReportForm
    path('report_form_view', ReportFormView.as_view(), name='report'),
    path('list_report_form_view', ListReportFormView.as_view(), name='list_report'),
    path('update_report_form_view/<pk>', UpdateReportFormView.as_view(), name='update_report'),
    path('delete_report_form_view/<pk>', DeleteReportFormView.as_view(), name='delete_report'),
    #FileUpload
    path('fileupload_form_view', FileUploadFormView.as_view(), name='fileupload'),
    path('list_fileupload_form_view', ListFileUploadFormView.as_view(), name='list_fileupload'),
    path('update_fileupload_form_view/<pk>', UpdateFileUploadFormView.as_view(), name='update_fileupload'),
    path('delete_fileupload_form_view/<pk>', DeleteFileUploadFormView.as_view(), name='delete_fileupload'),
]
