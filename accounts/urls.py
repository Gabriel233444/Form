from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateUser, LoginUser, LogoutUser, UpdateUser, DeleteUser,\
    CreateAdminUser, UpdateAdminUser, DeleteAdminUser, LoginAdminUser, LogoutAdminUser, \
    AdminProfileList, UserList, View

app_name='accounts'

urlpatterns = [
    path('view', View.as_view(), name='view'),
    #create admin/user
    path('signup', CreateUser.as_view(), name='signup'),
    path('admin_signup', CreateAdminUser.as_view(), name='admin'),
    #login admin/user
    path('login', LoginUser.as_view(), name='login'),
    path('admin_login', LoginAdminUser.as_view(), name='admin_login'),
    #logout admin/user
    path('logout', LogoutUser, name='logout'),
    path('admin_logout', LogoutAdminUser, name='admin_logout'),
    #list admin/user
    path('user', UserList.as_view(), name='user'),
    path('admin_user', AdminProfileList.as_view(), name='admin_user'),
    #update admin/user
    path('update/<pk>', UpdateUser.as_view(), name='update'),
    path('admin_update/<pk>', UpdateAdminUser.as_view(), name='admin_update'),
    #delete admin/user
    path('delete/<pk>', DeleteUser.as_view(), name='delete'),
    path('admin_delete/<pk>', DeleteAdminUser.as_view(), name='admin_delete'),
    #password reset
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uid64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]