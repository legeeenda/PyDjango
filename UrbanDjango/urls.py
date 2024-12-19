"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from task2.views import func, Cls
from task3.views import main, cart, shop
#from task4.views import cart, shop, main
#from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    # task 2
    path('admin/', admin.site.urls),
    path('func/', func),
    path('cls/', Cls.as_view()),
    
    #task3
    path('main/', main),
    path('cart/', cart),
    path('shop/', shop),


    # task 4
   # path('', main),
   # path('shop', shop),
   # path('cart', cart),

    # task 5
   # path('html', sign_up_by_html),
   # path('django', sign_up_by_django),
]
