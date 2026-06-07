from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', TemplateView.as_view(template_name='registration/register.html'), name='register'),
]