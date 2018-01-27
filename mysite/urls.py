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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .sitemaps import MainSitemap
from blog.sitemaps import BlogSitemap


urlpatterns = [
    url(r'^photos/', include('photos.urls')),
    url(r'^game/', include('hindsight1.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.about, name='home'),
    url(r'^myhome/(?P<username>[\w\-]+)/', views.myhome, name='myhome'),        
    url(r'^about/$', views.about, name='about'), 
]


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),

]

#Add sitemapts

sitemaps = {
        'blog': BlogSitemap(),
        'main': MainSitemap(),
        }

urlpatterns += [
        url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)