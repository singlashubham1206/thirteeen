from django.conf.urls import url
from QRcode import views

urlpatterns = [
    url(r'^home/generateQR$',views.generateQR),
]
