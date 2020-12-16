# Generated by Django 3.0.5 on 2020-08-17 12:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('application_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('execution_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status_time', models.DateTimeField(blank=True, null=True)),
                ('status_type', models.CharField(choices=[('START', 'Start'), ('END', 'End')], max_length=128)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Application')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(default='Unknown', max_length=128)),
                ('business_owner', models.CharField(max_length=256)),
                ('application_group_name', models.CharField(max_length=128)),
                ('created_by', models.CharField(max_length=256)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('time_out', models.IntegerField(default=120)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('version', models.CharField(default='Latest', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_in_job', models.IntegerField(default=1)),
                ('dataset_key', models.CharField(blank=True, default=uuid.uuid4, max_length=128, unique=True)),
                ('dataset_name', models.CharField(max_length=128)),
                ('dataset_type', models.CharField(choices=[('INPUT', 'Input'), ('OUTPUT', 'Output'), ('INTERMEDIATE', 'Intermediate'), ('TEMPORARY', 'Temporary'), ('OTHER', 'Other')], default='INPUT', max_length=32)),
                ('query_timeout', models.IntegerField(default=300)),
                ('dataset_access_method', models.CharField(choices=[('TABLE', 'Table'), ('SQL', 'SQL query')], default='TABLE', max_length=32)),
                ('dataset_extraction_sql', models.CharField(blank=True, default=None, max_length=5000, null=True)),
                ('dataset_extraction_table', models.CharField(blank=True, max_length=32, null=True)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('connection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saef.Connection')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Application')),
            ],
        ),
        migrations.CreateModel(
            name='JobSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('execution_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status_time', models.DateTimeField(blank=True, null=True)),
                ('status_type', models.CharField(choices=[('START', 'Start'), ('END', 'End')], default='START', max_length=128)),
                ('application_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.ApplicationSession')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Job')),
            ],
        ),
        migrations.CreateModel(
            name='PostgresConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('host', models.CharField(max_length=300)),
                ('port', models.IntegerField(default=5432)),
                ('connection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saef.Connection')),
            ],
        ),
        migrations.CreateModel(
            name='JobSessionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_type', models.CharField(choices=[('PREPROCESSING', 'Preprocessing'), ('START', 'Start'), ('COMPLETE', 'Complete'), ('INPROGRESS', 'In Progress'), ('ERROR', 'Error'), ('OTHER', 'Other'), ('POSTROCESSING', 'Postprocessing')], default='START', max_length=64)),
                ('description', models.CharField(max_length=2048, null=True)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('job_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.JobSession')),
            ],
            options={
                'ordering': ('create_timestamp',),
            },
        ),
        migrations.CreateModel(
            name='DatasetSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('status_time', models.DateTimeField(blank=True, null=True)),
                ('execution_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Dataset')),
                ('job_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.JobSession')),
            ],
        ),
        migrations.CreateModel(
            name='DatasetProfileOperationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_mode', models.CharField(max_length=16)),
                ('batch_id', models.BigIntegerField()),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='DatasetProfileHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_json', models.CharField(max_length=5000)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Dataset')),
                ('job_session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='saef.JobSession')),
            ],
            options={
                'ordering': ('dataset', 'job_session', 'create_timestamp'),
            },
        ),
        migrations.CreateModel(
            name='DatasetMetadataConstraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constraint_name', models.CharField(default='', max_length=128)),
                ('columns', models.CharField(max_length=1024)),
                ('constraint_type', models.CharField(max_length=128)),
                ('constraint_definition', models.CharField(max_length=5000)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='DatasetMetadataColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=512)),
                ('data_type', models.CharField(max_length=128)),
                ('is_null', models.BooleanField()),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Dataset')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Job'),
        ),
        migrations.AddField(
            model_name='connection',
            name='connection_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saef.ConnectionType'),
        ),
        migrations.CreateModel(
            name='ColumnProfileHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=1024)),
                ('profile_json', models.CharField(max_length=5000)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('column', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='saef.DatasetMetadataColumn')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.Dataset')),
                ('job_session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='saef.JobSession')),
            ],
            options={
                'ordering': ('dataset', 'job_session', 'create_timestamp'),
            },
        ),
        migrations.CreateModel(
            name='ApplicationSessionMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_execution_time', models.DurationField()),
                ('expected_execution_time', models.DurationField()),
                ('status_type', models.CharField(choices=[('SUCCEEDED', 'SUCCEEDED'), ('SUCCEEDED_ISSUE', 'SUCCEEDED_ISSUE'), ('FAILED', 'FAILED')], max_length=128)),
                ('application_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.ApplicationSession')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='application_token',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saef.ApplicationToken'),
        ),
    ]