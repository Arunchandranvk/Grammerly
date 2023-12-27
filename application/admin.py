from django.contrib import admin
from application.models import ImageUpload,PdfUpload,TextUpload,ExtractedData

admin.site.register(ImageUpload)
admin.site.register(PdfUpload)
admin.site.register(TextUpload)
admin.site.register(ExtractedData)
