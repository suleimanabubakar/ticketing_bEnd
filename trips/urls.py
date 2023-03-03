from rest_framework import routers
from . import views 

router = routers.DefaultRouter()

router.register('trips', views.TripViewSet)
router.register('trip-details', views.TripDetailsViewSet)
router.register('trip-driver', views.TripDriverViewSet)
router.register('trip-pricings', views.TripPricingsViewSet)
router.register('trip-seats-involved', views.TripSeatsInvolvedViewSet)
router.register('trip-seats', views.TripSeatsViewSet)

urlpatterns = router.urls