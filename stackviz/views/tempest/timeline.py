from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, RedirectView
from django.http import Http404

from stackviz.parser.tempest_subunit import get_repositories


class TimelineView(TemplateView):
    template_name = 'tempest/timeline.html'

    def get_context_data(self, **kwargs):
        context = super(TimelineView, self).get_context_data(**kwargs)
        context['run_id'] = self.kwargs['run_id']

        return context


class TimelineLatestView(RedirectView):
    def get_redirect_url(self, run_id):
        repos = get_repositories()
        if not repos:
            raise Http404("No testr repositories could be loaded")

        return reverse('tempest_timeline', kwargs={
            'run_id': repos[0].get_latest_run().get_id()
        })
