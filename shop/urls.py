# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Corrected this line
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/edit/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
