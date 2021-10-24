from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission,User
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect,redirect

def watsonperm(request,id):
    # user = User.objects.get(id=id)
    # print(user)
    user = User.objects.get(id=id)
    print(user)
    permission = Permission.objects.filter(user__id=id)
    print(permission)
    # user.user_permissions.add(permission)
    return HttpResponse(200)









