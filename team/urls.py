from django.urls import path
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, DeleteTeamMemberView

urlpatterns = [
    path('', TeamMemberListView.as_view(), name='team_member_list'),
    path('new/', TeamMemberCreateView.as_view(), name='team_member_new'),
    path('edit/<int:pk>/', TeamMemberUpdateView.as_view(), name='team_member_edit'),
    path('delete/<int:pk>/', DeleteTeamMemberView.as_view(), name='team_member_delete'),
]