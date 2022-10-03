from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pdf_app'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('pdf_upload/',views.pdf_upload,name='pdf_upload'),
    path('text_upload/',views.text_upload,name='text_upload'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)