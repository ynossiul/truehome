# Generated by Django 4.0 on 2021-12-30 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('propiedad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Activo', 'Activo'), ('Cancelado', 'Cancelada'), ('Realizado', 'Realizada')], default='Activo', max_length=35)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.propiedad')),
            ],
        ),
    ]
