# Generated by Django 2.2.6 on 2019-11-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191128_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='acess',
            field=models.CharField(choices=[('Не разрешать', 'not_allowed'), ('Разрешить просмотр', 'allowed')], default='Не разрешать', max_length=30, verbose_name='Доступ'),
        ),
    ]