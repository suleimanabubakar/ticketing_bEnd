from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('chart', views.ChartViewSet)
router.register('chart_seats', views.ChartSeatsViewSet, basename="chart_seats")



# URLConf
urlpatterns = router.urls
