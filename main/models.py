from django.db import models


class Models(models.Model):
    title = models.CharField('Название', max_length=50)
    cost = models.IntegerField('Цена')
    specification = models.CharField('Описание', max_length=1000)
    picture = models.CharField('Картинка', max_length=999999)

    def __str__(self):
        return self.title




class Users(models.Model):
    ID = models.IntegerField('ID')
    name = models.CharField('Имя', max_length=10000)
    password = models.CharField('Пароль', max_length=99999)
    email = models.CharField('Почта', max_length=100)
    cart = models.CharField('Корзина', max_length=9999)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-ID"]


class DonationPerMonth(models.Model):
    id_donators = models.TextField('ID')
    summ = models.IntegerField('Сумма пожертвований за последний месяц')
    number = models.IntegerField('Месяц')

    def __str__(self):
        return str(self.number)

    class Meta:
        ordering = ["-number"]

