from django.contrib.auth import logout as django_logout
from django.utils.translation import ugettext_lazy as _
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request, *args, **kwargs):
        django_logout(request)
        return Response({'detail': _('Successfully logged out.')})


logout = LogoutView.as_view()