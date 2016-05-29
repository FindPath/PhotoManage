# coding=utf8

from django.db import models

# Create your models here.

#相册实体
class Album(models.Model):
    recordId=models.UUIDField(blank=True)                       #编号
    name=models.CharField(max_length=30,blank=True)             #名字
    rootId=models.CharField(max_length=20)                      #权限
    addtime=models.DateTimeField(blank=True)                    #添加时间
    updateTime=models.DateTimeField()                           #更新时间


#图片实体
class Photo(models.Model):
    recordId=models.UUIDField(blank=True)                       #编号
    name=models.CharField(max_length=30,blank=True)             #名字
    rootId=models.CharField(max_length=20)                      #权限
    addtime=models.DateTimeField(blank=True)                    #添加时间
    updateTime=models.DateTimeField()                           #更新时间
    photoUrl=models.CharField(max_length=200)                                 #路径
    title=models.CharField(max_length=30)                       #标题
    summary=models.TextField()                                  #简介

