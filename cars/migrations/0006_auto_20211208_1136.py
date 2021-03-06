# Generated by Django 3.2.9 on 2021-12-08 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_merge_0002_alter_image_link_0004_alter_car_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='link',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterModelTable(
            name='car',
            table='cars_car',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('rating', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
