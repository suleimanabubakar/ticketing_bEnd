# Generated by Django 4.1.7 on 2023-03-08 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounting', '0002_initial'),
        ('payment', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='sale',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sales.sale'),
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
        migrations.AddField(
            model_name='focs',
            name='authorized_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='focs',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
        migrations.AddField(
            model_name='discounts',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
        migrations.AddField(
            model_name='cashpayment',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.currency'),
        ),
        migrations.AddField(
            model_name='cashpayment',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
    ]
