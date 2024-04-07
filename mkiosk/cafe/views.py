from django.shortcuts import render
from .models import Category, Item, Order
from django.shortcuts import redirect

# Create your views here.
def rich_cafe(request):
    categorys = Category.objects.all()
    context = {
        "lions" : categorys
    }
    return render(request, "cafe/rich_cafe.html", context)


def coffee_view(request):
    lions = Category.objects.filter(name='coffee')
    return render(request, 'cafe/coffee.html', {'lions': lions})

def tea_view(request):
    lions = Category.objects.filter(name='tea')
    return render(request, 'cafe/tea.html', {'lions': lions})

def dessert_view(request):
    lions = Category.objects.filter(name='dessert')
    return render(request, 'cafe/dessert.html', {'lions': lions})

def order_view(request):
    if request.method == 'POST':
        item_id = request.POST.get('item')
        item = Item.objects.get(id=item_id)
        quantity = request.POST.get('quantity')

        # 사용자가 입력한 수량을 정수로 변환합니다.
        item_count = int(quantity)

        # 주문을 생성합니다. 
        order = Order.objects.create(item=item, item_count=item_count, order_price=item.price * item_count)
        order.save()

        # 주문 내역 페이지로 이동합니다.
        return render(request, 'cafe/order.html', {'order': order})
    else:
        return redirect('home')