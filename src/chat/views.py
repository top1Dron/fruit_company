import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from chat import utils, forms


def index(request):
    context = {'last_messages': utils.get_last_chat_messages_for_chat_area()}
    if not request.user.is_authenticated:
        context['login_form'] = forms.LoginForm()
        context['signup_form'] = forms.CustomUserCreationForm()
    context['message_form'] = forms.MessageForm()
    return render(request, 'chat/index.html', context=context)


@require_http_methods(['POST'])
def api_login_user(request):
    errors = {}
    body = json.loads(request.body)
    username = body.get('username')
    password = body.get('password')
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect(reverse('chat:index'))
    else:
        user = utils.get_user_by_username(username)
        
        if user is not None and user.is_active == False:
            errors['invalid'] = 'Пользователь заблокирован!'
        else:
            errors['invalid'] = 'Неверный логин/пароль!'
    return JsonResponse(errors)


@login_required
def api_logout_user(request):
    logout(request)
    return redirect(reverse('chat:index'))


@require_http_methods(['POST'])
def api_signup_user(request):
    body = json.loads(request.body)
    username = body.get('username')
    email = body.get('email')
    first_name = body.get('first_name')
    password1 = body.get('password1')
    password2 = body.get('password2')
    form = forms.CustomUserCreationForm(data={
        'username': username,
        'email': email,
        'first_name': first_name,
        'password1': password1,
        'password2': password2
    })
    if form.is_valid():
        form.save()
        user = authenticate(
            request, 
            username=form.cleaned_data['username'], 
            password=form.cleaned_data['password1'])
        login(request, user)
    return JsonResponse(form.errors)


@login_required
def post_user_message(request):
    context = {'last_messages': utils.get_last_chat_messages_for_chat_area()}
    if request.method == 'POST':
        form = forms.MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
            return redirect(reverse('chat:index'))
        context['message_form'] = form
    return render(request, 'chat/index.html', context=context)
    
