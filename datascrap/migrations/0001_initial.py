# Generated by Django 4.0.6 on 2022-10-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitrage_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_date', models.DateField()),
                ('today_time', models.TimeField()),
                ('matchtime', models.TextField()),
                ('sports_name', models.TextField()),
                ('team1_name', models.TextField()),
                ('team2_name', models.TextField()),
                ('team1_odds', models.TextField(default=None, null=True)),
                ('team2_odds', models.TextField(default=None, null=True)),
                ('stake1', models.DecimalField(decimal_places=2, max_digits=15)),
                ('stake2', models.DecimalField(decimal_places=2, max_digits=15)),
                ('profit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('profitper', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'verbose_name_plural': 'arbitrage_master',
                'db_table': 'arbitrage_master',
            },
        ),
        migrations.CreateModel(
            name='Proxy_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy_ip', models.CharField(default=None, max_length=150, null=True, unique=True)),
                ('proxy_url', models.TextField(default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'proxy_master',
                'db_table': 'proxy_master',
            },
        ),
        migrations.CreateModel(
            name='Match_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leauge_id', models.IntegerField()),
                ('date', models.TextField()),
                ('Leauge_name', models.TextField()),
                ('sports_name', models.TextField()),
                ('team1_name', models.TextField()),
                ('team2_name', models.TextField()),
                ('team1_id', models.IntegerField(default=None, null=True)),
                ('team2_id', models.IntegerField(default=None, null=True)),
                ('team1_odds', models.TextField(default=None, null=True)),
                ('team2_odds', models.TextField(default=None, null=True)),
                ('draw_odds', models.TextField(default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'match_master',
                'db_table': 'match_master',
                'unique_together': {('date', 'Leauge_name', 'sports_name', 'team1_name', 'team2_name', 'team1_id', 'team2_id')},
            },
        ),
    ]
