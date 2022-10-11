from django.db import models

# Create your models here.
# Основные требования:

# 1. Создать модель для справочника "Цвета".
# 2. Создать модель для справочника "Марки автомобилей"
# 3. Создать модель для справочника "Модели автомобилей"
# 4. Создать модель для хранения заказов авто. Заказ должен включать в себя цвет, модель, количество, дату (по умолчанию текущая).
# 5. С использованием библиотеки Django Rest Framework создать RestAPI для управления справочниками и заказами. API должно реализовать операции CRUD для моделей, а также чтение списков. 
# API для списка заказов должен возвращать элементы со след. атрибутами: дата заказа, цвет, марка авто, модель авто, количество.


class Color(models.Model):
    """
    Модель цвета.
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    Модель марки авто.
    """
    name = models.CharField(max_length=20)
    class Meta:
        ordering = ['name',]
    
    def __str__(self):
        return self.name


class Model(models.Model):
    """
    Модель авто.
    """
    name = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brands')

    class Meta:
        unique_together = ['name', 'brand']

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Модель заказа.
    """
    color = models.ForeignKey(Color,  on_delete=models.CASCADE, blank=False)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, blank=False, related_name='models')
    quantity = models.PositiveIntegerField(blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)
