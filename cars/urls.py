from django.urls import path
from .views import CartListView, CarCreateView, CarDetailView, CarProfitView
urlpatterns = [
    path('', CartListView.as_view(), name='cars-list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    # path('category/<int:id>/', CategoryDetailApiView.as_view(), name='category-detail'),
    # path('categories/', CategoryListApiView.as_view(), name='categories-list'),
    path('create/', CarCreateView.as_view(), name='create-car'),
    path('profit-of-car/<int:id>/', CarProfitView.as_view(), name='profit-of-car'),
    # path('create/category/', AddCategoryApiView.as_view(), name='create-category'),
    # path('update/<int:pk>/', UpdateProductView.as_view(), name='update-product'),
    # path('filter/', FilterByCategories.as_view(), name='filter-by-category'),

]