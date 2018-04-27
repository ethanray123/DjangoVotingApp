# Generated by Django 2.0.4 on 2018-04-25 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='party_list',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.Position'),
        ),
    ]
