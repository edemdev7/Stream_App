
from django.contrib import admin
from django.urls import path
from Broadcast import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.diffusion_en_direct, name='home'),
    path('diffusion/<int:diffusion_id>/', views.detail_diffusion, name='detail_diffusion'),
]

