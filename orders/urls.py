from django.urls import path
from .views import (OrderListView, OrderCreateView, OrderDetailView,
 OrderExtendView, ExtendedOrderDetailView, NumberOfOrdersForPeriod, ExtendencyCountView)
urlpatterns = [
    path('', OrderListView.as_view(), name='Orders-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('create/', OrderCreateView.as_view(), name='create-oder'),
    path('extend/', OrderExtendView.as_view(), name='extend-order'),
    path('extended/<int:pk>/', ExtendedOrderDetailView.as_view(), name='extended-order-detail'),
    path('orders-for-period/', NumberOfOrdersForPeriod.as_view(), name='orders-for-period'),
    path('extendency/<int:id>/', ExtendencyCountView.as_view(), name='extendency-numbers'),
    
    # path('categories/', CategoryListApiView.as_view(), name='categories-list'),
    # path('create/category/', AddCategoryApiView.as_view(), name='create-category'),
    # path('update/<int:pk>/', UpdateProductView.as_view(), name='update-product'),
    # path('filter/', FilterByCategories.as_view(), name='filter-by-category'),
]