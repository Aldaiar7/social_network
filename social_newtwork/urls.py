from rest_framework_swagger.views import get_swagger_view
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="social_network API",
        default_version='v0',
        description="Welcome to social network",
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include('account.urls')),
    path('api/v0/', include('subscription.urls')),
    path('api/v0/', include('post.urls')),
    path('api/v0/', include('message.urls')),
    path('api/v0/', include('like.urls')),
    path('api/v0/', include('comment.urls')),
    path('api/v0/', include('status.urls')),
    path('api/v0/', include('mark.urls')),
    path('api/v0/', include('repost.urls')),
    path('api/v0/', include('feed.urls')),
    
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
