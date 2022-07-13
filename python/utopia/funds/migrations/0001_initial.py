# Generated by Django 4.0.5 on 2022-07-13 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fundname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nav', models.DecimalField(decimal_places=4, max_digits=8)),
                ('date', models.DateField()),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.scheme')),
            ],
            options={
                'unique_together': {('scheme_id', 'date')},
            },
        ),
    ]
