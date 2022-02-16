from django.urls import path
from games_api.views import *

# Create your urls here

urlpatterns = [
    path('category/', Category_View.as_view(), name='category'),
    path('available_on/', Available_On_View.as_view(), name='available_on'),
    path('system_requirements/', System_Requirements_View.as_view(), name='system_requirements'),
    path('publishers/', Publishers_View.as_view(), name='publishers'),
    path('language_supported/', Language_Supported_View.as_view(), name='language_supported'),
    path('capabilities/', Capabilities_View.as_view(), name='capabilities'),
    path('games/', Games_View.as_view(), name='games'),
]