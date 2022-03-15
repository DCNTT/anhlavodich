from django.urls import path
from.import views


urlpatterns = [
    path('memo/',views.memo, name='memo'),
    path('new',views.new, name='new'),
]
