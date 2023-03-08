from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('customers', views.CustomerViewSet)
router.register('customers', views.CustomerDetailsViewSet)




# URLConf
urlpatterns = router.urls