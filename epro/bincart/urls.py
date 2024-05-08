from django.urls import path
from . import views

urlpatterns =[
    path('view_cart/' , views.view_cart , name='view_cart'),
    # path('checkout_cart/<int:id>' , views.checkoutview , name='addtocart'),
    path('checkout_info/' , views.checkoutinfoview , name='checkout_info'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('showcart/', views.view_cart, name='showcart')
]