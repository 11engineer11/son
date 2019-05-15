"""app URL Configuration

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
from django.urls import path,include
from home.views import homeview,katil_post
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import login_view
from accounts.views import register_view
from accounts.forms import LoginForm
from home.views import login_redirect
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',homeview,name='home'),
    path('home/',include('home.urls')),
    path('', login_redirect, name='login_redirect'),
    path('accounts/',include('accounts.urls')),
    path('post/',include('post.urls')),
    
 
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
