from django.shortcuts import render,redirect
from .forms import JssForm
from .models import Jasoseol
# Create your views here.

def index(request):
    # index라는 함수에 자기소개서 데이터를 다 보내주기
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})


def create(request):
    # 만약 포스트라는 방식으로 객체 생성 요청이 들어왔다면,
    # Jssform에 post 방식으로 객체를 채워줘라 = create 해주는것
    if request.method == "POST":
        filled_form = JssForm(request.POST)     
        #유효성 검증, 저장이 쉬움
        if filled_form.is_valid():
            filled_form.save()
            # redirect = url페이지 이름을 써줌으로서 데이터 다루지 않고 그저 그 페이지로 옮겨줌
            # 새로 객체가 생성됐으면 목록으로 다시 돌아가게 해주는 것
            return redirect('index')
    # 폼을 띄어주기 위한 것 - 1. form에서 class로 지정했던 JssForm을 jss_form으로 같게 만들어준다
    # render의 3번째 인자 = 딕셔너리 형태로 이름을 지어서 폼을 보내주기
    jss_form = JssForm()
    
    return render(request, 'create.html', {'jss_form':jss_form})

# detail.html 만들어주기 - 상세 설명마다 모든 html 파일을 생성하는 것이 아니라 이 하나를 가지고
# 원하는 특정 데이터를 제공할 수 있게 만들어줄것임 

def detail(request, jss_id): 
    # get = 객체 하나만 보내줘 - pk=1 객체 번호가 1번인 것을
    # my_jss = Jasoseol.objects.get(pk=1)
    # 원하는 객체 번호 불러오기 - index.html에서 사용한 jss_id(객체 번호)를 가져오기
    my_jss = Jasoseol.objects.get(pk=jss_id)

    return render(request, 'detail.html', {'my_jss':my_jss }) 

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index')