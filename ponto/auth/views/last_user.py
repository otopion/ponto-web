from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from ponto.auth.serializers import UserSerializer


class LastUserViewSet(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return get_user_model().objects.last()


last_user = LastUserViewSet.as_view()
