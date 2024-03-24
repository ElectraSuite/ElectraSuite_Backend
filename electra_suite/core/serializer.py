from rest_framework import serializers

# import model from models.py
from .models import ParamModel

# Create a model serializer
class ParamSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = ParamModel
		fields = ('title', 'description')
