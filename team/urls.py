from django.urls import path, re_path
from django.conf.urls import handler404
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateDeleteView, custom_404

urlpatterns = [
    path('', TeamMemberListView.as_view(), name='team_member_list'),
    path('new/', TeamMemberCreateView.as_view(), name='team_member_new'),
    path('edit/<int:pk>/', TeamMemberUpdateDeleteView.as_view(), name='team_member_edit'),
    re_path(r'^.*$', custom_404),
]