from django.urls import path
from . import views

# #ekhane route gula list kora hobe
urlpatterns = [
    # path('<a>', views.home, name="home") # in episode 3 url theke msg web browser e show koranor jonno
    # path('/)
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]
