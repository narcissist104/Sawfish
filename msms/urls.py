"""msms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lessons import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('log_in/', views.log_in, name='log_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    # URLs for Student
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student_request_form/', views.student_request_form, name='student_request_form'),
    path('view_request_form/', views.view_request_form, name='view_request_form'),
    # URLs for Admins
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage_requests/', views.manage_requests, name='manage_requests'),
    path("manage_requests/edit/<request_id>", views.edit_requests, name='edit_requests'),
    path("manage_requests/delete/<request_id>", views.delete_requests, name='delete_requests'),
    # URLs for Directors
    path('director_dashboard/', views.director_dashboard, name='director_dashboard'),
    path('manage_accounts/', views.manage_accounts, name='manage_accounts'),
    path('manage_accounts/add', views.create_account, name='create_account'),
    path("manage_accounts/edit/<account_id>", views.edit_account, name='edit_account'),
    path("manage_accounts/delete/<account_id>", views.delete_account, name='delete_account')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
