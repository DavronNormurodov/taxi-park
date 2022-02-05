from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from .models import Cars
from rest_framework.response import Response
from orders.models import Orders, ExtendedOrders
from .serializers import CarSerializer
from rest_framework import status
# Create your views here.

class CartListView(ListAPIView):
    serializer_class = CarSerializer

    queryset = Cars.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.all()

class CarCreateView(CreateAPIView):

    serializer_class = CarSerializer


class CarDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = CarSerializer
    # lookup_url_kwarg = 'question_id'
    queryset = Cars.objects.all()

class CarProfitView(GenericAPIView):
    serializer_class = CarSerializer
    def get(self, request, id):
        car = Cars.objects.get(id=id)
        orders = Orders.objects.filter(cars_id=id)
        ordered_numbers = len(orders)
        days = 0
        extended_numbers = 0
        extended_days = 0
        profit_from_car = 0
        for order in orders:
            days += (order.to_date - order.from_date).days
            profit_from_car += days*car.rent_cost
            extended_orders = ExtendedOrders.objects.filter(order=order)
            extended_numbers += len(extended_orders)
            for extended_order in extended_orders:
                extended_days += (extended_order.extended_to - extended_order.extended_from).days
                profit_from_car += extended_days*car.rent_cost

        return Response(
            {'num_of_orders_for_car': ordered_numbers, 
            'num_of_extended_orders_for_car': extended_numbers, 
            'profit_from_car': profit_from_car}, status=status.HTTP_200_OK)
