from django.urls import path
from .views import ClientListView, ClientCreateView, ClientDetailView, ClientExpenseView
urlpatterns = [
    path('', ClientListView.as_view(), name='Clients-list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='Client-detail'),
    # path('category/<int:id>/', CategoryDetailApiView.as_view(), name='category-detail'),
    # path('categories/', CategoryListApiView.as_view(), name='categories-list'),
    path('create/', ClientCreateView.as_view(), name='create-Client'),
    path('<int:id>/expense/', ClientExpenseView.as_view(), name='client-expense'),
    # path('create/category/', AddCategoryApiView.as_view(), name='create-category'),
    # path('update/<int:pk>/', UpdateProductView.as_view(), name='update-product'),
    # path('filter/', FilterByCategories.as_view(), name='filter-by-category'),

]