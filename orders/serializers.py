from select import select
from rest_framework import serializers
from .models import Orders, ExtendedOrders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class OrderExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedOrders
        fields = '__all__'

    # def create(self, validated_data):
    #     order_id = validated_data['old_order']
    #     order = Orders.objects.get(id=order_id)
    #     order.extended = True
    #     order.save()
    #     return ExtendedOrders.objects.create(**validated_data)


class NumberOfOrdersForPeriodSerializer(serializers.Serializer):
    from_date = serializers.DateField()
    to_date = serializers.DateField()
    