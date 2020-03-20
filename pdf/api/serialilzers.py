from rest_framework import serializers
from pdf.models import PDF

class PDFSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = PDF
        fields = ['id', 'title', 'description', 'cover', 'url']
