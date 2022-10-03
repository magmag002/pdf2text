
from django import forms
from .models import FileModel,TextFileModel

class UserInfo(forms.Form):
    name=forms.CharField()

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = '__all__'

class UploadTextForm(forms.ModelForm):
    texts = forms.CharField(
        widget = forms.Textarea(attrs={'row':30,'col':20})
    )

    class Meta:
        model = TextFileModel
        fields = '__all__'