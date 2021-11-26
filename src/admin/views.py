import json
import logging

from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from admin import utils

logger = logging.getLogger(__name__)


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def index(request):
    company = utils.get_company()
    operation_history = utils.get_operation_history()
    return render(request, 'admin/index.html', context={
        'company': company, 
        'operation_history': operation_history
    })


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def buy_apples(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        apples = int(data.get('count'))
        seconds = int(data.get('seconds'))
        PeriodicTask.objects.filter(name__icontains="Buy apples").delete()
        PeriodicTask.objects.create(
            name=f'Buy apples',
            interval=IntervalSchedule.objects.get_or_create(
                every=seconds, 
                period=IntervalSchedule.SECONDS)[0],
            task='admin.tasks.buy_apples',
            kwargs=json.dumps({
                'count': apples,
            })
        )
    return JsonResponse({})


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def buy_bananas(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bananas = int(data.get('count'))
        seconds = int(data.get('seconds'))
        PeriodicTask.objects.filter(name__icontains="Buy bananas").delete()
        PeriodicTask.objects.create(
            name=f'Buy bananas',
            interval=IntervalSchedule.objects.get_or_create(
                every=seconds, 
                period=IntervalSchedule.SECONDS)[0],
            task='admin.tasks.buy_bananas',
            kwargs=json.dumps({
                'count': bananas,
            })
        )
    return JsonResponse({})


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def buy_pineapples(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pineapples = int(data.get('count'))
        seconds = int(data.get('seconds'))
        PeriodicTask.objects.filter(name__icontains="Buy pineapples").delete()
        PeriodicTask.objects.create(
            name=f'Buy pineapples',
            interval=IntervalSchedule.objects.get_or_create(
                every=seconds, 
                period=IntervalSchedule.SECONDS)[0],
            task='admin.tasks.buy_pineapples',
            kwargs=json.dumps({
                'count': pineapples,
            })
        )
    return JsonResponse({})


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def buy_peaches(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        peaches = int(data.get('count'))
        seconds = int(data.get('seconds'))
        PeriodicTask.objects.filter(name__icontains="Buy peaches").delete()
        PeriodicTask.objects.create(
            name=f'Buy peaches',
            interval=IntervalSchedule.objects.get_or_create(
                every=seconds, 
                period=IntervalSchedule.SECONDS)[0],
            task='admin.tasks.buy_peaches',
            kwargs=json.dumps({
                'count': peaches,
            })
        )
    return JsonResponse({})


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def sell_apples(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        apples = int(data.get('count'))
        seconds = int(data.get('seconds'))
        PeriodicTask.objects.filter(name__icontains="Sell apples").delete()
        PeriodicTask.objects.create(
            name=f'Sell apples',
            interval=IntervalSchedule.objects.get_or_create(
                every=seconds, 
                period=IntervalSchedule.SECONDS)[0],
            task='admin.tasks.sell_apples',
            kwargs=json.dumps({
                'count': apples,
            })
        )
    return JsonResponse({})


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def sell_bananas(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bananas = int(data.get('count'))
        seconds = int(data.get('seconds'))
        PeriodicTask.objects.filter(name__icontains="Sell bananas").delete()
        PeriodicTask.objects.create(
            name=f'Sell bananas',
            interval=IntervalSchedule.objects.get_or_create(
                every=seconds, 
                period=IntervalSchedule.SECONDS)[0],
            task='admin.tasks.sell_bananas',
            kwargs=json.dumps({
                'count': bananas,
            })
        )
    return JsonResponse({})


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def sell_pineapples(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pineapples = int(data.get('count'))
        seconds = int(data.get('seconds'))
        PeriodicTask.objects.filter(name__icontains="Sell pineapples").delete()
        PeriodicTask.objects.create(
            name=f'Sell pineapples',
            interval=IntervalSchedule.objects.get_or_create(
                every=seconds, 
                period=IntervalSchedule.SECONDS)[0],
            task='admin.tasks.sell_pineapples',
            kwargs=json.dumps({
                'count': pineapples,
            })
        )
    return JsonResponse({})


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def sell_peaches(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        peaches = int(data.get('count'))
        seconds = int(data.get('seconds'))
        PeriodicTask.objects.filter(name__icontains="Sell peaches").delete()
        PeriodicTask.objects.create(
            name=f'Sell peaches',
            interval=IntervalSchedule.objects.get_or_create(
                every=seconds, 
                period=IntervalSchedule.SECONDS)[0],
            task='admin.tasks.sell_peaches',
            kwargs=json.dumps({
                'count': peaches,
            })
        )
    return JsonResponse({})


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def add_money(request):
    if request.method == 'POST':
        money = request.POST.get('add_money')
        company = utils.get_company()
        company.money_balance += int(money)
        company.save()
    return redirect(reverse_lazy('admin:index'))


@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('chat:index'))
def take_money(request):
    if request.method == 'POST':
        money = request.POST.get('take_money')
        company = utils.get_company()
        if company.money_balance >= int(money):
            company.money_balance -= int(money)
        company.save()
    return redirect(reverse_lazy('admin:index'))