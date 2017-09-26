from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Photo

@login_required # 로그인을 하지않으면 동작하지 않음
def post_list(request):
    posts = Photo.objects.all()                              # 포스트라는 변수에 모든것을 불러옮.
    return render(request,'photo/list.html',{'posts':posts}) # 템플릿에서 'posts' 라는 변수를 사용함, posts는 이클래스의 값

