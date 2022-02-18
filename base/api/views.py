from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .models import Doctor
from .serializers import DoctorSerializer

class ListCreateDoctor(GenericViewSet, ListModelMixin, CreateModelMixin):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RetrieveUpdateDestroyDoctor(GenericViewSet, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)        

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)