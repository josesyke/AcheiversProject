# from django.conf.urls import url
# from . import views
# from django.contrib.auth.views import (
#     login, logout, password_reset, password_reset_done, password_reset_confirm,
#     password_reset_complete
# )

# urlpatterns = [
#     url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
#     url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
#     url(r'^register/$', views.register, name='register'),
#     url(r'^profile/$', views.view_profile, name='view_profile'),
#     url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
#     url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
#     url(r'^change-password/$', views.change_password, name='change_password'),

#     url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),

#     url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),

#     url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),

#     url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete')

# ]


from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path(
       'reset-password/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/reset_password.html',
            success_url='/accounts/reset-password-done/'
    #   'reset-password/', PasswordResetView.as_view(
    #     template_name='accounts/reset_password.html',
    #     email_template_name='accounts/reset_password_email.html',
    #     success_url='accounts:password_reset_done'
    ), 
    name='reset_password'
    ),
    path(
        'reset-password-done/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),
        name='password_reset_done'
    
    ),
    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        PasswordResetConfirmView.as_view(
            template_name='accounts/reset_password_confirm.html',
            success_url='accounts:password_reset_complete'
        ), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(
        template_name='accounts/reset_password_complete.html'
    ), name='password_reset_complete'),

     path('edit_profile/', views.edit_profile, name='edit_profile'),
]
