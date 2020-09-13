# Generated by Django 3.0.7 on 2020-09-13 18:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    from django.conf import settings

    dependencies = [
        ('automated_logging', '0017_auto_20200819_1004'),
    ]

    if hasattr(settings, 'AUTOMATED_LOGGING_DEV') and settings.AUTOMATED_LOGGING_DEV:
        operations = [
            migrations.CreateModel(
                name='DecoratorOverrideExclusionTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    ('random', models.CharField(max_length=255, null=True)),
                    ('random2', models.CharField(max_length=255, null=True)),
                ],
            ),
            migrations.CreateModel(
                name='FullClassBasedExclusionTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    ('random', models.CharField(max_length=255, null=True)),
                    ('random2', models.CharField(max_length=255, null=True)),
                ],
            ),
            migrations.CreateModel(
                name='FullDecoratorBasedExclusionTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    ('random', models.CharField(max_length=255, null=True)),
                    ('random2', models.CharField(max_length=255, null=True)),
                ],
            ),
            migrations.CreateModel(
                name='OrdinaryTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    ('random', models.CharField(max_length=255, null=True)),
                    ('random2', models.CharField(max_length=255, null=True)),
                ],
            ),
            migrations.CreateModel(
                name='PartialClassBasedExclusionTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    ('random', models.CharField(max_length=255, null=True)),
                    ('random2', models.CharField(max_length=255, null=True)),
                ],
            ),
            migrations.CreateModel(
                name='PartialDecoratorBasedExclusionTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    ('random', models.CharField(max_length=255, null=True)),
                    ('random2', models.CharField(max_length=255, null=True)),
                ],
            ),
            migrations.CreateModel(
                name='SpeedTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    ('column0', models.CharField(max_length=15, null=True)),
                    ('column1', models.CharField(max_length=15, null=True)),
                    ('column2', models.CharField(max_length=15, null=True)),
                    ('column3', models.CharField(max_length=15, null=True)),
                    ('column4', models.CharField(max_length=15, null=True)),
                    ('column5', models.CharField(max_length=15, null=True)),
                    ('column6', models.CharField(max_length=15, null=True)),
                    ('column7', models.CharField(max_length=15, null=True)),
                    ('column8', models.CharField(max_length=15, null=True)),
                    ('column9', models.CharField(max_length=15, null=True)),
                    ('column10', models.CharField(max_length=15, null=True)),
                    ('column11', models.CharField(max_length=15, null=True)),
                    ('column12', models.CharField(max_length=15, null=True)),
                    ('column13', models.CharField(max_length=15, null=True)),
                    ('column14', models.CharField(max_length=15, null=True)),
                    ('column15', models.CharField(max_length=15, null=True)),
                    ('column16', models.CharField(max_length=15, null=True)),
                    ('column17', models.CharField(max_length=15, null=True)),
                    ('column18', models.CharField(max_length=15, null=True)),
                    ('column19', models.CharField(max_length=15, null=True)),
                    ('column20', models.CharField(max_length=15, null=True)),
                    ('column21', models.CharField(max_length=15, null=True)),
                    ('column22', models.CharField(max_length=15, null=True)),
                    ('column23', models.CharField(max_length=15, null=True)),
                    ('column24', models.CharField(max_length=15, null=True)),
                    ('column25', models.CharField(max_length=15, null=True)),
                    ('column26', models.CharField(max_length=15, null=True)),
                    ('column27', models.CharField(max_length=15, null=True)),
                    ('column28', models.CharField(max_length=15, null=True)),
                    ('column29', models.CharField(max_length=15, null=True)),
                    ('column30', models.CharField(max_length=15, null=True)),
                    ('column31', models.CharField(max_length=15, null=True)),
                    ('column32', models.CharField(max_length=15, null=True)),
                    ('column33', models.CharField(max_length=15, null=True)),
                    ('column34', models.CharField(max_length=15, null=True)),
                    ('column35', models.CharField(max_length=15, null=True)),
                    ('column36', models.CharField(max_length=15, null=True)),
                    ('column37', models.CharField(max_length=15, null=True)),
                    ('column38', models.CharField(max_length=15, null=True)),
                    ('column39', models.CharField(max_length=15, null=True)),
                    ('column40', models.CharField(max_length=15, null=True)),
                    ('column41', models.CharField(max_length=15, null=True)),
                    ('column42', models.CharField(max_length=15, null=True)),
                    ('column43', models.CharField(max_length=15, null=True)),
                    ('column44', models.CharField(max_length=15, null=True)),
                    ('column45', models.CharField(max_length=15, null=True)),
                    ('column46', models.CharField(max_length=15, null=True)),
                    ('column47', models.CharField(max_length=15, null=True)),
                    ('column48', models.CharField(max_length=15, null=True)),
                    ('column49', models.CharField(max_length=15, null=True)),
                    ('column50', models.CharField(max_length=15, null=True)),
                    ('column51', models.CharField(max_length=15, null=True)),
                    ('column52', models.CharField(max_length=15, null=True)),
                    ('column53', models.CharField(max_length=15, null=True)),
                    ('column54', models.CharField(max_length=15, null=True)),
                    ('column55', models.CharField(max_length=15, null=True)),
                    ('column56', models.CharField(max_length=15, null=True)),
                    ('column57', models.CharField(max_length=15, null=True)),
                    ('column58', models.CharField(max_length=15, null=True)),
                    ('column59', models.CharField(max_length=15, null=True)),
                    ('column60', models.CharField(max_length=15, null=True)),
                    ('column61', models.CharField(max_length=15, null=True)),
                    ('column62', models.CharField(max_length=15, null=True)),
                    ('column63', models.CharField(max_length=15, null=True)),
                    ('column64', models.CharField(max_length=15, null=True)),
                    ('column65', models.CharField(max_length=15, null=True)),
                    ('column66', models.CharField(max_length=15, null=True)),
                    ('column67', models.CharField(max_length=15, null=True)),
                    ('column68', models.CharField(max_length=15, null=True)),
                    ('column69', models.CharField(max_length=15, null=True)),
                    ('column70', models.CharField(max_length=15, null=True)),
                    ('column71', models.CharField(max_length=15, null=True)),
                    ('column72', models.CharField(max_length=15, null=True)),
                    ('column73', models.CharField(max_length=15, null=True)),
                    ('column74', models.CharField(max_length=15, null=True)),
                    ('column75', models.CharField(max_length=15, null=True)),
                    ('column76', models.CharField(max_length=15, null=True)),
                    ('column77', models.CharField(max_length=15, null=True)),
                    ('column78', models.CharField(max_length=15, null=True)),
                    ('column79', models.CharField(max_length=15, null=True)),
                    ('column80', models.CharField(max_length=15, null=True)),
                    ('column81', models.CharField(max_length=15, null=True)),
                    ('column82', models.CharField(max_length=15, null=True)),
                    ('column83', models.CharField(max_length=15, null=True)),
                    ('column84', models.CharField(max_length=15, null=True)),
                    ('column85', models.CharField(max_length=15, null=True)),
                    ('column86', models.CharField(max_length=15, null=True)),
                    ('column87', models.CharField(max_length=15, null=True)),
                    ('column88', models.CharField(max_length=15, null=True)),
                    ('column89', models.CharField(max_length=15, null=True)),
                    ('column90', models.CharField(max_length=15, null=True)),
                    ('column91', models.CharField(max_length=15, null=True)),
                    ('column92', models.CharField(max_length=15, null=True)),
                    ('column93', models.CharField(max_length=15, null=True)),
                    ('column94', models.CharField(max_length=15, null=True)),
                    ('column95', models.CharField(max_length=15, null=True)),
                    ('column96', models.CharField(max_length=15, null=True)),
                    ('column97', models.CharField(max_length=15, null=True)),
                    ('column98', models.CharField(max_length=15, null=True)),
                    ('column99', models.CharField(max_length=15, null=True)),
                ],
            ),
            migrations.CreateModel(
                name='OneToOneTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    (
                        'relationship',
                        models.OneToOneField(
                            null=True,
                            on_delete=django.db.models.deletion.CASCADE,
                            to='automated_logging.OrdinaryTest',
                        ),
                    ),
                ],
            ),
            migrations.CreateModel(
                name='M2MTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    (
                        'relationship',
                        models.ManyToManyField(to='automated_logging.OrdinaryTest'),
                    ),
                ],
            ),
            migrations.CreateModel(
                name='ForeignKeyTest',
                fields=[
                    (
                        'id',
                        models.UUIDField(
                            default=uuid.uuid4, primary_key=True, serialize=False
                        ),
                    ),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                    (
                        'relationship',
                        models.ForeignKey(
                            null=True,
                            on_delete=django.db.models.deletion.CASCADE,
                            to='automated_logging.OrdinaryTest',
                        ),
                    ),
                ],
            ),
        ]

    else:
        operations = []
