from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('destinations', views.DestinationViewSet)
router.register('destinations', views.DestinationDetailsViewSet)
router.register('routes', views.RoutesViewSet)
router.register('routes', views.RoutesDetailsViewSet)



# URLConf
urlpatterns = router.urls