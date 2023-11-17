# Generated by Django 3.2.6 on 2023-11-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medicines', models.TextField()),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_mob', models.CharField(max_length=15)),
            ],
        ),
    ]
