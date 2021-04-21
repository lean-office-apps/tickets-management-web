# -*- encoding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path('tickets/', include('tickets.urls')),  # Ticket routes - Create, list, detail
    path("", include("authentication.urls")),   # Auth routes - login / register
    path('groups/', include('groups.url')),     # Grouping of tickets and users (group, project)
    #path("", include("app.urls")),              # UI Kits Html files
]

# Required to use the django debug toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path("__debug__/", include(debug_toolbar.urls))
                  ] + urlpatterns
