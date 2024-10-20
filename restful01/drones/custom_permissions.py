from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Se o metodo for get, read, options
        if request.method in permissions.SAFE_METHODS:
            return True

        # Se for outro metodo verifica se o responsavel
        # pela requisisão é o dono do drone.
        else:

            return obj.owner == request.user
