from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from task_manager.serializers.user import UserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

