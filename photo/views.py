from django.shortcuts import render

from .models import Photo

def post_list(request):
    posts = Photo.objects.all()                              # 포스트라는 변수에 모든것을 불러옮.
    return render(request,'photo/list.html',{'posts':posts}) # 템플릿에서 'posts' 라는 변수를 사용함, posts는 이클래스의 값

