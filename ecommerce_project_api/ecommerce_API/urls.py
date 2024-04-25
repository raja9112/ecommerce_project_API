from django.urls import path
from . import views
urlpatterns =[
    path('categories/', views.categoriesView.as_view()),
    path('Menu-Items/', views.MenuItemView.as_view()),
    
]