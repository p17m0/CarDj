from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import Color, Order, Brand
from .serializers import BrandSerializer, ColorSerializer, OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    Viewset for order.
    """
    serializer_class = OrderSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ['model__brand']
    queryset = Order.objects.all()


class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for color.
    """
    serializer_class = ColorSerializer
    queryset = Color.objects.all()


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for brand.
    """
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
