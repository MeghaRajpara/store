from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db.models import Func, F, Value, ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order, OrderItem, Customer
from tags.models import TaggedItem

def say_hello(request):
    # order = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # Order.objects.aggregate(Count('id'))
    # OrderItem.objects.filter(product__id=1).aggregate(Count('product_id'))

    # queryset = Customer.objects.annotate(
    #     full_name = Func(F('first_name'), Value(' '),F('last_name'), function='CONCAT')
    # )

    # queryset = Customer.objects.annotate(
    #     full_name = Concat('first_name', Value(' '), 'last_name')
    # )

    # queryset = Customer.objects.annotate(
    #     orders_count = Count('order')
    # )

    # Expression wrapper
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())

    # queryset = Product.objects.annotate(discounted_price=discounted_price)

    # with transaction.atomic():
        #two different query if something goes wrong with 2nd one then it will roll back 1st one too.

    #raw sql query - it doesn't accept other thing update filter and all other
    # queryset = Product.objects.raw('SELECT * FROM store_product')

    return render(request, 'hello.html', {'name': 'megha', 'tags': list(queryset)})