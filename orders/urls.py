from django.urls import path
from .views import (
    CreateOrderView,
    OrderListView,
    OrderDetailView,
    PayOrderView
)

urlpatterns = [
    path('create/', CreateOrderView.as_view()),
    path('', OrderListView.as_view()),
    path('<int:pk>/', OrderDetailView.as_view()),
    path('<int:pk>/pay/', PayOrderView.as_view()),
]

