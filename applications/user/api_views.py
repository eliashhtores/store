from rest_framework.views import APIView
from .serializers import LoginSocialSerializer


class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token_id = serializer.data.get('token_id', None)

        return []
