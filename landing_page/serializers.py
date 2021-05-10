from rest_framework import serializers
from .models import Post

#un serializer è utilizzato per trasformare i dati in output dei moduli in file JSON leggibili e utilizzabili all'interno di URL
#il framework django ha a disposizione dei serializzatori built-in 

class post_serializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'author', 'body', 'created', 'updated',)
