# Generated by Django 2.1.1 on 2018-10-06 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peoples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('p_age', models.IntegerField()),
                ('pgender', models.BooleanField(default=False)),
                ('pcontend', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('pdate', models.DateTimeField()),
                ('pboynum', models.IntegerField()),
                ('pgirlnum', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='peoples',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstApp.Projects'),
        ),
    ]
