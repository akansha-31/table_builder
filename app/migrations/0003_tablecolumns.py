# Generated by Django 3.2.8 on 2022-08-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tablerecords'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableColumns',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('column_name', models.CharField(max_length=20)),
                ('column_type', models.CharField(max_length=20)),
                ('is_primary', models.BooleanField()),
                ('nullable', models.BooleanField(default=False)),
            ],
        ),
    ]
