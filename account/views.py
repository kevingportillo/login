from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout
# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
)    # 変更
from django.contrib.auth import get_user_model
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
)    # 変更
from django.urls import reverse    # 追記
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView
)    # 追記


User = get_user_model()

class OnlyYouMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser
    

class UserDetail(OnlyYouMixin, DetailView):
    model = User
    template_name = 'account/user_detail.html'

class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm   # 変更
    # 省略
    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=raw_pw)
        login(self.request, user)
        return response
    
class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'account/user_edit.html'

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.kwargs['pk']})
    
# 省略
class PasswordChange(PasswordChangeView):
    template_name = 'account/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'account/user_detail.html'

class UserDelete(OnlyYouMixin, DeleteView):
    model = User
    template_name = 'account/user_delete.html'
    success_url = reverse_lazy('login')

def cerrarsesion (request):
    logout(request=request)
    return redirect('/account/login')