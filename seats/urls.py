from django.urls import path
from rest_framework import routers
# from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('seats', views.SeatTypeViewSet, basename="seats")



# URLConf
urlpatterns = router.urls