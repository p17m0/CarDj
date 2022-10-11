from rest_framework import serializers
from .models import Order, Color, Brand


class OrderSerializer(serializers.ModelSerializer):
    """
    Сериалайзер Order.
    """
    # model = serializers.StringRelatedField()
    # color = serializers.StringRelatedField()
    brand = serializers.SerializerMethodField('get_brand')

    class Meta:
        model = Order
        fields = ('color', 'model', 'quantity', 'date', 'brand')

    def get_brand(self, obj):
        return obj.model.brand.name
    

class ColorSerializer(serializers.ModelSerializer):
    """
    Сериалайзер Color.
    """
    quantity = serializers.SerializerMethodField('get_quantity')

    class Meta:
        model = Color
        fields = ('name', 'quantity')
    
    def get_quantity(self, obj):
        return Order.objects.filter(color=obj.id).count()
    
class BrandSerializer(serializers.ModelSerializer):
    """
    Сериалайзер Brand.
    """
    quantity = serializers.SerializerMethodField('get_quantity')

    class Meta:
        model = Brand
        fields = ('name', 'quantity')
    
    def get_quantity(self, obj):
        return Order.objects.filter(color=obj.id).count()