# Generated by Django 3.0.3 on 2020-06-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bloggin', '0005_auto_20200602_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('Blog', models.TextField()),
            ],
        ),
    ]
