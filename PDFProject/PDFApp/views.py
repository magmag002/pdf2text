from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FileModel,TextModel,TextFileModel
from django import forms
from django.forms import formset_factory,modelformset_factory
from django.core.files.storage import FileSystemStorage
from . import forms
import os,re
from PDFApp.views_module import pdf2text

# Create your views here.

def index(request):
    return render(request,'PDFApp/index.html')

def pdf_upload(request):
    name=""
    text=''
    word_cnt=[]
    sep_text_number=0
    #number_list=[]
    FileModel.objects.all().delete()
    TextModel.objects.all().delete()
    #ファイルの削除
    path = "file/upload/"
    files = os.listdir(path)
    if files !=[]:
        for file in files:
            os.remove('file/upload/'+file)

    if request.method=="POST":
        form = forms.UploadFileForm(request.POST,request.FILES)
        name=request.FILES["files"]
        sep_text_number=request.POST["sep_text_number"]
        if form.is_valid():
            form.save()
            text,word_cnt=pdf2text.pdf_to_text("file/upload/"+str(name))
            #number_list=[k for k in range(0,len(word_cnt))]

            for i,tex in enumerate(text):
                TextModel.objects.create(number=i,len_text=word_cnt[i],text=tex)

    else:
        form = forms.UploadFileForm()

    return render(
        request,'PDFApp/pdf_upload.html',context={
            'form':form,
            'sep_text_number':sep_text_number,
            'name':name,
            'text':text,
            'word_cnt':word_cnt,
            #'number':number_list
        }
    )

def text_upload(request):
    new_text=''
    word_cnt=[]
    sep_text_number=0
    TextFileModel.objects.all().delete()
    TextModel.objects.all().delete()

    if request.method=="POST":
        form = forms.UploadTextForm(request.POST)
        sep_text_number=request.POST["sep_text_number"]
        text=request.POST["texts"]
        if form.is_valid():
            form.save()
            text = re.sub("\n",' ',text)
            text = re.sub("\r",' ',text)
            text = re.sub("  ",' ',text)
            new_text=(text.split('.'))
            new_text=new_text[:-1]

            for i,tex in enumerate(new_text):
                word_cnt.append(len(tex.split(" ")))
                TextModel.objects.create(number=i,len_text=word_cnt[-1],text=tex+".")
                new_text[i]=tex+"."
            #print(new_text)

    else:
        form = forms.UploadTextForm()

    return render(
        request,'PDFApp/text_upload.html',context={
            'form':form,
            'sep_text_number':sep_text_number,
            'text':new_text,
            'word_cnt':word_cnt,
        }
    )
