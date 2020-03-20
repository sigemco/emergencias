from django.db import models
from django.conf import settings

#https://medium.com/@h4k1m0u/displaying-a-map-in-a-django-webapp-1-3-creating-a-gis-database-with-postgresql-and-postgis-e596d3c2310
#Tener en cuenta que para los campos de los modelos tomarlos de django.contrib.gis.db

##IMPORTANTE CON GeometryCollectionField: eRROR Eso sucede generalmente con archivos de forma que contienen una mezcla de polígonos y multipolígonos.
# Si inicializa la tabla para polígonos, los multipolígonos se rechazan y viceversa.
# https://gis.stackexchange.com/questions/324703/error-geometry-constraint-geom-type-or-srid-not-allowed-how-to-ensure-the-corr

from django.contrib.gis.db import models as geomodels

# nesesarios para la respuesta del datatables
from django.db.models import Q
# https://django-model-utils.readthedocs.io/en/latest/setup.html -> Descargar esta libreria y no es necesario agregarlas a las app instaladas del setting.py
from model_utils import Choices


class Estado(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='estado')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Estado de {self.user.username}"







    # Funcion q me permite serializar en formato json el queryset que se pasara en data (nombre necesario en datatables)
    # los datos del modelo
    def generar_diccionario_json(self):
        return {
                'id': self.id,
                'nombre': self.nombre,
                'fecha_nacimiento': self.fecha_nacimiento,
                # 'grado': self.grado.objects.all(),
                # 'especialidad': self.especialidad
            }


ORDER_COLUMN_CHOICES = Choices(
    ('0', 'nombre'),
    ('1', 'fecha_nacimiento'),
    # ('2', 'grado'),
    # ('3', 'especialidad'),
)


