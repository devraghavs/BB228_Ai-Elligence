from django.contrib import admin
from django.urls import path,include

from django.views.generic import RedirectView
from django.conf.urls import url

# For removing favicon.io
url_patterns=[
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('railway/',include('railway.urls')),
]
