# Generated by Django 3.0.7 on 2020-06-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeaStallProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField()),
                ('item_price', models.FloatField()),
                ('item_image', models.ImageField(blank=True, upload_to='D:\\Twinkle\\thinkbridge\\media/')),
            ],
        ),
    ]
