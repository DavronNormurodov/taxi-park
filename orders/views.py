from msilib.schema import ServiceInstall
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Orders, ExtendedOrders
from .serializers import OrderSerializer, OrderExtendSerializer, NumberOfOrdersForPeriodSerializer
from django.http import HttpResponse, JsonResponse

class OrderListView(ListAPIView):
    serializer_class = OrderSerializer

    queryset = Orders.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.all()

class OrderCreateView(CreateAPIView):

    serializer_class = OrderSerializer


class OrderDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = OrderSerializer
    # lookup_url_kwarg = 'question_id'
    queryset = Orders.objects.all()

class NumberOfOrdersForPeriod(GenericAPIView):
    serializer_class = NumberOfOrdersForPeriodSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            orders = Orders.objects.filter(from_date__gte=data['from_date'], to_date__lte=data['to_date'])   
            return Response({'numbers_of_orders': len(orders)}, status=status.HTTP_200_OK)


class OrderExtendView(GenericAPIView):
    serializer_class = OrderExtendSerializer
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            order_id = serializer.data['order']
            order = Orders.objects.get(id=order_id)
            order.extended = True
            order.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ExtendedOrderDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = OrderExtendSerializer
    # lookup_url_kwarg = 'question_id'
    queryset = ExtendedOrders.objects.all()



class ExtendencyCountView(GenericAPIView):
    serializer_class = OrderExtendSerializer

    def get(self, request, id):
        # car = Cars.objects.get(id=id)
        order = Orders.objects.get(id=id)
        extendency_number = len(ExtendedOrders.objects.filter(order=order))

        return Response({'extendency_number': extendency_number}, status=status.HTTP_200_OK)

