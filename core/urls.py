from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def home(request):
	return render(request, 'pages/home/index.html')

urlpatterns = [
    path('', home, name = 'home'),
    path('crm-admin-secure/', admin.site.urls),
    path('auth/', include('account.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)