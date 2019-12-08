from django.conf import settings
from django.db import models
from django.utils import timezone
#from 또는 import로 시작하는 부분은 다른 파일에 있는 것을 추가하라는 뜻 입니다.


class Post (models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # 길이 제한이 있는 문자열
    text = models.TextField()            
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title



    