from django.contrib.postgres.operations import CreateExtension
from django.db import models, migrations
from django.contrib.gis.db import models as gis_models


# Create your models here.
class Migration(migrations.Migration):

    operations = [
        CreateExtension('postgis'),
    ]


class Peak(models.Model):
    coordinates = gis_models.PointField(geography=True)
    altitude = models.IntegerField()
    name = models.CharField(max_length=255, null=True)
