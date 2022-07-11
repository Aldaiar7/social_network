from django.shortcuts import render
from django.contrib.auth import get_user_model
from requests import Response
from account.models import Message
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
User = get_user_model()


def index(request):
    users = User.objects.exclude(username=request.user.username)
    print(request.user)
    return render(request, "index.html", context={"users": users})


def chatPage(request, username):
    user_obj = User.objects.filter(username=username).first()
    users = User.objects.exclude(username=request.user.username)
    if user_obj:
        if request.user.is_authenticated:
            if request.user.id > user_obj.id:
                thread_name = f"chat_{request.user.id}-{user_obj.id}"
            else:
                thread_name = f"chat_{user_obj.id}-{request.user.id}"
            message_objs = Message.objects.filter(thread_name=thread_name)
            return render(
                request,
                "main_chat.html",
                context={"user": user_obj, "users": users, "messages": message_objs},
            )
        else:
            return HttpResponse('You didnt logged in.')
    else:
        return Response('There is no user with that name.')

def loginView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account Not Active")
        else:
            context = {'notfound': True}
            print(
                f"NO ACCOUNT FOUND WITH USERNAME {username} AND PASSWORD {password}")
            print(context)
            return render(request, 'login.html', context) 

    else:
        return render(request, 'login.html')
