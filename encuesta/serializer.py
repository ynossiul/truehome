from rest_framework import serializers
from encuesta.models import encuesta
# con la funcion modelserializer se muestra todos los campos de model
class encuesta_serializers(serializers.ModelSerializer):
    class Meta:
        model=encuesta
        fields='__all__'

