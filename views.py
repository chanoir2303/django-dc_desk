from django.shortcuts import get_object_or_404, render

from .models import Ticket


def index(request):
    latest_ticket_list = Ticket.objects.order_by('-last_update')[:10]
    title_table = ['#', 'status', 'lvl', 'category', 'tag', 'agent', 'team', 'creation date', 'last action', 'user',
                   'close at']
    title_navbar = ['global', 'service requests', 'incidents', 'stats', 'settings']
    value_pagination = [10, 25, 50, 100]
    context = {'latest_ticket_list': latest_ticket_list, 'title_table': title_table,
               'value_pagination': value_pagination, 'title_navbar': title_navbar}
    return render(request, 'backlog/backlog.html', context)


def detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'backlog/detail.html', {'ticket': ticket})
