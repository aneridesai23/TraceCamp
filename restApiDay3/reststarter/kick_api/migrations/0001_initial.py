# Generated by Django 2.1.4 on 2018-12-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kickstarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backers_count', models.IntegerField()),
                ('blurb', models.TextField()),
            ],
        ),
    ]
