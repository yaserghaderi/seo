# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('keywordresearch.urls')),  # اطمینان از وجود این خط برای ادغام مسیرهای اپلیکیشن

]