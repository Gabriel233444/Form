from django.forms import ModelForm
from django.contrib.auth.models import User


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        
class UserUpdatForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        
class AdminCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password','is_staff', 'is_superuser')

class AdminLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        
class AdminUpdatForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'is_superuser')