"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^photos/', include('photos.urls')),
    url(r'^game/', include('hindsight1.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),    
    url(r'^about/$', views.about, name='about'), 
]


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/logout/$', logout, name='logout'), 
]

#Add Photologue
urlpatterns += [
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
]

#Add Markdown
urlpatterns += [
    url(r'^markdownx/', include('markdownx.urls')),
]

#Add media path
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)