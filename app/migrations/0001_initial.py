# Generated by Django 2.1.2 on 2018-12-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sosul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('ko_title', models.CharField(max_length=50)),
                ('update_count', models.IntegerField(max_length=10)),
                ('data_path', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('keyword', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]