from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect, reverse
from .models import User


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        print('I am entering get_login_redirect_url')
        if 'team_membership_project_id' in request.session:
            parameters = {}
            parameters['invitation_id'] = request.session['invitation_id']
            path = reverse('action:accept_invitation', urlconf=None, args=None, kwargs=parameters)
            return path

        path = '/'

        return path

    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.Next to simply returning True/False you can also intervene the
        regular flow by raising an ImmediateHttpResponse. (Comment reproduced from the overridden method.)
        """
        return True


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = User.objects.filter(email=sociallogin.user.email).first()
        if user and not sociallogin.is_existing:
            sociallogin.connect(request, user)
