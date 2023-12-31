# Generated by Django 4.2.5 on 2023-12-04 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_servicio_calificacion_servicio_empleado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('numero_celular', models.CharField(max_length=15)),
                ('zona_trabajo', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='perfil_empleado/')),
                ('habilidades', models.TextField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='calificacion',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='fecha_agenda',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='fecha_solicitud',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='mensaje_calificacion',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='metodo_pago',
        ),
        migrations.AddField(
            model_name='servicio',
            name='calificacion_cliente',
            field=models.IntegerField(blank=True, choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], null=True),
        ),
        migrations.AddField(
            model_name='servicio',
            name='direccion_servicio',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='servicio',
            name='tipo_pago',
            field=models.CharField(choices=[('efectivo', 'Efectivo'), ('corresponsal_bancario', 'Corresponsal Bancario'), ('debito', 'Tarjeta de Débito'), ('credito', 'Tarjeta de Crédito')], default=250, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='tipo_servicio',
            field=models.CharField(choices=[('limpiar_casa', 'Limpiar mi casa'), ('limpiar_empresa', 'Limpiar mi empresa'), ('cuidado_ninos', 'Cuidado de niños'), ('cuidado_adulto_mayor', 'Cuidado del adulto mayor'), ('empleadas_dias', 'Empleadas por días'), ('empleadas_horas', 'Empleadas por horas'), ('empleadas_internas', 'Empleadas internas')], max_length=50),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='servicio',
            name='empleado_seleccionado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.perfilempleado'),
        ),
    ]
