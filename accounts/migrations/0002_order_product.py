# Generated by Django 3.0.5 on 2020-04-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out of stock', 'Out of stock'), ('Delivered', 'Delivered')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(null=True)),
                ('description', models.TextField(max_length=100, null=True)),
                ('category', models.DateTimeField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
