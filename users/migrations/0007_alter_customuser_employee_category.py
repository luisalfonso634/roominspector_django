# Generated by Django 4.0.2 on 2022-03-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_employee_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='employee_category',
            field=models.CharField(choices=[('man', 'manager'), ('sup', 'supervisor'), ('hke', 'house keeping employee')], max_length=10),
        ),
    ]
