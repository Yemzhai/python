from . import views
from django.conf.urls import url
urlpatterns = [
    url('products', views.products, name='products'),
    url('categories', views.categories, name='categories'),
    url('product/<int:id>/', views.product, name='product'),
    url('category/<int:id>/', views.category, name='category'),
    url('prodByCat/<int:id>/products', views.productsByCategory, name='productsByCategory'),
]