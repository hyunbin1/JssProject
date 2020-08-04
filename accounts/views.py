from django.shortcuts import render

# Create your views here.

# 회원가입 함수 만들기
def signup(request):

    return render(request, 'signup.html')