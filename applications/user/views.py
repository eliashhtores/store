from django.views.generic import TemplateView


class LoginUserView(TemplateView):
    template_name = 'user/login.html'
