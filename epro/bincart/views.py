from django.shortcuts import render, redirect
from main.models import electric_product
from .models import it_cart
from django.contrib.auth.models import User
# Create your views here.


def add_to_cart(request, product_id):
    item = electric_product.objects.get(id=product_id)
    cart_items = it_cart.objects.filter(user_id=request.user)
    product_total_price=sum(int(i.electricproduct.orignal_price) * i.quantity for i in cart_items)
    # individual=[]
    # for itm in cart_items:
    #     product_price=int(itm.electricproduct.orignal_price) * itm.quantity
    #     print(product_price)
    #     individual.append(product_price)
    
    cart_item, created = it_cart.objects.get_or_create(electricproduct=item, user=request.user)
    # if not created:
    if cart_item:  
     # cart_item.quantity += 1
     cart_item.save()
    #  return redirect('showcart')

    context={
        "cartitems":cart_items,
        'product_total_price':product_total_price,
        # 'individual':individual,
    }    
    return render(request, 'bincart/checkout_cart.html',context)

# def checkoutview(request):
#     cart_items = it_cart.objects.all()
#     return render(request , 'bincart/checkout_cart.html',{'cart_items':cart_items})
def checkoutinfoview(request):
    return render(request , 'bincart/checkout_info.html')

def view_cart(request):
    cart_items = it_cart.objects.filter(user=request.user)
    print(cart_items)
    product_total_price=sum(int(i.electricproduct.orignal_price) * i.quantity for i in cart_items)

    return render(request, 'bincart/checkout_cart.html', {'cartitems': cart_items,'product_total_price':product_total_price,})
