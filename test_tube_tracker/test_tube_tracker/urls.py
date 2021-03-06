"""test_tube_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# Use include() to add paths from the catalog application 
from django.conf.urls import include, url
from django.urls import path
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from catalog import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
   # path('', RedirectView.as_view(url='/catalog/')),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.sampledef, name='home'),
    path('accounts/', include('django.contrib.auth.urls')), # new
    url(r'^', include('catalog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
