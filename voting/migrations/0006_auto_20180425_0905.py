# Generated by Django 2.0.4 on 2018-04-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_candidate_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partylist',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
