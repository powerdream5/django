from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TeamMember
from .forms import TeamMemberForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team_member_list.html'
    paginate_by = 5

    def get_queryset(self):
        sort_by = self.request.GET.get('sort', 'name')
        
        sort_options = {
            'name': ('first_name', 'last_name'),
            'date_added': ('created_at',),
        }

        sort_fields = sort_options.get(sort_by, sort_options['name'])
        
        return TeamMember.objects.filter(is_deleted=False).order_by(*sort_fields)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_member_counter'] = TeamMember.objects.filter(is_deleted=False).count()
        return context

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_member_form.html'
    success_url = reverse_lazy('team_member_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Team member created successfully!')
        return response

class TeamMemberUpdateDeleteView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_member_form.html'
    success_url = reverse_lazy('team_member_list')

    def post(self, request, *args, **kwargs):
        if "action" in request.POST:
            if request.POST["action"] == "delete":
                self.object = self.get_object()
                self.object.delete()
                messages.success(request, 'Team member deleted successfully!')
                return HttpResponseRedirect(self.get_success_url())
            elif request.POST["action"] == "Save":
                return super().post(request, *args, **kwargs)
            
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Team member updated successfully!')
        return response

def custom_404(request, exception=None):
    return render(request, '404.html', {}, status=404)