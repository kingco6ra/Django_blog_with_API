from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.reverse import reverse

from .forms import *
from .models import *
from .serializers import NewsSerializer, CommentsSerializer
from .permissions import IsAdminOrReadOnly


class HomeNews(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    paginate_by = 5

    # queryset = News.objects.select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        # select_related() - оптимизирует количество SQL запросов, убирая дубликаты запросов
        return News.objects.filter(is_published=True).order_by('-created_at').select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    allow_empty = False  # если пользователь обратится к несуществующему id, то поднимется 404 ошибка
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView, CreateView):
    model = News
    template_name = 'view_news.html'
    context_object_name = 'news_item'
    form_class = CommentsForm

    def get_success_url(self):
        news_id = self.kwargs['pk']
        return reverse_lazy('view_news', kwargs={'pk': news_id})

    # в скрытые поля присваивается id новости и id автора комментария
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
    # после отправки формы через данный класс, происходит автоматический редирект на созданную новость
    # в виду того, что ранее в модели был указан методо get_absolute_url()
    # success_url = '/' - переназначает редирект
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
class APIRootView(APIView):
    def get(self, request):
        return Response({
            'users': reverse('user-list'),
            'news': reverse('news-list'),
            'comments': reverse('comments-list'),
        })


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAdminOrReadOnly,)
