from django.shortcuts import redirect, render

from django.views import View
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from entify.forms import NodeForm

from entify.models import Node, Type


class CreateNodeView(LoginRequiredMixin, View):
    def get(self, request):
        form = NodeForm()
        
        return render(
            request,
            'entify/node/[nodeId]/overview.html',
            {
                'form': form
            }
        )

    def post(self, request):
        form = NodeForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect(
            'nodes'
        )


class NodeView(LoginRequiredMixin, View):
    def get(self, request, node_id=None):
        node = Node.objects.get(
            identifier=node_id
        )
        form = NodeForm(instance=node)
        
        return render(
            request,
            'entify/node/[nodeId]/overview.html',
            {
                'form': form,
                'node': node
            }
        )

    def post(self, request, node_id=None):
        form = NodeForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect(
            'nodes'
        )


class NodeListView(LoginRequiredMixin, ListView):
    model = Node
    template_name = "entify/node/index.html"
    queryset = Node.objects.all()

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)

        ret['has_filter'] = False

        ret['types'] = Type.objects.order_by('name')
        if node_type := self.request.GET.get('type'):
            ret['type'] = node_type

        if q := self.request.GET.get('q'):
            ret['q'] = q
            ret['has_filter'] = True

        return ret

    def get_queryset(self):
        queryset = super().get_queryset()

        if node_type := self.request.GET.get('type'):
            queryset = queryset.filter(
                slug=node_type
            )

        queryset = queryset.order_by('-created')

        return queryset
