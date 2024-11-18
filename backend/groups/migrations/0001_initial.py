# Generated by Django 5.1.3 on 2024-11-18 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255, verbose_name='Номер группы')),
                ('name', models.CharField(max_length=255, verbose_name='Название группы')),
                ('documentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentation.documentation', verbose_name='Документация')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]
