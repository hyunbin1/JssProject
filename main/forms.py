from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm): 

    class Meta:
        model = Jasoseol
        # jasoseol에 대응되는 필드를 만들어줌
        fields = ("title", 'content',)
# 모델 커스텀하는방법 : 들어오는 모든걸 받아주는 파라미터 적용
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"

        self.fields['title'].widget.attrs.update({
            'class': 'jss_title', 
            'placeholder': '제목',
                     
        })

        