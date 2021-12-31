from django.db import models
from rest_framework import fields, serializers
from propiedad.models import propiedad
# con la funcion modelserializer se muestra todos los campos de model
class Propiedad_serializers(serializers.ModelSerializer):
    class Meta:
        model=propiedad
        fields='__all__'
    
   
    