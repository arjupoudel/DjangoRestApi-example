from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paradigm', views.ParadigmView)
router.register('programmer', views.ProgrammerView)


urlpatterns =[
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='API Example', public=False)), #localhost:8000/api/docs takes you to the documentation page
]