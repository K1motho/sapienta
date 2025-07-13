from django.urls import path
from . import views

urlpatterns = [
    path('api/daily/', views.daily_saying, name='daily_saying'),
    path('api/save/<int:saying_id>/', views.save_saying, name='save_saying'),
    path('api/reflect/<int:saying_id>/', views.add_reflection, name='add_reflection'),
    path('api/saved/', views.get_saved_sayings, name='get_saved_sayings'),  # ✅ Include this
]
