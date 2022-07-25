# Generated by Django 4.0 on 2022-07-02 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_employer_city_alter_employer_country'),
        ('chatsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatsystem.session')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]
