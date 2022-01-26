from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from firebase_admin import auth
from .serializers import LoginSocialSerializer
from .models import User


class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token_id = serializer.data.get('token_id', None)
        decoded_token = auth.verify_id_token(token_id)
        email = decoded_token['email']
        name = decoded_token['name']
        # picture = decoded_token['picture']
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'full_name': name,
                'email': email,
                'is_active': True
            }
        )
        if created:
            token = Token.objects.create(user=user)
        else:
            token = Token.objects.get(user=user)

        userGet = {
            'id': user.id,
            'email': user.email,
            'full_name': user.full_name,
            'gender': user.gender
        }

        return Response({
            'token': token.key,
            'user': userGet
        })
