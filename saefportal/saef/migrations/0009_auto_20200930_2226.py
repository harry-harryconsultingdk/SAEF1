# Generated by Django 3.0.3 on 2020-09-30 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saef', '0008_auto_20200828_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='dataset_access_method',
            field=models.CharField(choices=[('TABLE', 'TABLE'), ('SQL', 'SQL')], default='TABLE', max_length=32),
        ),
        migrations.CreateModel(
            name='AzureConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('host', models.CharField(max_length=300)),
                ('port', models.IntegerField(default=1433)),
                ('connection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saef.Connection')),
            ],
        ),
    ]
