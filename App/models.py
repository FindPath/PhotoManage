# coding=utf8

from django.db import models, migrations
import datetime
# Create your models here.

#相册实体
from django.utils import timezone


class Album(models.Model):
   # recordId=uuid.uuid1()                       #编号
    name=models.CharField(max_length=30)             #名字
    rootId=models.CharField(max_length=20)                      #权限
    addtime=models.DateTimeField(default = timezone.now)                    #添加时间
    updateTime=models.DateTimeField(auto_now=True)                           #更新时间
    summary=models.TextField()                                  #简介
    def __unicode__(self):
        return self.name

#图片实
class Photo(models.Model):
    # recordId=uuid.uuid1()                        #编号
    name=models.CharField(max_length=30,blank=True)             #名字
    rootId=models.CharField(max_length=20)                      #权限
    addtime=models.DateTimeField(default = timezone.now)                    #添加时间
    updateTime=models.DateTimeField(auto_now=True)                           #更新时间
    photoUrl=models.ImageField('图片',upload_to='uploadImages')                                 #路径
    title=models.CharField(max_length=30)                       #标题
    summary=models.TextField()                                  #简介
    Album=models.ForeignKey(Album)                              #相册
    def __unicode__(self):
        return self.name

