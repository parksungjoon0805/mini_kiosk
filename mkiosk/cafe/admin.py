from django.contrib import admin
from .models import Category,Item,Order
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' )
    list_filter=('id',)
    search_fields = ('id', 'name')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'Category_id', )
    list_filter=('id',)
    search_fields = ('id', 'name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'order_date', 'item_count', 'order_price')
    list_filter = ('order_date',)
    search_fields = ('id', 'item__name')

admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
# admin.site.register(Order)
