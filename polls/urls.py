from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # If you want to change the URL of the polls detail view to something else, 
    # perhaps to something like polls/specifics/12/ instead of doing it in the 
    # template (or templates) you would change it in polls/urls.py:
    # added the word 'specifics'
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),
    # The 'name' value as called by the {% url %} template tag
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]