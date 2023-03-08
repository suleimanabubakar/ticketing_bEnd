from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('sales', views.SaleViewSet)
router.register('sales', views.SaleDetailViewSet)
router.register('tickets', views.TicketsViewSet)
router.register('tickets', views.TicketsDetailViewSet)



# URLConf
urlpatterns = router.urls