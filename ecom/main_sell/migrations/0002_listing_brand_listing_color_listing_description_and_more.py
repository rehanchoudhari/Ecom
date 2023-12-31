# Generated by Django 4.2.1 on 2023-09-16 09:14

from django.db import migrations, models
import django.db.models.deletion
import main_sell.comman_utils


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_alter_profiledetials_profile_pic'),
        ('main_sell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='brand',
            field=models.CharField(choices=[('bmw', 'BMW'), ('mercedes benz', 'Mercedes Benz'), ('audi', 'Audi'), ('subaru', 'Subaru'), ('tesla', 'Tesla'), ('jaguar', 'Jaguar'), ('land rover', 'Land Rover'), ('bentley', 'Bentley'), ('bugatti', 'Bugatti'), ('ferrari', 'Ferrari'), ('lamborghini', 'Lamborghini'), ('honda', 'Honda'), ('toyota', 'Toyota'), ('chevrolet', 'Chevrolet'), ('porsche', 'Porsche')], default=None, max_length=25),
        ),
        migrations.AddField(
            model_name='listing',
            name='color',
            field=models.CharField(default='black', max_length=25),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='engine',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='', upload_to=main_sell.comman_utils.get_listing_image),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.location'),
        ),
        migrations.AddField(
            model_name='listing',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='model',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='transmisson',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='vin',
            field=models.CharField(default='', max_length=17),
            preserve_default=False,
        ),
    ]
