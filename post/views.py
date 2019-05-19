from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import post,Katilim
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms

def post_katilim(request):
    katilimcilar=Katilim.objects.filter(post=post).order_by('-id')
    args={
        'katilimcilar':katilimcilar,
        }
    return render(request,'post/katilim.html',args)
def post_detay(request,id):
    posta=post.objects.get(id=id)
    katilimcilar=posta.katilimci.all()
    users = User.objects.exclude(id=request.user.id)
    return render(request,'post/detay.html',{'posta':posta,'users':users,'katilimcilar':katilimcilar})
def post_detail(request,id):
    
     
    posta=post.objects.get(id=id)
    katilimcilar=posta.katilimci.all()
    users = User.objects.exclude(id=request.user.id)
    return render(request,'post/detail.html',{'posta':posta,'users':users,'katilimcilar':katilimcilar})
def post_index(request):
     users = User.objects.exclude(id=request.user.id)
     posts=post.objects.all()
     args = {
             'posts': posts, 'users': users, 
        }
   
     return render(request,'post/index.html',args)
def post_create(request):

    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('home')
   
    context={
        'form':form,
        }
    return render(request,'post/form.html',context)

    
def post_delete(request,id):
    posta=post.objects.get(id=id)
    posta.delete()
    return redirect('home')

def post_update(request,id):
    posta=post.objects.get(id=id)
    form=PostForm(request.POST or None,request.FILES or None,instance=posta)
    if form.is_valid():
        posta = form.save(commit=False)
        posta.user = request.user
        posta.save()
        return redirect('home')
   
    context={
        'form':form,
        }
    return render(request,'post/form.html',context)
    return()
    


