from django.conf.urls import url
from views import predict

urlpatterns = [
    url(r'^predict',predict),
    url(r'$', predict),
]