# Generated by Django 4.1.6 on 2023-02-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alvo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alvo',
            name='id',
        ),
        migrations.AlterField(
            model_name='alvo',
            name='identificador',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
