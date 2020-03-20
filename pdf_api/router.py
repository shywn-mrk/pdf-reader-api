from rest_framework import routers
from pdf.api.viewsets import PDFViewset

router = routers.DefaultRouter()

router.register('pdf', viewset=PDFViewset, basename='pdf')
