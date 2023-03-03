
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Ticketing B/End API",
      default_version='v1',
      description="",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('charts/', include('charts.urls')),
    path('seats/', include('seats.urls')),
    path('fleet/', include('fleet.urls')),
    path('branches/', include('branches.urls')),
    path('currency/', include('accounting.urls')),
    path('routes/', include('routes.urls')),
    path('trips/', include('trips.urls')),
]
