from django.urls import path
from . import views


app_name = 'delivery_app'

urlpatterns = [
    path('delivery/api/v0/delivery-points/', views.DeliveryPoints.as_view(), name='delivery-points'),
    path('delivery/api/v0/calculator/', views.Calculator.as_view(), name='calculator'),
    path('delivery/api/v0/delivery-create/', views.DeliveryCreate.as_view(), name='delivery-create'),
    path('delivery/api/v0/delivery-status/', views.DeliveryStatus.as_view(), name='delivery-status'),
    path('delivery/api/v0/delivery-cancel/', views.DeliveryCancel.as_view(), name='delivery-cancel'),
    path('delivery/api/v0/delivery-return/', views.DeliveryReturn.as_view(), name='delivery-return'),
    path('delivery/api/v0/delivery-intake/', views.DeliveryIntake.as_view(), name='delivery-intake'),

]
