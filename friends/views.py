from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from .models import *
from django.urls import reverse
from .randomname import UniqueNameGenerator
# Create your views here.
def friend(request):
    
    friends=request.user.boss.all()
    
    if request.method=="POST":
        target_username = request.POST.get('target_username')
        return redirect(reverse('request_send', args=[target_username]))
    target=request.GET.get('target')
    if target==None:
        return render(request,'friend.html',{
        'target':None,
        'friends':friends
        })
    user=User.objects.get(username=target)
    
        
    return render(request,'friend.html',{
        'target':user,
        'friends':friends
    })
def request_send(request,username):
    
    user=User.objects.get(username=username)
    
    curr_user=request.user
    
    friend_request=FriendRequest(sender=curr_user,receipient=user)
    friend_request.save()
    return render(request,'confirm_request.html')
def view_request(request):
    if request.method=="POST":
        if "decline" in request.POST:
            sender=User.objects.get(username=request.POST.get('sender'))
            frequest=FriendRequest.objects.get(sender=sender,receipient=request.user)
            frequest.declined=True
            frequest.delete()
        elif "accept" in request.POST:
            sender=User.objects.get(username=request.POST.get('sender'))
            frequest=FriendRequest.objects.get(sender=sender,receipient=request.user)
            frequest.accepted=True
            name_generator = UniqueNameGenerator()
            groupname=name_generator.generate_unique_random_name()
            friends_now=Friendship(user=request.user,friend=sender,groupname=groupname)
            friends_then=Friendship(user=sender,friend=request.user,groupname=groupname)
            friends_now.save()
            friends_then.save()
            
    curr_user=request.user
    frequest=FriendRequest.objects.filter(receipient=curr_user)
    return render(request,'friendrequests.html',{
        'requests':frequest
    })