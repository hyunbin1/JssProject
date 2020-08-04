from django.shortcuts import render, redirect
# contrib.auth가 유저 모델 관련된 것들이 있다고 생각하면 된다. 
from django.contrib.auth.forms import UserCreationForm
# 로그인 기능 커스텀 하는법
from django.contrib.auth.views import LoginView
# Create your views here.

# 회원가입 함수 만들기
def signup(request):
    # 회원가입 폼 만들어주기 - 유저모델이 만들어져 있고, 장고에서 다 제공을 해줌
    # UsercCreationForm - 만들어져 있는 유저 폼 사용
    regi_form = UserCreationForm()
    # request post일 때 여기로 다시 돌아옴
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index') 

    return render(request, 'signup.html', {'regi_form':regi_form})

# 로그인 기능 커스텀 하는법
class MyLoginView(LoginView):
    template_name = 'login.html'
