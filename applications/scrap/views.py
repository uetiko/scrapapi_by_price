from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(TemplateView):
    template_name = 'scrap/home.html'


class AdminView(TemplateView):
    template_name = 'scrap/admin.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kvargs):
        return super(self.__class__, self).dispatch(request, *args, **kvargs)
