from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('payments', views.PaymentViewSet)
router.register('payments', views.PaymentDetailViewSet)
router.register('focs', views.FocsViewSet)
router.register('focs', views.FocsDetailViewSet)
router.register('discounts', views.DiscountsViewSet)
router.register('discounts', views.DiscountsDetailViewSet)
router.register('cashpayment', views.CashPaymentViewSet)
router.register('cashpayment', views.CashPaymentDetailViewSet)
router.register('mpesapayment', views.MpesaPaymentViewSet)
router.register('mpesapayment', views.MpesaPaymentDetailViewSet)



# URLConf
urlpatterns = router.urls