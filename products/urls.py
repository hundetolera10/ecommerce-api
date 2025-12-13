from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView
)
urlpatterns = [
     # Categories
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),

    # Products
    path('', ProductListCreateView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
]

