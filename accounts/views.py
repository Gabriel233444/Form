from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin


from .forms import UserCreateForm, AdminCreateForm, UserLoginForm, AdminLoginForm, UserUpdatForm, AdminUpdatForm
# Create your views here.

def is_admin(user):
    return user.is_authenticated and user.is_staff
class View(TemplateView):
    template_name = 'views.html'

class CreateUser(CreateView):
    template_name = 'create.html'
    queryset = User.objects.all()
    form_class = UserCreateForm
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('/login')
        else:
            return render("Inavlid Signup")
        
class LoginUser(CreateView):
    template_name = 'login.html'
    queryset = User.objects.all()
    form_class = UserLoginForm
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/choose')
        else:
            return HttpResponse('details : User Not Found')
    
    
def LogoutUser(request):
    logout(request)
    return redirect('/login')

class UserList(LoginRequiredMixin, ListView):
    template_name = 'users.html'
    queryset = User.objects.all()
    context_object_name = 'users'
    login_url ='/login'

    def get_queryset(self):
        # Filter the queryset to include only normal users
        return User.objects.filter(is_staff=False)

class UpdateUser(LoginRequiredMixin, UpdateView):
    template_name = 'update.html'
    queryset = User.objects.all()
    form_class = UserUpdatForm
    success_url = '/user'
    login_url ='/login'
    success_message = 'user updated successfully'
    
class DeleteUser( LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = User.objects.all()
    context_object_name = 'user_delete'
    success_url = '/user'
    login_url ='/login'
    success_message = 'user deleted successfully'
        
class CreateAdminUser(CreateView):
    template_name = 'admin_signup.html'
    queryset = User.objects.all()
    form_class = AdminCreateForm
    success_message = 'create admin user successfully'
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = User.objects.create_superuser(username, email, password)
            user.save()
            return redirect('/admin_login')
        else:
            return render("Inavlid Admin Signup")

class LoginAdminUser(CreateView):
    template_name = 'admin_login.html'
    queryset = User.objects.all()
    form_class = AdminLoginForm
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/view')
        else:
            return HttpResponse({'Admin User Not Found'})
    
def LogoutAdminUser(request):
    logout(request)
    return redirect('/admin_login')
    
class AdminProfileList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'admin_users.html'
    queryset = User.objects.all()
    context_object_name = 'admin'
    login_url ='/admin_login'

    def test_func(self):
        return is_admin(self.request.user)
    
    def get_queryset(self):
        # Filter the queryset to include only admin users
        return User.objects.filter(is_staff=True)
    
class UpdateAdminUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'admin_update.html'
    queryset = User.objects.all()
    form_class = AdminUpdatForm
    success_url = '/admin_user'
    login_url ='/admin_login'

    def test_func(self):
        return is_admin(self.request.user)

class DeleteAdminUser(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'admin_delete.html'
    queryset = User.objects.all()
    context_object_name = 'admin_delete'
    success_url = '/admin_user'
    login_url ='/admin_login'

    def test_func(self):
        return is_admin(self.request.user)
    

