# Generated by Django 4.1 on 2022-08-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Coder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
