# Generated by Django 2.1.5 on 2020-04-01 20:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ok', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('real_name', models.CharField(max_length=100)),
                ('tz', models.CharField(default=django.utils.timezone.get_current_timezone_name, max_length=100)),
                ('ok', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='API.Members')),
            ],
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='user_activities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='API.Users'),
        ),
    ]