# Generated by Django 4.2.7 on 2024-03-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=15)),
                ('dis', models.TextField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='service',
        ),
    ]