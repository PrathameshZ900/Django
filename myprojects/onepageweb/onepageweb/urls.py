"""
URL configuration for onepageweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from onepageweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about-us/<str:idd>', views.about_us),
    path('course/<slug:courseid>',views.course),
    path('CheckPrime/<int:n>',views.check_prime),
    path("djangohome/",views.homeDjango),
    path("listDjango/",views.stdData),
    path("userform/",views.userform),
    path("submit/",views.submit),
    path("get/",views.sum),
    path("post/",views.sumpost),
    path("action/",views.action,name="action"),
    path("formdjango/",views.formDjango),
    path("service/",views.service_view,name='service_view'),
    path("news/",views.news),
    path("newsdetail/<newsid>",views.newsdetail),

    

]
# from django.urls import path
# from onepageweb import views

# urlpatterns = [
#     path('prime/', views.check_prime, name='check_prime'),
# ]
