from http import client
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from .models import Clients
from orders.models import Orders, ExtendedOrders
from .serializers import ClientSerializer
from rest_framework.response import Response
from rest_framework import status


class ClientListView(ListAPIView):
    serializer_class = ClientSerializer

    queryset = Clients.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.all()

class ClientCreateView(CreateAPIView):

    serializer_class = ClientSerializer


class ClientDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ClientSerializer
    # lookup_url_kwarg = 'question_id'
    queryset = Clients.objects.all()


class ClientExpenseView(GenericAPIView):
    serializer_class = ClientSerializer
    
    def get(self, request, id):
        orders = Orders.objects.filter(client_id=id)
        ordered_numbers = len(orders)
        extended_numbers = 0
        days = 0
        extended_days = 0
        expense = 0
        for order in orders:
            days += (order.to_date - order.from_date).days
            expense += order.cars.rent_cost*days
            extended_orders = ExtendedOrders.objects.filter(order=order)
            extended_numbers += len(extended_orders)
            for extended_order in extended_orders:
                extended_days += (extended_order.extended_to - extended_order.extended_from).days
                expense += extended_order.order.cars.rent_cost*extended_days

        return Response(
            {'num_of_orders': ordered_numbers, 
            'num_of_extended_order': extended_numbers, 
            'client_expense': expense}, status=status.HTTP_200_OK)
