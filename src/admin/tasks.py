from random import randint
import json

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django_celery_beat.models import IntervalSchedule, PeriodicTask, PeriodicTasks

from admin import utils

channel_layer = get_channel_layer()


@shared_task
def update_last_operations():
    operations = utils.get_last_operations()
    async_to_sync(channel_layer.group_send)('last_operations', {
        'type': 'update_last_operations', 
        'operations': operations,
    })

PeriodicTask.objects.update_or_create(
    name='Update last operations',
    defaults={
        'name': 'Update last operations', 
        'task': f'admin.tasks.update_last_operations',
        'interval': IntervalSchedule.objects.get_or_create(
            every=10, 
            period=IntervalSchedule.SECONDS)[0]
    }
)


@shared_task
def buy_apples(count: int):
    company, operation = utils.buy_fruits(count, 'apples')
    utils.update_or_create_periodic_task_on_buy_fruit(
        fruit='apples', 
        interval=6, 
        count=randint(1, 10))
    async_to_sync(channel_layer.group_send)('fruits', {
        'type': 'update_apples', 
        'money': company.money_balance,
        'apples': company.apples,
        'operation': (operation.execution_date.strftime("%d.%m.%Y %H:%M") + 
            ' - ' + operation.get_status_display() + ': ' + operation.message + '\n')
    })

@shared_task
def buy_bananas(count: int):
    company, operation = utils.buy_fruits(count, 'bananas')
    utils.update_or_create_periodic_task_on_buy_fruit(
        fruit='bananas', 
        interval=9, 
        count=randint(10, 20))
    async_to_sync(channel_layer.group_send)('fruits', {
        'type': 'update_bananas', 
        'money': company.money_balance,
        'bananas': company.bananas,
        'operation': (operation.execution_date.strftime("%d.%m.%Y %H:%M") + 
            ' - ' + operation.get_status_display() + ': ' + operation.message + '\n')
    })


@shared_task
def buy_pineapples(count: int):
    company, operation = utils.buy_fruits(count, 'pineapples')
    utils.update_or_create_periodic_task_on_buy_fruit(
        fruit='pineapples', 
        interval=12, 
        count=randint(1, 10))
    async_to_sync(channel_layer.group_send)('fruits', {
        'type': 'update_pineapples', 
        'money': company.money_balance,
        'pineapples': company.pineapples,
        'operation': (operation.execution_date.strftime("%d.%m.%Y %H:%M") + 
            ' - ' + operation.get_status_display() + ': ' + operation.message + '\n')
    })


@shared_task
def buy_peaches(count: int):
    company, operation = utils.buy_fruits(count, 'peaches')
    utils.update_or_create_periodic_task_on_buy_fruit(
        fruit='peaches', 
        interval=15, 
        count=randint(5, 15))
    async_to_sync(channel_layer.group_send)('fruits', {
        'type': 'update_peaches', 
        'money': company.money_balance,
        'peaches': company.peaches,
        'operation': (operation.execution_date.strftime("%d.%m.%Y %H:%M") + 
            ' - ' + operation.get_status_display() + ': ' + operation.message + '\n')
    })

utils.update_or_create_periodic_task_on_buy_fruit(
    fruit='apples', 
    interval=6, 
    count=randint(1, 10))

utils.update_or_create_periodic_task_on_buy_fruit(
    fruit='bananas', 
    interval=9, 
    count=randint(10, 20))

utils.update_or_create_periodic_task_on_buy_fruit(
    fruit='pineapples', 
    interval=12, 
    count=randint(1, 10))

utils.update_or_create_periodic_task_on_buy_fruit(
    fruit='peaches', 
    interval=15, 
    count=randint(5, 15))


@shared_task
def sell_apples(count: int):
    company, operation = utils.sell_fruits(count, 'apples')
    utils.update_or_create_periodic_task_on_sell_fruit(
        fruit='apples', 
        interval=15, 
        count=randint(1, 10))
    async_to_sync(channel_layer.group_send)('fruits', {
        'type': 'update_apples', 
        'money': company.money_balance,
        'apples': company.apples,
        'operation': (operation.execution_date.strftime("%d.%m.%Y %H:%M") + 
            ' - ' + operation.get_status_display() + ': ' + operation.message + '\n')
    })

@shared_task
def sell_bananas(count: int):
    company, operation = utils.sell_fruits(count, 'bananas')
    utils.update_or_create_periodic_task_on_sell_fruit(
        fruit='bananas', 
        interval=12, 
        count=randint(1, 30))
    async_to_sync(channel_layer.group_send)('fruits', {
        'type': 'update_bananas', 
        'money': company.money_balance,
        'bananas': company.bananas,
        'operation': (operation.execution_date.strftime("%d.%m.%Y %H:%M") + 
            ' - ' + operation.get_status_display() + ': ' + operation.message + '\n')
    })


@shared_task
def sell_pineapples(count: int):
    company, operation = utils.sell_fruits(count, 'pineapples')
    utils.update_or_create_periodic_task_on_sell_fruit(
        fruit='pineapples', 
        interval=9, 
        count=randint(1, 10))
    async_to_sync(channel_layer.group_send)('fruits', {
        'type': 'update_pineapples', 
        'money': company.money_balance,
        'pineapples': company.pineapples,
        'operation': (operation.execution_date.strftime("%d.%m.%Y %H:%M") + 
            ' - ' + operation.get_status_display() + ': ' + operation.message + '\n')
    })


@shared_task
def sell_peaches(count: int):
    company, operation = utils.sell_fruits(count, 'peaches')
    utils.update_or_create_periodic_task_on_sell_fruit(
        fruit='peaches', 
        interval=6, 
        count=randint(1, 20))
    async_to_sync(channel_layer.group_send)('fruits', {
        'type': 'update_peaches', 
        'money': company.money_balance,
        'peaches': company.peaches,
        'operation': (operation.execution_date.strftime("%d.%m.%Y %H:%M") + 
            ' - ' + operation.get_status_display() + ': ' + operation.message + '\n')
    })


utils.update_or_create_periodic_task_on_sell_fruit(
    fruit='apples', 
    interval=15, 
    count=randint(1, 10))

utils.update_or_create_periodic_task_on_sell_fruit(
    fruit='bananas', 
    interval=12, 
    count=randint(1, 30))

utils.update_or_create_periodic_task_on_sell_fruit(
    fruit='pineapples', 
    interval=9, 
    count=randint(1, 10))

utils.update_or_create_periodic_task_on_sell_fruit(
    fruit='peaches', 
    interval=6, 
    count=randint(1, 20))


@shared_task
def checking_storage():
    result = [i for i in range(utils.number_range(2, 1), utils.number_range(2, 21)+1) if utils.filter_num(i)]