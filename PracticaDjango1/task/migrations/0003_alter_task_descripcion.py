# Generated by Django 4.2.7 on 2023-11-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_descripcion_alter_task_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]
