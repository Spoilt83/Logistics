# Generated by Django 5.0.2 on 2024-02-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='package',
            name='destination',
            field=models.CharField(max_length=100, verbose_name='Destino'),
        ),
        migrations.AlterField(
            model_name='package',
            name='dimensions',
            field=models.CharField(max_length=100, verbose_name='Dimensiones'),
        ),
        migrations.AlterField(
            model_name='package',
            name='origin',
            field=models.CharField(max_length=100, verbose_name='Origen'),
        ),
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.CharField(max_length=100, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='package',
            name='weight',
            field=models.FloatField(verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='transportist',
            name='contact_number',
            field=models.CharField(max_length=10, verbose_name='Teléfono de contacto'),
        ),
        migrations.AlterField(
            model_name='transportist',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='transportist',
            name='vihicle_type',
            field=models.CharField(max_length=100, verbose_name='Tipo de vehículo'),
        ),
    ]
