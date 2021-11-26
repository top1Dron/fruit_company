from django.urls import path

from admin import views

app_name = 'admin'

urlpatterns = [
    path('', views.index, name="index"),
    
    path('buy-apples', views.buy_apples, name="buy_apples"),
    path('buy-bananas', views.buy_bananas, name="buy_bananas"),
    path('buy-pineapples', views.buy_pineapples, name="buy_pineapples"),
    path('buy-peaches', views.buy_peaches, name="buy_peaches"),
    
    path('sell-apples', views.sell_apples, name="sell_apples"),
    path('sell-bananas', views.sell_bananas, name="sell_bananas"),
    path('sell-pineapples', views.sell_pineapples, name="sell_pineapples"),
    path('sell-peaches', views.sell_peaches, name="sell_peaches"),
    
    path('add-money', views.add_money, name="add_money"),
    path('take-money', views.take_money, name="take_money"),
]
