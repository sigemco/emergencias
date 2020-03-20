# Generated by Django 2.2.4 on 2020-03-17 23:12

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroSalud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'CentroSalud',
                'verbose_name_plural': 'CentroSaluds',
            },
        ),
        migrations.CreateModel(
            name='Efectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('efecto', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Efectos',
                'verbose_name_plural': 'Efectoss',
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'especialidad',
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grado',
            },
        ),
        migrations.CreateModel(
            name='Medios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medio', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Medios',
                'verbose_name_plural': 'Medios',
            },
        ),
        migrations.CreateModel(
            name='TipOperacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='TipoTransporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipotransporte', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'TipoTransporte',
                'verbose_name_plural': 'TipoTransportes',
            },
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Unidades',
                'verbose_name_plural': 'Unidadess',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingresa tu nombre', max_length=50)),
                ('archivo', models.FileField(upload_to='archivos/%Y/%m/%d')),
                ('fecha_nacimiento', models.DateTimeField()),
                ('ubicacion', django.contrib.gis.db.models.fields.GeometryCollectionField(srid=4326)),
                ('especialidad', models.ManyToManyField(to='emergencias.Especialidad')),
                ('grado', models.ForeignKey(on_delete=False, to='emergencias.Grado')),
            ],
            options={
                'db_table': 'nombre',
            },
        ),
        migrations.CreateModel(
            name='OperacionesEnDesarrollo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('mision', models.CharField(max_length=50, null=True)),
                ('objetivo', models.CharField(max_length=50, null=True)),
                ('centrosalud', models.ManyToManyField(to='emergencias.CentroSalud')),
                ('efectos', models.ManyToManyField(to='emergencias.Efectos')),
                ('personal', models.ManyToManyField(to='emergencias.Persona')),
                ('tipoperacion', models.ForeignKey(on_delete=False, to='emergencias.TipOperacion')),
                ('tipotransporte', models.ManyToManyField(to='emergencias.TipoTransporte')),
            ],
            options={
                'verbose_name': 'operaciones en desarrollo',
                'verbose_name_plural': 'Operaciones en desarrollo',
            },
        ),
        migrations.AddField(
            model_name='efectos',
            name='unidad',
            field=models.ForeignKey(on_delete=False, to='emergencias.Unidades'),
        ),
    ]