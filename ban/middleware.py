from datetime import datetime, timezone
from ban.models import Ban
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from django.http import HttpResponse

class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        return HttpResponse("in exception")


class BanAuthenticationMiddleware(MiddlewareMixin):

    def process_request(self, request):

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username is not None and password is not None:
            user = authenticate(username=username, password=password)

            if user is not None:
                now = datetime.now(timezone.utc)
                bans = Ban.objects.filter(receiver=user).filter(Q(end_date__isnull=True) | Q(end_date__gt=now))

                if bans.count() > 0:
                    try:
                        messages.add_message(request, messages.WARNING, 'This account has been banned.')
                    except messages.MessageFailure:
                        pass
                    return HttpResponseRedirect(settings.LOGIN_URL)
