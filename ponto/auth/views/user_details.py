from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from ponto.auth.permissions import IsActive
from ponto.auth.serializers import LoginResponseSerializer


class UserDetailsView(RetrieveAPIView):
    serializer_class = LoginResponseSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def get_object(self):
        return self.request.user


user_details = UserDetailsView.as_view()
