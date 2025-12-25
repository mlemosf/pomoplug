import os

from django.contrib.admin.utils import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.http import urlencode
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.views.generic import TemplateView
from google.auth.transport import requests
from google.oauth2 import id_token


class AuthenticationView(TemplateView):
    template_name = "authentication.html"


@csrf_exempt
def sign_in(request):
    return render(request, "sign_in.html")


@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print("Inside")
    token = request.POST["credential"]

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ["GOOGLE_OAUTH_CLIENT_ID"]
        )
    except ValueError:
        return HttpResponse(status=403)

    # In a real app, I'd also save any new user here to the database.
    # You could also authenticate the user here using the details from Google (https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-in)
    request.session["user_data"] = user_data

    # TODO: Get query params from the redirect
    query_kwargs = {"t": "minha tarefa"}
    url = f"{reverse('timer-create')}?{urlencode(query_kwargs)}"

    return redirect(url)


def sign_out(request):
    del request.session["user_data"]
    return redirect("sign_in")
