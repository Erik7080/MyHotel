# Generated by Django 2.1 on 2019-04-19 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_reservation_dates'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountedPacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_type', models.CharField(max_length=200)),
                ('pack_price_night', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ExtraCategory')),
            ],
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Reservation_dates',
        ),
        migrations.RemoveField(
            model_name='room',
            name='extras',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
