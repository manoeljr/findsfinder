# Generated by Django 3.2.5 on 2021-07-08 23:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FundoImobiliario',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=8)),
                ('setor', models.CharField(choices=[('hospital', 'Hospital'), ('hotel', 'Hotel'), ('hibrido', 'Híbrido'), ('lajes_corporativas', 'Lajes Corporativas'), ('logistica', 'Logística'), ('outros', 'Outros'), ('residencial', 'Residencial'), ('titulos_valores_mobiliarios', 'Títulos e Val. Mob.')], max_length=30)),
                ('dividend_yield_medio_12m', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vacancia_financeira', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vacancia_fisica', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade_ativos', models.IntegerField(default=0)),
            ],
        ),
    ]
