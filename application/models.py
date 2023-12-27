from django.db import models

class ImageUpload(models.Model):
    files=models.ImageField(upload_to='images/')
    uploaded_at=models.DateTimeField(auto_now_add=True)



class PdfUpload(models.Model):
    files=models.FileField(upload_to='pdf')
    uploaded_at=models.DateTimeField(auto_now_add=True)


class TextUpload(models.Model):
    text=models.TextField()
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class ExtractedData(models.Model):
    text=models.TextField()
    uploaded_at=models.DateTimeField(auto_now_add=True)
