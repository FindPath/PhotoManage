# coding=utf8
from django.contrib import admin

# Register your models here.
from App.models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    fieldsets  = [
        (None,               {'fields': ['name']}),
        ('information', {'fields': ['summary']}),
          ]

class PhotoInline(admin.StackedInline):
    model = Photo

class PhotoAdmin(admin.ModelAdmin):
    fieldsets =[
        (None,{'fields': ['name']}),
        ('information', {'fields': ['title','photoUrl','summary']}),
         ('Album', {'fields': ['Album']}),
            ]

admin.site.register(Album,AlbumAdmin)
admin.site.register(Photo,PhotoAdmin)
