from django.db import models
# 포린키를 위해 유저를 임폴트 해준다
from django.contrib.auth.models import User
# Create your models here.
class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    update_at = models.DateTimeField(null=True, auto_now=True) 


# cf] Primary key = pk = 데이터를 다룰때 사용하는 값 -  오브젝트를 식별할 수 있는 값 - 중복될 수 없는 단일 값


# 자소설 모델과 장고에서 만들어준 포린키로 연결을 시켜주고 싶음 - 한명이 자기의 파일들만 다루는것
# author = 필터 , on_delete 꼭써줘야됨 = 기존 모델(회원탈퇴)이 지워지면 어떻게 할거냐 - CASCADE = 모델이 지워지면 이 오브젝트(객체)도 지워줄것이다.
    # 글의 작성자를 어떻게 해줄거냐를 정의해주지 않았기 때문에 아직 migrate 불가능
    #[1. default 값으로 유저를 넣어주거나, 2. 유저를 넣어주지 않아도 되게 만들어주거나]
    # 선택 = 2. 유저 넣지 않아도 되게 - makemigrations 하고 null=True 사용
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # 만약에 작성자를 설정하고 싶으면 기존의 글들을 다 지우고 null도 지워준다음에 migrate 다시 해주면 됨.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 혹은 default 값을 관리자 계정으로 해주고 싶으면 null 대신에 default=관리자 계정 으로 설정해주면 됨.





