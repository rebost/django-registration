"""
URLconf for registration and activation, using django-registration's
default backend.

If the default behavior of these views is acceptable to you, simply
use a line like this in your root URLconf to set up the default URLs
for registration::

    (r'^accounts/', include('registration.backends.default.urls')),

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
from registration.views import ActivationComplete, RegistrationComplete, RegistrationDisallowed


urlpatterns = patterns('',
                       url(r'^activate/complete/$', ActivationComplete.as_view(), name='registration_activation_complete'),
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       url(r'^activate/(?P<activation_key>\w+)/$',
                           activate,
                           {'backend': 'registration.backends.default.DefaultBackend'},
                           name='registration_activate'),
                       url(r'^register/$',
                           register,
                           {'backend': 'registration.backends.default.DefaultBackend'},
                           name='registration_register'),
                       url(r'^register/complete/$', RegistrationComplete.as_view(), name='registration_complete'),
                       url(r'^register/closed/$', RegistrationDisallowed.as_view(), name='registration_disallowed'),
                       (r'', include('registration.auth_urls')),
                       )
