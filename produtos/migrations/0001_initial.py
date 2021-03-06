# Generated by Django 3.0.2 on 2020-01-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marca', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('Eletronico', 'ELETRONICO'), ('Automotivo', 'AUTOMOTIVO')], max_length=100)),
                ('descricao', models.TextField()),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]
