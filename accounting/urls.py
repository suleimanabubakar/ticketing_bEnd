from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('currency', views.CurrencyViewSet, basename="currency")
router.register('currency', views.CurrencyDetailViewSet)




# URLConf
urlpatterns = router.urls