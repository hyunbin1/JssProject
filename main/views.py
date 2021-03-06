from django.shortcuts import render,redirect, get_object_or_404
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404 
from django.core.exceptions import PermissionDenied
# 로그인 데코레이터
from django.contrib.auth.decorators import login_required




def index(request):
    # index라는 함수에 자기소개서 데이터를 다 보내주기
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})



def my_index(request):
    # 필터를 사용해서 내 자소서만 보게 만들기
    my_jss = Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html', {'all_jss':my_jss})



    # 로그인이 안되어있을때 글 작성하지 못하게 하기
# [방법 1] 로그인 필요한 부분에 데코레이션 하기
@login_required(login_url="/login/")
def create(request):
    #[방법 2]
    #if request.user.is_authenticated:
    #    return redirect('login')

    # 만약 포스트라는 방식으로 객체 생성 요청이 들어왔다면,
    # Jssform에 post 방식으로 객체를 채워줘라 = create 해주는것
    if request.method == "POST":
        filled_form = JssForm(request.POST)     
        #유효성 검증, 저장이 쉬움
        if filled_form.is_valid():
            # 마지막] 임시 폼을 만들어서 유효성 검증이 되면 업데이트가 되기 전에 잠시 지연시킴 = commit false
            temp_form = filled_form.save(commit=False)
            # 현재 로그인된 유저를 넣어줌
            temp_form.author = request.user            
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
    # [방법 1]
    my_jss = get_object_or_404(Jasoseol, pk=jss_id)

    # [방법 2] try:
    # get = 객체 하나만 보내줘 - pk=1 객체 번호가 1번인 것을
    # my_jss = Jasoseol.objects.get(pk=1)
    # 원하는 객체 번호 불러오기 - index.html에서 사용한 jss_id(객체 번호)를 가져오기
    #    my_jss = Jasoseol.objects.get(pk=jss_id)
    # except: 
    #   raise Http404
    return render(request, 'detail.html', {'my_jss':my_jss }) 

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    # url로 다른 사람이 삭제하지 못하도록 하기
    if request.user == my_jss.author:
        my_jss.delete()
        return redirect('index')

    # 자기 글 삭제가 아니면 권한을 위반했다는 에러를 띄어주기
    raise PermissionDenied


def update(request, jss_id):

       # url로 다른 사람이 어베이트하지 못하도록 하기
    if request.user == my_jss.author:
        my_jss.update()
        return redirect('index')

    # 자기 글 업데이트가 아니면 권한을 위반했다는 에러를 띄어주기
    raise PermissionDenied


    #  기존에 쓰여져 있는 내용을 그대로 수정할때 가져오고 싶기때문에 가져옴
    my_jss = Jasoseol.objects.get(pk=jss_id)
    # jss_form에 모델 폼을 사용하려고 선언해줌 - instance라는 인자에 가져온 특정한 객체를 가져오게 되면 이 객체가 모델에 담기게 되서 랜더링이 됨
    jss_form = JssForm(instance=my_jss)
    # update 유효성 검증
    if request.method == "POST":
        update_form =JssForm(request.POST, instance=my_jss)
        if update_form.is_valid():
            update_form.save()
            return redirect('index') 
    
    # model form을 사용할 html을 연결시켜줌
    return render(request, 'create.html', {'jss_form':jss_form})



