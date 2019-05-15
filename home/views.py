from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import HomePost,Friend
from .forms import HomeForm
from post.forms import *
from post.urls import *
from django.urls import reverse

# Create your views here.


def login_redirect(request):
    return redirect('/accounts/login/')

def homeview(request):

    context={
            'isim':'Misafir',
            }
    form = HomeForm()
    posts = post.objects.all()
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except Friend.DoesNotExist:
        friends = None
    users = User.objects.exclude(id=request.user.id)
    args = {
            'form': form, 'posts': posts, 'users': users, 'friends':friends}
        
   
    return render(request,'home.html',args)
def katil_post(request,id):
    post1=post.objects.get(id=id)
    post1.katilimci.add(request.user)
    
    return HttpResponseRedirect(post1.get_absolute_url())

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home')


