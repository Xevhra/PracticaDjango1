# Generated by Django 4.2.7 on 2023-11-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]