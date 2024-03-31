from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from .models import TeamMember
from .forms import TeamMemberForm
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team_member_list.html'

    def get_queryset(self):
        sort_by = self.request.GET.get('sort', 'name')
        
        sort_options = {
            'name': ('first_name', 'last_name'),
            'date_added': ('created_at',),
        }

        sort_fields = sort_options.get(sort_by, sort_options['name'])
        
        return TeamMember.objects.filter(is_deleted=False).order_by(*sort_fields)

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_member_form.html'
    success_url = reverse_lazy('team_member_list')

class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_member_form.html'
    success_url = reverse_lazy('team_member_list')

@method_decorator(csrf_protect, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class DeleteTeamMemberView(View):
    def post(self, request, pk, *args, **kwargs):
        member = get_object_or_404(TeamMember, pk=pk)
        member.delete()
        return JsonResponse({'status': 'success'})