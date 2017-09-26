from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='NoImage.jpg')
    author = models.ForeignKey(User, related_name='photo_posts')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # auto_now_add 처음에만 업데이트
    updated = models.DateTimeField(auto_now=True)     # auto_now     계속 자동 업데이트

    class Meta:                     # 모델안에 미리 정의된 규칙(정렬, 세팅 등)
        ordering = ('-updated',)    # 업데이트 내림차순

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%i:%s")