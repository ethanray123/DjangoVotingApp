# Generated by Django 2.0.4 on 2018-04-25 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_auto_20180425_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.PartyList'),
        ),
    ]
