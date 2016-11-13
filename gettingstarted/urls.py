from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_all_workouts$',hello.views.get_all_workouts, name='get_all_workouts'),
    url(r'^add_workout$',hello.views.add_workout, name='add_workout'),
    url(r'^remove_workout$',hello.views.remove_workout, name='remove_workout'),
    url(r'^get_all_food$',hello.views.get_all_food, name='get_all_food'),
    url(r'^add_food$',hello.views.add_food, name='add_food'),
    url(r'^remove_food$',hello.views.remove_food, name='remove_food'),
]
