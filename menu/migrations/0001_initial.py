# Generated by Django 5.0.2 on 2024-03-03 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('menu_name', models.CharField(max_length=255, verbose_name='Название меню')),
                ('position', models.IntegerField(blank=True, null=True, verbose_name='Позиция')),
                ('left', models.IntegerField(blank=True, null=True)),
                ('right', models.IntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menuitem', verbose_name='Родитель')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
