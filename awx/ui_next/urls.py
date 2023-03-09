from django.urls import re_path
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView

from awx.main.utils.licensing import server_product_name


class IndexView(TemplateView):
    template_name = 'index_awx.html'


app_name = 'ui_next'

urlpatterns = [re_path(r'^$', IndexView.as_view(), name='index')]
