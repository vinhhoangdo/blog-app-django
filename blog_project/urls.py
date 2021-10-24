from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
    path('accounts/',include('accounts.urls')),  # new
]
