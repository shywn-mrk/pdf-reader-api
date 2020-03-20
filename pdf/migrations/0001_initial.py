# Generated by Django 3.0.4 on 2020-03-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cover', models.ImageField(upload_to='covers/')),
                ('url', models.FileField(upload_to='files/')),
            ],
        ),
    ]