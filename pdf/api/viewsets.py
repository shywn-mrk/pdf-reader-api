from rest_framework import viewsets
from .serialilzers import PDFSerializer
from pdf.models import PDF

class PDFViewset(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
