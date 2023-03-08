# Generated by Django 4.1.7 on 2023-03-08 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=200)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Focs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=200)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MpesaPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Cancelled', 'Cancelled')], default='Paid', max_length=255)),
                ('Currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.currency')),
            ],
        ),
    ]
