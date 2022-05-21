from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet

from .forms import *
from .models import *
from .permissions import IsAdminOrReadOnly, IsAdminUser, IsOwnerOrReadOnly
from .serializers import NewsSerializer, CommentsSerializer, UserSerializer, CategorySerializer


class HomeNews(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by('-created_at').select_related('category', 'author')


class NewsByCategory(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs['category_id'], is_published=True).select_related('category', 'author')


class ViewNews(DetailView, CreateView):
    model = News
    template_name = 'view_news.html'
    context_object_name = 'news_item'
    form_class = CommentsForm

    def get_success_url(self):
        news_id = self.kwargs['pk']
        return reverse_lazy('view_news', kwargs={'pk': news_id})

    # the news id and the comment author id are entered in the hidden fields
    def get_initial(self, **kwargs):
        initial = super(ViewNews, self).get_initial()
        initial['news'] = self.kwargs['pk']
        initial['author'] = self.request.user.id
        initial['content'] = ''
        return initial.copy()

    def get_context_data(self, **kwargs):
        context = super(ViewNews, self).get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(news_id=self.kwargs['pk']).select_related('author')
        return context


class CreateNews(LoginRequiredMixin, CreateView):
    template_name = 'add_news.html'
    login_url = 'home'
    form_class = NewsForm


def contact(request):
    if request.method == 'POST':
        form = ContactEmailForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'], form.cleaned_data['content'],
                'king.co6ra@yandex.ru', ['horror201@mail.ru']
            )
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactEmailForm()
    return render(request, 'contact.html', {'form': form})


# API
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# TokenAuthentication
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
