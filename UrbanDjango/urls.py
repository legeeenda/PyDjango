from django.contrib import admin
from django.urls import path

from task2.views import func, Cls


urlpatterns = [
    # task 2
    path('admin/', admin.site.urls),
    path('func/', func),
    path('cls/', Cls.as_view()),
]