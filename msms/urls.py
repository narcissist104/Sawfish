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
    path('', views.home),
    path('log_in/', views.log_in),
    path('sign_up/', views.sign_up),
    # URLs for Student
    path('', views.student_dashboard, name='student_dashboard'),
    path('student_request_form/', views.student_request_form, name='student_request_form'),
    path('view_request_form/', views.view_request_form, name='view_request_form'),
    path('admin_requests/', views.admin_requests),
    path("admin_requests/edit/<request_id>", views.admin_edit_requests),
    path("admin_requests/delete/<request_id>", views.admin_delete_requests)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
