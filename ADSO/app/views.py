from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods

class GlobalLogoutView(LogoutView):
    @method_decorator(require_http_methods(['post']), name='dispatch')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('login'))
    

    def get_redirect_url(self):
        return reverse_lazy('login')

def vista_home(request):
    return render(request, 'body.html')

