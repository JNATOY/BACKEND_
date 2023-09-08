# Generated by Django 3.2 on 2023-09-02 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_nom', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'db_table': 'tbl_categoria',
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('mesa_id', models.AutoField(primary_key=True, serialize=False)),
                ('mesa_nro', models.CharField(max_length=10, verbose_name='Nro Mesa')),
            ],
            options={
                'db_table': 'tbl_mesa',
            },
        ),
    ]
