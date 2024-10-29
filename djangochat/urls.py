from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('A/', include('chat.urls')),
    path('', include('translator.urls')),  # Inclure les URLs de l'application
    path("chatbot/", include("chatbot.urls")),  # Incluez les URLs de l'application chatbot


 
]
