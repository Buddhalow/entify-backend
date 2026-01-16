from django.shortcuts import redirect, render

from django.views import View
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from entify.forms import NodeForm

from .models import Node, Type


class CreateNodeView(LoginRequiredMixin, View):
    def get(self, request):
        form = NodeForm()
        
        return render(
            request,
            'entify/admin/node/overview.html',
            {
                'form': form
            }
        )

    def post(self, request):
        form = NodeForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect(
            'nodes', node_id=form.instance.slug
        )


class NodeView(LoginRequiredMixin, View):
    def get(self, request, node_id):
        node = Node.objects.get(
            slug=node_id
        )
        form = NodeForm(instance=node)
        
        return render(
            request,
            'entify/admin/node/overview.html',
            {
                'form': form,
                'node': node
            }
        )


class NodeListView(LoginRequiredMixin, ListView):
    model = Node
    template_name = "entify/admin/nodes.html"
    queryset = Node.objects.all()

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        type = self.request.GET.get('type')

        ret['types'] = Type.objects.order_by('name')
        ret['type'] = type

        return ret

    def get_queryset(self):
        queryset = super().get_queryset()
        if type := self.request.GET.get('type'):
            queryset = queryset.filter(
                slug=type
            )

        return queryset
