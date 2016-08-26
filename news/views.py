import datetime

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django_languages.languages import LANGUAGES

from news.models import News
from news.serializers import NewsSerializer


class GetLanguageViewSet(ViewSet):

    http_method_names = ('get', )
    permission_classes = [IsAdminUser]

    def list(self, request):
        return Response(dict(LANGUAGES), status=HTTP_200_OK)


class NewsViewSet(ModelViewSet):
    """
    Endpoint to create and list news

    POST: /news - To create a news
    GET: /news  - To list all the published news in the db
    GET: /news/?language=language_code  - To filter and list language based news
    """

    queryset = News.objects.all()
    http_method_names = ['get', 'post']
    permission_classes = [IsAdminUser]
    serializer_class = NewsSerializer

    def get_queryset(self):
        language = self.request.GET.get('language')
        if language:
            self.queryset = self.queryset.filter(language=language)
        self.queryset = self.queryset.filter(publication_date__lte=datetime.date.today()).order_by('-publication_date')
        return self.queryset
