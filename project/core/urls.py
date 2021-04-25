# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path('tickets/', include('tickets.urls')),  # Ticket routes - Create, list, detail
    path("", include("accounts.urls")),              # UI Kits Html files
]

# Required to use the django debug toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path("__debug__/", include(debug_toolbar.urls))
                  ] + urlpatterns
