"""
URL configuration for receiptdjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from vege import views
from django.conf import settings
from django.conf.urls.static import static
from .seed import seedStudents


urlpatterns = [
    path("",views.login_user),
    path("admin/", admin.site.urls),
    path('recipes/',views.recipes,name='recipes'),
    path('recipes_delete/<id>/',views.delete_recipe,name='recipes_delete'),
    path('recipes_update/<id>/',views.update_recipe,name='update_recipe'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('seed/',seedStudents,name='seed')
    

]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)