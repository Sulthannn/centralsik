from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Berhasil Dibuat!")
            return redirect('register')
        else:
            messages.error(request, "Gagal Dibuat!")
            return redirect('register')
    else:
        form = UserCreationForm()
        data = {
            'form':form,
        }
    return render(request, 'register.html', data)


def index(request):
    berita =  Video.objects.all()
    data = {
        'berita' : berita,
    }
    return render(request, 'index.html', data)


def rekomendasi(request):
    map = Tempat.objects.all()
    data = {
        'map' : map,
    }
    return render(request, 'rekomendasi.html', data)


def contact(request):
    data = {
        'Title' : "CENTRAL SIK",
   
    }
    return render(request, 'contact.html', data)


@login_required(login_url=settings.LOGIN_URL)
def central(request):
    map = Tempat.objects.all()
    berita =  Video.objects.all()
    data = {
        'map' : map,
        'berita' : berita,
    }
    return render(request, 'central.html', data)


@login_required(login_url=settings.LOGIN_URL)
def datarekomendasi(request):
    if request.POST:
        form = FormTempat(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormTempat()
            map = Tempat.objects.all()
            data = {
            'map' : map,
            'form'  : form,
            }
            return render(request, 'datarekomendasi.html', data)
    else:
        form = FormTempat()
        map = Tempat.objects.all()
        data = {
           'map' : map,
           'form'  : form,
        }
    return render(request, 'datarekomendasi.html', data)


@login_required(login_url=settings.LOGIN_URL)
def updaterekomendasi(request, id):
    ubahmap = Tempat.objects.get(pk=id)
    if request.POST:
        form = FormTempat(request.POST, instance=ubahmap)
        if form.is_valid():
            form.save()
            data = {
                'tempat' : ubahmap,
                'form'  : form,
            }
            return render(request, 'updaterekomendasi.html', data)
    else:
        form = FormTempat(instance=ubahmap)
        data = {
        'tempat' : ubahmap,
        'form'  : form,
        }
    return render(request, 'updaterekomendasi.html', data)


@login_required(login_url=settings.LOGIN_URL) 
def deleterekomendasi(request, id):
    tempat = Tempat.objects.get(pk=id)
    tempat.delete()
    
    return redirect("/central/")


@login_required(login_url=settings.LOGIN_URL)
def datavideo(request):
    if request.POST:
        form = FormVideo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormVideo()
            berita = Video.objects.all()
            data = {
            'berita' : berita,
            'form'  : form,
            }
            return render(request, 'datavideo.html', data)
    else:
        form = FormVideo()
        berita = Video.objects.all()
        data = {
           'berita' : berita,
           'form'  : form,
        }
    return render(request, 'datavideo.html', data)


@login_required(login_url=settings.LOGIN_URL)
def updatevideo(request, bn):
    ubahvideo = Video.objects.get(pk=bn)
    if request.POST:
        if request.FILES:
            ubahvideo.gambar.delete()
        form = FormVideo(request.POST, request.FILES, instance=ubahvideo)
        if form.is_valid():
            form.save()
            data = {  
                'video' : ubahvideo,
                'form'  : form,
            }
            return render(request, 'updatevideo.html', data)
    else:
        form = FormVideo(instance=ubahvideo)
        data = {
        'video' : ubahvideo,
        'form'  : form,
        }
    return render(request, 'updatevideo.html', data)


@login_required(login_url=settings.LOGIN_URL) 
def deletevideo(request, bn):
    video = Video.objects.get(pk=bn)
    video.gambar.delete()
    video.delete()
    
    return redirect("/central/")





