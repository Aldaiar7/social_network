from django.urls import path


from . import views

urlpatterns = [
    path(
        "subscriptions/<slug:slug>/create/", views.SubscriptionCreateAPIView.as_view(), name="follow"
    ),
    path(
        "subscriptions/<slug:slug>/delete/<int:pk>/",
        views.SubscriptionDestroyAPIView.as_view(),
        name="unfollow",
    ),
    path("subscriptions/list/", views.SubscriptionListAPIView.as_view(), name="sub_list"),
]
