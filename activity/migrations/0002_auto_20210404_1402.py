# Generated by Django 3.1.7 on 2021-04-04 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_item'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item'),
        ),
    ]
