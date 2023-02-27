from django.urls import path

from .views import home_page

urlpatterns = [
    # Home Page
    path('home/', home_page, {'name': 'Home'}, name='home'),

    # Python Pages
    path('python/', home_page, {'name': 'Python'}, name='python'),
    path('python/django/', home_page, {'name': 'Python Django'}, name='python_django'),
    path('python/fastapi/', home_page, {'name': 'Python FastAPI'}, name='python_fastapi'),
    path('python/tornado/', home_page, {'name': 'Python Tornado'}, name='python_tornado'),
    path('python/django/sqlite', home_page, {'name': 'Python Django Sqlite'}, name='python_django_sqlite'),

    # C++ Pages
    path('cpp/', home_page, {'name': 'C++'}, name='cpp'),
    path('cpp/unreal_engine/', home_page, {'name': 'C++ Unreal Engine'}, name='cpp_unreal_engine'),
    path('cpp/unreal_engine/games/', home_page, {'name': 'C++ Unreal Engine Games'}, name='cpp_unreal_engine_games'),

    # JavaScript Pages
    path('javascript/', home_page, {'name': 'JavaScript'}, name='javascript'),
    path('javascript/express/', home_page, {'name': 'JavaScript Express'}, name='javascript_express'),
    path('javascript/react/', home_page, {'name': 'JavaScript React'}, name='javascript_react'),
    path('javascript/vue/', home_page, {'name': 'JavaScript Vue'}, name='javascript_vue'),
]
