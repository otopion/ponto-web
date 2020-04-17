from rest_framework.permissions import BasePermission
from django.utils.translation import ugettext_lazy as _


class IsActive(BasePermission):
    message = _('User account is disabled.')

    def has_permission(self, request, view):
        return request.user.is_active
