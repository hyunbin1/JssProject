from django.urls import path
from .views import index, create, detail, delete, update, my_index

urlpatterns =[
    path('', index, name="index"),
    path('my_index/', my_index, name="my_index"),
    path('create/', create, name="create"),
    # <int:jss_id>는 views.py 에서 지정한 객체 번호를 html,url과 연결시켜주는 것임.  
    path('detail/<int:jss_id>', detail, name="detail"),
    # 몇번 객체를 삭제하는지 알려줘야 되기 때문에 int:jss_id 사용해준다. 
    path('delete/<int:jss_id>', delete, name="delete"),
    path('update/<int:jss_id>', update, name="update"),

]