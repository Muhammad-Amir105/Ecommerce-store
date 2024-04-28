from django.urls import path
from . import views
urlpatterns = [
    path('index/' , views.index , name='index'),
    path('about_us/' , views.about_us , name='about_us'),
    path('contact_us/' , views.contact_us , name='contact_us'),
    path('faq/' , views.faq , name='faq'),
    path('invers/' , views.invers , name='invers'),
    path('product/' , views.product , name='product'),
    path('product_detail/' , views.product_detail , name='product_detail'),
    path('my_account/' , views.my_account , name='my_account'),
    path('search_results/' , views.search_results , name='search_results'),
    path('checkout_cart/' , views.checkout_cart , name='checkout_cart'),
    path('checkout_complete/' , views.checkout_complete , name='checkout_complete'),
    path('checkout_info/' , views.checkout_info , name='checkout_info'),
    path('checkout_payment/' , views.checkout_payment , name='checkout_payment'),
    path('index_fixed_header/' , views.index_fixed_header , name='index_fixed_header'),
    path('index_inverse_header/' , views.index_inverse_header , name='index_inverse_header'),
    
]