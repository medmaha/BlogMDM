

from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from users import views as users_views

from django.contrib.auth import  views as auth_view
from django.conf import settings
from django.conf.urls.static import static

def vieww(req):
    return render(req, 'users/aa.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', users_views.register, name='register'),
    path('login/', users_views.login_user, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    # password resetting path(urls)
    path('password-reset/',
        auth_view.PasswordResetView.as_view(
            template_name='users/password_reset.html'
            ),
        name='password_reset'
    ),
    path('password-reset/done/',
        auth_view.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
            ),
        name='password_reset_done'
    ),
    path('password-reset/confirm/<uidb64>/<token>/',
        auth_view.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'
            ),
        name='password_reset_confirm'
    ),
    path('password-reset-complete/',
        auth_view.PasswordResetDoneView.as_view(
            template_name='users/password_reset_complete.html'
            ),
        name='password_reset_complete'
    ),
    
    path('profile/<int:pk>/', users_views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns +=   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)