# Generated by Django 3.0.3 on 2020-02-07 02:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_pagarme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagarmePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('boleto', 'Boleto'), ('credit_card', 'Cartão de Crédito')], max_length=11)),
                ('amount', models.PositiveIntegerField(verbose_name='Preço pago em Centavos')),
                ('card_id', models.CharField(max_length=64, null=True)),
                ('card_last_digits', models.CharField(max_length=4, null=True)),
                ('boleto_url', models.TextField(null=True)),
                ('installments', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Parcelas')),
            ],
        ),
        migrations.CreateModel(
            name='PagarmePaymentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_pagarme.PaymentItem')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_pagarme.PagarmePayment')),
            ],
            options={
                'unique_together': {('payment', 'item')},
            },
        ),
        migrations.AddField(
            model_name='pagarmepayment',
            name='items',
            field=models.ManyToManyField(related_name='payments', through='django_pagarme.PagarmePaymentItem', to='django_pagarme.PaymentItem'),
        ),
    ]