# Generated by Django 2.2.6 on 2019-11-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='branch',
            name='latitude',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='branch',
            name='longitude',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='category',
            name='img_path',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='value',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='course',
            name='logo',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
