# Generated by Django 2.2.6 on 2019-11-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(default='....', max_length=300, verbose_name='Расскажите о себе'),
        ),
        migrations.AddField(
            model_name='profile',
            name='exp',
            field=models.CharField(choices=[('junior', 'До года'), ('middle', 'От года до трёх лет'), ('senior', 'Больше трех лет')], default='До года', max_length=30, verbose_name='Опыт'),
        ),
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(choices=[('actor', 'Актер'), ('creator', 'Режиссер'), ('cameraman', 'Оператор'), ('editor', 'Монтажер')], default='Актер', max_length=30, verbose_name='Специализация'),
        ),
        migrations.AddField(
            model_name='profile',
            name='portfoils_site',
            field=models.URLField(blank=True, verbose_name='Ссылка на портфолио/личную страницу'),
        ),
        migrations.AddField(
            model_name='profile',
            name='price',
            field=models.TextField(default='.../час работы', max_length=15, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='profile',
            name='ready',
            field=models.BooleanField(default=True, verbose_name='Вы готовы работать за идею в некомерческом проекте?'),
        ),
    ]
