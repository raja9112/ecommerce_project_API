from django.urls import path
from . import views
urlpatterns =[
    path('categories/', views.categoriesView.as_view()),
    path('Menu-Items/', views.MenuItemView.as_view()),
    path('MenuItem/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('Cart/', views.CartView.as_view()),
    path('Orders/', views.OrderView.as_view()),
    path('Order/<int:pk>/', views.SingleOrderView.as_view()),
    path('groups/manager/users', views.GroupViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'})),

    path('groups/delivery-crew/users', views.DeliveryCrewViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'}))
    
]