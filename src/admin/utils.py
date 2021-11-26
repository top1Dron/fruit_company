import json
import string
from django.db import transaction
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from admin.models import Company, Operation


goods_cost = {
    'apples': 4,
    'bananas': 1,
    'pineapples': 3,
    'peaches': 2,
}
goods_names = {
    'apples': 'яблок',
    'bananas': 'бананов',
    'pineapples': 'ананасов',
    'peaches': 'персиков',
}


def get_company() -> Company:
    company = Company.objects.first()
    if company:
        return company
    return Company.objects.create(
        money_balance=120,
        apples=0,
        bananas=0,
        pineapples=0,
        peaches=0
    )


def get_operation_history() -> str:
    result = ''
    operations = Operation.objects.all()[:20]
    for operation in operations[::-1]:
        result += (operation.execution_date.strftime("%d.%m.%Y %H:%M") + 
            ' - ' + operation.get_status_display() + ': ' + operation.message + '\n')
    return result


@transaction.atomic
def buy_fruits(goods_count: int, goods_code: str) -> tuple[Company, Operation]:
    company = get_company()
    
    if goods_code not in ['apples', 'bananas', 'pineapples', 'peaches']:
        operation = Operation.objects.create(name="buy_undefined", 
            message=f"Возможность закупки неизвестного товара, закупка отменена",
            status='2')
        return company, operation
    
    operation_message = f"Возможность закупки {goods_count} {goods_names[goods_code]}"
    if company.money_balance >= goods_count * goods_cost[goods_code]:
        company.money_balance -= goods_count * goods_cost[goods_code]
        if goods_code == 'apples':
            company.apples += goods_count
        elif goods_code == 'bananas':
            company.bananas += goods_count
        elif goods_code == 'pineapples':
            company.pineapples += goods_count
        elif goods_code == 'peaches':
            company.peaches += goods_count
        company.save()
        operation = Operation.objects.create(name=f"buy_{goods_code}", 
            message=f"{operation_message}. Успешное приобретение {goods_names[goods_code]}, затрачены средства - {goods_count * goods_cost[goods_code]}$",
            status='1')
    else:
        operation = Operation.objects.create(name=f"buy_{goods_code}", 
            message=f"{operation_message}. Недостаточно средств на счету, закупка отменена",
            status='2')
    return company, operation


@transaction.atomic
def sell_fruits(goods_count: int, goods_code: str) -> tuple[Company, Operation]:
    company = get_company()
    
    if goods_code not in ['apples', 'bananas', 'pineapples', 'peaches']:
        operation = Operation.objects.create(name="sell_undefined", 
            message=f"Поступил заказ на неизвестный товар, сделка отменена",
            status='2')
        return company, operation
    
    succesfull_update = False
    operation_message = f"Поступил заказ на {goods_count} {goods_names[goods_code]}"

    if goods_code == 'apples':
        if company.apples >= goods_count:
            company.apples -= goods_count
            succesfull_update = True
    elif goods_code == 'bananas':
        if company.bananas >= goods_count:
            company.bananas -= goods_count
            succesfull_update = True
    elif goods_code == 'pineapples':
        if company.pineapples >= goods_count:
            company.pineapples -= goods_count
            succesfull_update = True
    elif goods_code == 'peaches':
        if company.peaches >= goods_count:
            company.peaches -= goods_count
            succesfull_update = True
    if succesfull_update:
        company.money_balance += goods_count * (goods_cost[goods_code] + 1)
        company.save()
        operation = Operation.objects.create(name=f"sell_{goods_code}", 
            message=f"{operation_message}. Нужное количество в наличии, {goods_names[goods_code]} проданы, на счёт поступило - {goods_count * (goods_cost[goods_code] + 1)}$",
            status='1')
    else:
        operation = Operation.objects.create(name=f"sell_{goods_code}", 
            message=f"{operation_message}. На складе недостаточно {goods_names[goods_code]}, сделка отменена",
            status='2')
    return company, operation


def update_or_create_periodic_task_on_buy_fruit(fruit: str, interval: int, count: int):
    return PeriodicTask.objects.update_or_create(
        name=f'Buy {fruit}',      
        defaults={
            'name':f'Buy {fruit}',
            'interval': IntervalSchedule.objects.get_or_create(
                every=interval, 
                period=IntervalSchedule.SECONDS)[0], 
            'task':f'admin.tasks.buy_{fruit}',
            'kwargs': json.dumps({
                'count': count,
            })
        }
    )


def update_or_create_periodic_task_on_sell_fruit(fruit: str, interval: int, count: int):
    return PeriodicTask.objects.update_or_create(
        name=f'Sell {fruit}',      
        defaults={
            'name':f'Sell {fruit}',
            'interval': IntervalSchedule.objects.get_or_create(
                every=interval, 
                period=IntervalSchedule.SECONDS)[0], 
            'task':f'admin.tasks.sell_{fruit}',
            'kwargs': json.dumps({
                'count': count,
            })
        }
    )


def get_last_operations() -> str:
    result = 'Последние обновления\n'
    operations = Operation.objects.all()[:4]
    for operation in operations[::-1]:
        result += (operation.name + ' ' + operation.execution_date.strftime("%H:%M") + '\n')
    return result




digs = string.digits + string.ascii_letters
 
def int2base(x: int, base: int) -> str:
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1
 
    x *= sign
    digits = []
 
    while x:
        digits.append(digs[x % base])
        x = x // base
 
    if sign < 0:
        digits.append('-')
 
    digits.reverse()
 
    return ''.join(digits)
 
 
def filter_num(number: int) -> bool:
    base16 = int2base(number, 16)
    if ('b' in base16 or
        'c' in base16 or
        'd' in base16 or
        'e' in base16 or
        'f' in base16):
        return False
    return int2base(number, 11) == base16[::-1]
 
def number_range(number, inc):
    res = 1
    for _ in range(1, inc):
        res *= number
    return res