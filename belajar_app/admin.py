from django.contrib import admin

# Register your models here.
from .models import *

class olahtempat(admin.ModelAdmin):
    list_display = ['koordinat', 'provinsi', 'daya']
    search_fields = ['koordinat', 'provinsi']
    list_filter = ['usaha_id']
    list_per_page = 5

admin.site.register(Tempat, olahtempat)
admin.site.register(Usaha)

class videoadmin(admin.ModelAdmin):
    list_display = ['judul', 'gambar', 'publikasi', 'link', 'sumber']
    search_fields = ['judul', 'sumber']
    list_filter = ['jenis_id']
    list_per_page = 5

admin.site.register(Video, videoadmin)
admin.site.register(Jenis)