"""
Definition of urls for BoredGaming.
"""

from datetime import datetime
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.landing_page, name='landingpage'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^signup/$', app.views.signup, name='signup'),
    #url(r'^homepage/$', app.views.homepage, name='homepage'),
    url(r'^profiles/home', app.views.home, name='home' ),
    url(r'profiles/editprofile', app.views.update_profile, name='update_profile'),
    #TODO: profiles/username for linking a profile
    #For now, profiles/<user_id>
    url(r'profiles/(?P<user_id>[0-9]+)', app.views.user_profile, name='profile'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)