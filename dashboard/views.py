from django.db.models import Count
from django.db.models import Sum
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from payment.models import CashPayment, MpesaPayment
from trips.models import TripSeats, Trip, TripDetails
from branches.models import Branch



#* Total Payments Paid
# total cash payments made
cash_payments = CashPayment.objects.all().aggregate(Sum('amount'))
total_cash_payments = cash_payments['amount__sum'] or 0

# total mpesa payments made
mpesa_payments = MpesaPayment.objects.all().aggregate(Sum('transaction'))
total_mpesa_payments = mpesa_payments['transaction__sum'] or 0

# total payments made
total_payments = total_cash_payments + total_mpesa_payments


#* Tickets Booked
# number of booked seats
booked_seats = TripSeats.objects.filter(status='Booked')
total_tickets_booked = len(booked_seats)


#*Active Trips Today
from django.utils import timezone

# active trips today
today = timezone.now().date()
active_trips_today = Trip.objects.filter(expected_dep_time__date=today).count()

#*Departed Today

# trips departed today
today = timezone.now().date()
departed_trips_today = TripDetails.objects.filter(state='Departure', created_on__date=today).count()

#*No of Branches


# number of branches
total_branches = Branch.objects.all().count()

#*Pending Tickets
# number of empty seats
empty_seats = TripSeats.objects.filter(status='Empty')
total_pending_tickets = len(empty_seats)

#*Compiling


@api_view(['GET'])
def dashboard_api(request):
    # calculate required data
    cash_payments = CashPayment.objects.all().aggregate(Sum('amount'))
    total_cash_payments = cash_payments['amount__sum'] or 0
    mpesa_payments = MpesaPayment.objects.all().aggregate(Sum('transaction'))
    total_mpesa_payments = mpesa_payments['transaction__sum'] or 0
    total_payments = total_cash_payments + total_mpesa_payments

    booked_seats = TripSeats.objects.filter(status='Booked').values('seat').annotate(count=Count('seat'))
    total_tickets_booked = len(booked_seats)

    active_trips = Trip.objects.filter(
    expected_dep_time__lte=datetime.now(),
    expected_arval_time__gte=datetime.now(),
    )
    total_active_trips = active_trips.count()

    departed_trips = TripDetails.objects.filter(state='Departure')
    total_departed_trips = departed_trips.count()

    total_branches = Branch.objects.count()

    pending_tickets = TripSeats.objects.filter(status='Pending')
    total_pending_tickets = pending_tickets.count()

    data = {
        'total_payments_made': MpesaPayment.objects.count() + CashPayment.objects.count(),
        'total_tickets_booked': total_tickets_booked,
        'active_trips_today': total_active_trips,
        'departed_today': total_departed_trips,
        'no_of_branches': total_branches,
        'pending_tickets': total_pending_tickets,
    }

    return Response(data, status=status.HTTP_200_OK)

