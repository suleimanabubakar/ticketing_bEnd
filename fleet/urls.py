from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('fleet', views.FleetViewSet)
router.register('fleet_charts', views.FleetChartViewSet)



# URLConf
urlpatterns = router.urls