def query_musics_by_args(usuario, kwargs):

    draw = int(kwargs.get('draw', None))
    length = int(kwargs.get('length', None))
    start = int(kwargs.get('start', None))
    search_value = kwargs.get('search[value]', None)
    order_column = kwargs.get('order[0][column]', None)
    order = kwargs.get('order[0][dir]', None)

    order_column = ORDER_COLUMN_CHOICES[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column
    queryset = []

    '''
    grupos_del_usuario = usuario.groups.all()
    if 'grupoLector' in [str(x) for x in grupos_del_usuario]:
        queryset = Persona.objects.filter(tiene_permitido_leer='SI')
    else:
        queryset = Persona.objects.filter(grupo_creador__in=grupos_del_usuario)
    '''
    queryset = Persona.objects.all()

    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(nombre__icontains=search_value) |
                                   Q(fecha_nacimiento__icontains=search_value) |
                                   Q(grado__icontains=search_value) |
                                   Q(especialidd__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    data = [p.generar_diccionario_json() for p in queryset]
    return {
        'items': data,
        'count': count,
        'total': total,
        'draw': draw
    }

    ####Modelos de la organizacion####
    # como mínumo null=True

### Modelos de todo el sistema sanitario ###

class Unidades(models.Model):
    """Model definition for Unidades."""

    # TODO: Define fields here
    unidad = models.CharField(max_length=50, null=True)

    class Meta:
        """Meta definition for Unidades."""

        verbose_name = 'Unidades'
        verbose_name_plural = 'Unidadess'

    def __str__(self):
        """Unicode representation of Unidades."""
        return self.unidad

class Grado(models.Model):
    grado = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'grado'

    def __str__(self):
        return self.grado

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'especialidad'

    def __str__(self):
        return self.especialidad

class Persona(models.Model):
    nombre = models.CharField(max_length=50, null=False, help_text='Ingresa tu nombre')
    # destino = models.CharField(max_length=20, null=False)
    # documento = models.CharField(max_length=100, null=False)
    # https://stackoverflow.com/questions/5871730/how-to-upload-a-file-in-django
    archivo = models.FileField(upload_to='archivos/%Y/%m/%d')
    # fecha_creacion = models.DateTimeField(auto_now_add=True)
    # fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_nacimiento = models.DateTimeField()
    grado = models.ForeignKey(Grado, on_delete=False)
    especialidad = models.ManyToManyField(Especialidad)
    ubicacion = geomodels.GeometryCollectionField()

    class Meta:
        db_table = 'nombre'

    def __str__(self):
        return self.nombre

class TipOperacion(models.Model):
    """Model definition for Tipo."""
    tipo = models.CharField(max_length=50, null=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Tipo."""

        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        """Unicode representation of Tipo."""
        return self.tipo

class TipoTransporte(models.Model):
    """Model definition for TipoTransporte Terrestre, maritino, etc."""

    # TODO: Define fields here
    tipotransporte = models.CharField(max_length=50, null=True)

    class Meta:
        """Meta definition for TipoTransporte."""

        verbose_name = 'TipoTransporte'
        verbose_name_plural = 'TipoTransportes'

    def __str__(self):
        """Unicode representation of TipoTransporte."""
        return self.tipotransporte

class Medios(models.Model):
    """Model definition for Medios."""

    # TODO: Define fields here
    medio = models.CharField(max_length=50, null=True)

    class Meta:
        """Meta definition for Medios."""

        verbose_name = 'Medios'
        verbose_name_plural = 'Medios'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.medio

class CentroSalud(models.Model):
    """Model definition for CentroSalud."""

    # TODO: Define fields here
    centro = models.CharField(max_length=100, null=True)

    class Meta:
        """Meta definition for CentroSalud."""

        verbose_name = 'CentroSalud'
        verbose_name_plural = 'CentroSaluds'

    def __str__(self):
        """Unicode representation of CentroSalud."""
        return self.centro

class Efectos(models.Model):
    """Model definition for Efectos."""

    # TODO: Define fields here
    efecto = models.CharField(max_length=100, null=True)
    unidad = models.ForeignKey(Unidades, on_delete=False)


    class Meta:
        """Meta definition for Efectos."""

        verbose_name = 'Efectos'
        verbose_name_plural = 'Efectoss'

    def __str__(self):
        """Unicode representation of Efectos."""
        return self.efecto

class OperacionesEnDesarrollo(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    mision = models.CharField(max_length=50, null=True)
    objetivo = models.CharField(max_length=50, null=True)
    tipoperacion = models.ForeignKey(TipOperacion,on_delete=False)
    tipotransporte = models.ManyToManyField(TipoTransporte)
    personal = models.ManyToManyField(Persona)
    centrosalud = models.ManyToManyField(CentroSalud)
    efectos = models.ManyToManyField(Efectos)

    class Meta:
        verbose_name = ("operaciones en desarrollo")
        verbose_name_plural = ("Operaciones en desarrollo")

    def __str__(self):
        return self.operacion


class provincia(models.Model):
    """Model definition for provincia."""

    # TODO: Define fields here
    provincia = models.CharField(max_length=100, null=True, blank=False)

    class Meta:
        """Meta definition for provincia."""
        

        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'

    def __str__(self):
        """Unicode representation of provincia."""
        return self.provincia

class partido(models.Model):
    """Model definition for partido."""

    # TODO: Define fields here
    partido = models.CharField(max_length=100, null=True, blank=False)

    class Meta:
        """Meta definition for partido."""

        verbose_name = 'partido'
        verbose_name_plural = 'partidos'

    def __str__(self):
        """Unicode representation of partido."""
        return partido

class CCZE(models.Model):
    """Model definition for CCZE."""

    # TODO: Define fields here
    denominacion = models.CharField(max_length=100, null=True, blank=False)
    comando = models.CharField(max_length=100, null=True, blank=False) #la unidad de donde depende el CCZE
    respTerrProvincia = models.ManyToManyField(provincia)
    respTerrPartido = models.ForeignKey(partido, on_delete=False)
    ubicacion = geomodels.GeometryCollectionField()

    class Meta:
        """Meta definition for CCZE."""

        verbose_name = 'CCZE'
        verbose_name_plural = 'CCZEs'

    def __str__(self):
        """Unicode representation of CCZE."""
        pass
