from django.shortcuts import get_object_or_404, render
from webapp.models import WorkOrder, PurchaseOrder

def index(request):
	# return render(request, 'home.html', {})
	work_orders = WorkOrder.objects.order_by('due_date')[:5]
	purchase_orders = PurchaseOrder.objects.order_by('due_date')[:5]

	return render(request, 'home.html', {
		'work_orders': work_orders,
		'purchase_orders': purchase_orders
	})