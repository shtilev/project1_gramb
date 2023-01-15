from django.db import models

# Create your models here.
class feedback(models.Model):
    name = models.CharField('Имя', max_length=70)
    number = models.CharField('Номер телефона', max_length=20)
    summ = models.CharField('Сумма обмена', max_length=10)
    telegram = models.CharField('Никнейм в телеграме', max_length=70)
    message = models.TextField('Коментарий')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'
