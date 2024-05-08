from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView,TemplateView
from .models import catagory ,brand ,electric_product , ProductDetail,product_galary,rating 
from bincart.models import it_cart
from .forms import ratingform
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

def checkout_complete(request):
    return render(request , 'main/checkout_complete.html')



def checkout_payment(request):
    return render(request , 'main/checkout_payment.html')
def index_fixed_header(request):
    return render(request , 'main/index_fixed_header.html')
def index_inverse_header(request):
    return render(request , 'main/index_inverse_header.html')


def category_list(request):
    categories = catagory.objects.all()
    categories1 = electric_product.objects.filter(catagory__name='tablet' )
    categories2 = electric_product.objects.filter(catagory__name='mobile')
    prod=electric_product.objects.filter(catagory__name='mobile')
    brandy = brand.objects.all()
    popular_product=electric_product.objects.filter(is_populer=True)[:6]
    context={'categories': categories,'categories1': categories1,'categories2': categories2, 'brandy': brandy , 'is_populer':popular_product , 'prod':prod}
    return render(request, 'main/index.html', context)



class product_detail(DetailView):
    model=electric_product
    template_name='main/product_detail.html'
    context_object_name='product_det'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        print(pk)
        context = super().get_context_data(**kwargs)
        product_det = context[self.context_object_name]
        product_det_quantity = int(product_det.quantity)
        context['product_det_quantity'] = product_det_quantity
        product_images = product_det.product_galary_set.all() 
        context['product_images'] = product_images
        product_details=product_det.productdetail_set.all()
        context['product_details']=product_details
        ratings=product_det.rating_set.all()
        context['ratings']=ratings
        context['rating_form'] = ratingform()
        popular_products = electric_product.objects.filter(is_populer=True)[:6]
        context['popular_products'] = popular_products
        return context
    
    
    
    
    def post(self, request, *args, **kwargs):
        form = ratingform(request.POST)
        if form.is_valid():
            # Process the submitted data
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            discription = form.cleaned_data['discription']
            rate = form.cleaned_data['rate']
            
            # Save the rating to the database
            product_det = self.get_object()  # Get the product object
            rating.objects.create(
                electproduct=product_det,
                name=name,
                title=title,
                discription=discription,
                rate=rate
            )
            
            # Redirect to the product detail page
            return redirect('product_detail', pk=self.kwargs['pk'])
        else:
            # If the form is not valid, re-render the page with the form and errors
            return self.get(request, *args, **kwargs)


        




def show_product(request, category_name ):
    products = electric_product.objects.filter(catagory__name=category_name)
    
    context = {
        'products': products,
        'category_name': category_name
    }
    return render(request, 'main/product.html', context)

def show_product_brand(request, brand_name ):
    products = electric_product.objects.filter(brand__name=brand_name)
    context = {
        'products': products,
        'brand_name': brand_name
    }
    return render(request, 'main/product.html', context)






   





