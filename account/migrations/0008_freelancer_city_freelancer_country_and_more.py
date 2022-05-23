# Generated by Django 4.0 on 2022-05-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_freelancer'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='country',
            field=models.CharField(max_length=100, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='current_job',
            field=models.CharField(max_length=100, null=True, verbose_name='Current Job'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='education',
            field=models.CharField(max_length=30, null=True, verbose_name='Education'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='language',
            field=models.CharField(max_length=30, null=True, verbose_name='Language'),
        ),
    ]
