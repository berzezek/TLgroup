# Generated by Django 3.2.16 on 2022-11-17 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Отдел')),
                ('head_office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.department', verbose_name='Головной отдел')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('job', models.CharField(max_length=200, verbose_name='Должность')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('date_of_issue', models.DateField(verbose_name='Дата принятия на работу')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.department', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Сотрудника',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ('id',),
            },
        ),
    ]
