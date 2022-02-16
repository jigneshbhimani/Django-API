from games_api.models import *
from rest_framework.generics import ListAPIView
from games_api.serializers import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from games_api.permissions import IsOwnerOrReadOnly


# Create your views here



# Category View
# generics.CreateAPIView, generics.RetrieveUpdateAPIView, generics.DestroyAPIView
class Category_View(ListAPIView):                               
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


# Available_on View
# generics.CreateAPIView, generics.RetrieveUpdateAPIView, generics.DestroyAPIView
class Available_On_View(ListAPIView):                           
    queryset = Available_on.objects.all()
    serializer_class = AvailableOnSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


# System_requirements View
# generics.CreateAPIView, generics.RetrieveUpdateAPIView, generics.DestroyAPIView
class System_Requirements_View(ListAPIView):                    
    queryset = System_requirements.objects.all()
    serializer_class = SystemRequirementsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


# Publishers View
# generics.CreateAPIView, generics.RetrieveUpdateAPIView, generics.DestroyAPIView
class Publishers_View(ListAPIView):                             
    queryset = Publishers.objects.all()
    serializer_class = PublishersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


# Language_Supported View
# generics.CreateAPIView, generics.RetrieveUpdateAPIView, generics.DestroyAPIView
class Language_Supported_View(ListAPIView):                     
    queryset = Language_supported.objects.all()
    serializer_class = LanguageSupportedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


# Capabilities View
# generics.CreateAPIView, generics.RetrieveUpdateAPIView, generics.DestroyAPIView
class Capabilities_View(ListAPIView):                           
    queryset = Capabilities.objects.all()
    serializer_class = CapabilitiesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


# Games View
# generics.CreateAPIView, generics.RetrieveUpdateAPIView, generics.DestroyAPIView
class Games_View(ListAPIView):                                  
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # Filteration
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = (
        'name',
        'category', 
        'publishers', 
        'available_on', 
        'capabilities', 
        'best_of_all_time', 
        'trending', 
        'age_rating'
    )