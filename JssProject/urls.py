"""JssProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from main.views import index, create, detail, delete, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('create/', create, name="create"),
    # <int:jss_id>는 views.py 에서 지정한 객체 번호를 html,url과 연결시켜주는 것임.  
    path('detail/<int:jss_id>', detail, name="detail"),
    # 몇번 객체를 삭제하는지 알려줘야 되기 때문에 int:jss_id 사용해준다. 
    path('delete/<int:jss_id>', delete, name="delete"),
    path('update/<int:jss_id>', update, name="update"),


]
