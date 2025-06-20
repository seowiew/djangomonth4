# Generated by Django 5.2.1 on 2025-05-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_reviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.CharField(max_length=100, verbose_name='Режиссёр'),
        ),
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.IntegerField(verbose_name='Длительность (минуты)'),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(upload_to='films/', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='film',
            name='trailer_url',
            field=models.URLField(verbose_name='Ссылка на трейлер'),
        ),
    ]
