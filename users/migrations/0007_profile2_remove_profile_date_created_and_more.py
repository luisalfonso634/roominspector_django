# Generated by Django 4.0.1 on 2022-01-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_date_created_profile_date_deleted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('bio', models.TextField(blank=True, max_length=200)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_deleted',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='model_state',
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
