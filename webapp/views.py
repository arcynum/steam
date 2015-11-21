from django.shortcuts import get_object_or_404, render
from django.http import Http404

from webapp.models import Contact, WorkOrder, PurchaseOrder

def index(request):
	# return render(request, 'home.html', {})
	work_orders = WorkOrder.objects.order_by('due_date')[:5]
	purchase_orders = PurchaseOrder.objects.order_by('due_date')[:5]

	return render(request, 'home.html', {
		'work_orders': work_orders,
		'purchase_orders': purchase_orders
	})

def contact_index(request):
	contacts = Contact.objects.order_by('modified')[:5]
	return render(request, 'contacts/index.html', {'contacts': contacts})

def contact_view(request, contact_id):
	try:
		contact = Contact.objects.get(pk=contact_id)
	except Contact.DoesNotExist:
		raise Http404("Contact does not exist")
	return render(request, 'contacts/view.html', {'contact': contact})