from django.db import models


class Company(models.Model):
    money_balance = models.PositiveIntegerField()
    apples = models.PositiveIntegerField()
    bananas = models.PositiveIntegerField()
    pineapples = models.PositiveIntegerField()
    peaches = models.PositiveIntegerField()


class Operation(models.Model):
    STATUSES = (
        ('1', 'SUCCESS'),
        ('2', 'ERROR'),
        ('3', 'INFO'),
    )

    name = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    execution_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUSES)

    class Meta:
        ordering = ['-execution_date']