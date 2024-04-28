from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'main/index.html')
def about_us(request):
    return render(request , 'main/about_us.html')
def contact_us(request):
    return render(request , 'main/contact_us.html')
def faq(request):
    return render(request , 'main/faq.html')
def invers(request):
    return render(request , 'main/index_inverse_header.html')
def product(request):
    return render(request , 'main/product.html')
def product_detail(request):
    return render(request , 'main/product_detail.html')
def my_account(request):
    return render(request , 'main/my_account.html')
def search_results(request):
    return render(request , 'main/search_results.html')
def checkout_cart(request):
    return render(request , 'main/checkout_cart.html')
def checkout_complete(request):
    return render(request , 'main/checkout_complete.html')
def checkout_info(request):
    return render(request , 'main/checkout_info.html')
def checkout_payment(request):
    return render(request , 'main/checkout_payment.html')
def index_fixed_header(request):
    return render(request , 'main/index_fixed_header.html')
def index_inverse_header(request):
    return render(request , 'main/index_inverse_header.html')
