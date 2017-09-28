from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','author','created','updated') # Admin 칼럼 변경
    list_filter = ('author','created','updated')       # 필터 설정
    search_fields = ('text','created')                 # 서치 설정
    raw_id_fields = ('author',)                        # 회원번호 등에서 쓰듯, 검색 가능,은 필수
    ordering = ['updated','created']                   # 모델의 odering과 다름, admin페이지의 오더링순
admin.site.register(Photo,PhotoAdmin)


class A:
    def funcA(self):
        print(self)
