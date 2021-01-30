from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('blocks/<int:height>', views.show_block_by_height),
    path('<int:page_num>', views.index),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='1'))

]