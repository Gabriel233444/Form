from django.forms import ModelForm
from .models import Form, FileUpload

class ReportForm(ModelForm):
    
    class Meta:
        model = Form
        fields = ('__all__')
        
class FileUploadForm(ModelForm):
    
    class Meta:
        model = FileUpload
        fields = ('__all__')
        