"""
URLconf for registration and activation, using django-registration's
one-step backend.

If the default behavior of these views is acceptable to you, simply
use a line like this in your root URLconf to set up the default URLs
for registration::

    (r'^accounts/', include('registration.backends.simple.urls')),

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead.

"""


try:
    from django.conf.urls import (include, patterns, url)
except ImportError:
    # for django <= 1.3
    from django.conf.urls.defaults import (include, patterns, url)

from registration.views import activate
from registration.views import register
from registration.views import RegistrationDisallowed


urlpatterns = patterns('',
                       url(r'^register/$',
                           register,
                           {'backend': 'registration.backends.simple.SimpleBackend'},
                           name='registration_register'),
                       url(r'^register/closed/$', RegistrationDisallowed.as_view(), name='registration_disallowed'),
                       (r'', include('registration.auth_urls')),
                       )
