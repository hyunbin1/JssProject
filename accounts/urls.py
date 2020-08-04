from django.urls import path
from .views import signup , MyLoginView

# from django.contrib.auth.views import LoginView, LogoutView - 로그인 커스텀 안할때 
# 로그인 커스텀 할때 LoginView 삭제해줌
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name="signup"),
    # path('login/', login, name="login"), 이렇게 입력하지 않고 장고에서 제공하는 로그인 클레스를 사용한다.
    # class를 뷰에서 직접 실행하고 싶으면 .as_view를 써줘야 된다. 

    
    # path('login/' ,LoginView.as_view(), name="login"), - 기존 장고에 있는 폼 가져오는 법
    # 커스텀 해준 로그인 뷰 가져오는법
    path('login/' ,MyLoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
]  