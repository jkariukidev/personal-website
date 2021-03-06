from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms
from .models import Profile


class UserRegistrationView(generic.CreateView):
    """
    User creation view.
    """
    form_class = forms.AccountRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = forms.UserLoginForm
    success_url = reverse_lazy('dashboard')


class CreateProfilePageView(LoginRequiredMixin, generic.CreateView):
    """
    Profile creation view.
    """
    model = Profile
    form_class = forms.ProfilePageForm
    template_name = 'registration/create_user_profile.html'
    success_url = reverse_lazy('accounts:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'registration/dashboard.html'


class ShowProfileView(LoginRequiredMixin, generic.DetailView):
    """
    Profile details of registered user.
    """
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class EditProfilePageView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = forms.ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('accounts:edit_profile_success')


class UserEditView(LoginRequiredMixin, generic.UpdateView):
    """
    Edit user profile.
    """
    form_class = forms.ProfileEditForm
    template_name = 'edit_user_profile.html'
    success_url = reverse_lazy('accounts:dashboard')

    def get_object(self, queryset=None):
        return self.request.user


class UserEditSuccessView(generic.TemplateView):
    template_name = 'registration/edit_profile_success.html'


class UserRegisterSuccessView(generic.TemplateView):
    template_name = 'registration/register_done.html'
