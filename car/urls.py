
from django.urls import path
from . import views

urlpatterns = [
    path("details/<int:id>", views.CarDetailsView.as_view(), name="details"),
    path('purchase/<int:car_id>/', views.purchase_car, name='purchase_car'),
]
