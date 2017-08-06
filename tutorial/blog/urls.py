from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    
    url(r'^my_form$', views.my_form_upload, name='my_form_upload'),
    url(r'^my_form1$',TemplateView.as_view(template_name='blog/my_form1.html') ),
    
    #url(r'^/my_form1$',views.my_form_upload1, name='my_form_upload1'),
]
