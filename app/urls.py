from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.student_view, name='student'),
    path('api-auth/', include('rest_framework.urls'))
]
