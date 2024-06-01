from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler403, handler404, handler500
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('auth/login/', CustomLoginView.as_view(), name='login'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/',
         blog_views.SignUpView.as_view(), name='registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler403 = 'pages.views.csrf_failure'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
