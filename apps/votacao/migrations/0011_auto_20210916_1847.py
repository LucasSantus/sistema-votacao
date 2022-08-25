# Generated by Django 3.2.7 on 2021-09-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0010_alter_salavotacao_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salavotacao',
            name='codigo',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='salavotacao',
            name='resumo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Resumo'),
        ),
    ]
