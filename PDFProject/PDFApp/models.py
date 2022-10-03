
from django.db import models

# Create your models here.
class FileModel(models.Model):
    files = models.FileField(upload_to='upload')
    sep_text_number = models.IntegerField(default=0)

class TextFileModel(models.Model):
    texts = models.CharField(max_length=10000)
    sep_text_number = models.IntegerField(default=0)

    # def clean_file(self):
    #     file = self.cleaned_data["files"]

    #     if not file.endswith('pdf'):
    #         raise forms.ValidationError('pdfを登録してください．')

class TextModel(models.Model):
    number = models.IntegerField()
    len_text=models.IntegerField()
    text = models.CharField(max_length = 200)