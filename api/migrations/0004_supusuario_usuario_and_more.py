# Generated by Django 4.2.5 on 2023-10-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alumno_has_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupUsuario',
            fields=[
                ('idSupUsuario', models.IntegerField(db_column='id_SupUsuario', primary_key=True, serialize=False)),
                ('nombreSupUsuario', models.CharField(db_column='nombre_SupUsuario', max_length=100)),
                ('correoSupUsuario', models.CharField(db_column='correo_SupUsuario', max_length=100)),
                ('contraSupUsuario', models.CharField(db_column='contra_SupUsuario', max_length=100)),
            ],
            options={
                'db_table': 'SuperUsuarioTabla',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(db_column='id_Usuario', primary_key=True, serialize=False)),
                ('nombreUsuario', models.CharField(db_column='nombre_Usuario', max_length=100)),
                ('correoUsuario', models.CharField(db_column='correo_Usuario', max_length=100)),
                ('contraUsuario', models.CharField(db_column='contra_Usuario', max_length=100)),
            ],
            options={
                'db_table': 'UsuarioTabla',
            },
        ),
        migrations.RemoveField(
            model_name='alumno_has_genero',
            name='fk_Alumno',
        ),
        migrations.RemoveField(
            model_name='alumno_has_genero',
            name='fk_Genero',
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Alumno_has_Genero',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]