# Generated by Django 5.0 on 2023-12-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('Check review', 'Check review'), ('Planed treatment', 'Planed treatment'), ('Teeth cleaning', 'Teeth cleaning')], default='Doctor care', max_length=50),
        ),
    ]
