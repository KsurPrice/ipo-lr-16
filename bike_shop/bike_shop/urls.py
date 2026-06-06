from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('', include('products.urls')),
    path('', include('orders.urls')),
    path('api/', include('products.api_urls')),
    path('api/', include('orders.api_urls')),
    path('api/', include('accounts.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', TemplateView.as_view(template_name='registration/register.html'), name='register'),
    path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)