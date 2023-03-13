from django.shortcuts import render
from django.db.models import Sum
from payment.models import CashPayment, MpesaPayment
from trips.models import TripSeats, Trip, TripDetails
from branches.models import Branch
from datetime import datetime
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.models import Count
from django.http import JsonResponse
from rest_framework.decorators import api_view



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

import json


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

    return JsonResponse(data)




# def dashboard_api(request):
#     # calculate required data
#     cash_payments = CashPayment.objects.all().aggregate(Sum('amount'))
#     total_cash_payments = cash_payments['amount__sum'] or 0
#     mpesa_payments = MpesaPayment.objects.all().aggregate(Sum('transaction'))
#     total_mpesa_payments = mpesa_payments['transaction__sum'] or 0
#     total_payments = total_cash_payments + total_mpesa_payments

#     booked_seats = TripSeats.objects.filter(status='Booked')
#     total_tickets_booked = len(booked_seats.distinct('seat').values('seat'))

#     active_trips = Trip.objects.filter(
#     expected_dep_time__lte=datetime.now(),
#     expected_arval_time__gte=datetime.now(),
#     )
#     total_active_trips = active_trips.count()

#     departed_trips = TripDetails.objects.filter(state='Departure')
#     total_departed_trips = departed_trips.count()

#     total_branches = Branch.objects.count()

#     pending_tickets = TripSeats.objects.filter(status='Pending')
#     total_pending_tickets = pending_tickets.count()

#     data = {
#         'total_payments_made': MpesaPayment.objects.count() + CashPayment.objects.count(),
#         'total_tickets_booked': total_tickets_booked,
#         'active_trips_today': total_active_trips,
#         'departed_today': total_departed_trips,
#         'no_of_branches': total_branches,
#         'pending_tickets': total_pending_tickets,
#     }

#     return Response(data)







































# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

# class DashboardViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=['get'])
#     def total_payments_made(self, request):
#         mpesa_payments = MpesaPayment.objects.all().aggregate(total_amount=Sum('payment__sale__total_amount'))['total_amount']
#         cash_payments = CashPayment.objects.all().aggregate(total_amount=Sum('amount'))['total_amount']
#         total_payments = mpesa_payments + cash_payments

#         response = {
#             "total_payments_made": total_payments
#         }
        

#     @action(detail=False, methods=['get'])
#     def tickets_booked(self, request):
#         tickets_booked = TripSeats.objects.filter(status='Booked').count()
#         return Response({'tickets_booked': tickets_booked})

#     @action(detail=False, methods=['get'])
#     def active_trips_today(self, request):
#         active_trips = Trip.objects.filter(
#             expected_dep_time__date=datetime.datetime.today(),
#             tripdetails__state='Departure'
#         ).count()
#         return Response({'active_trips_today': active_trips})

#     @action(detail=False, methods=['get'])
#     def departured_today(self, request):
#         departured_trips = Trip.objects.filter(
#             expected_dep_time__date=datetime.datetime.today(),
#             tripdetails__state='Arrival'
#         ).count()
#         return Response({'departured_today': departured_trips})

#     @action(detail=False, methods=['get'])
#     def no_of_branches(self, request):
#         no_of_branches = Branch.objects.all().count()
#         return Response({'no_of_branches': no_of_branches})

#     @action(detail=False, methods=['get'])
#     def pending_tickets(self, request):
#         pending_tickets = TripSeats.objects.filter(status='Empty').count()
#         return Response({'pending_tickets': pending_tickets})



# class DashboardViewSet(viewsets.ViewSet):
#       @action(detail=False, methods=['get'])
#       def total_payments_made(self, request):
#                 cash_payments = CashPayment.objects.aggregate(total=Sum('amount'))['total'] or 0
#                 mpesa_payments = MpesaPayment.objects.aggregate(total=Sum('amount'))['total'] or 0
                
#                 total_payments = cash_payments + mpesa_payments
                
#                 tickets_booked = TripSeats.objects.filter(status=TripSeats.STATUS_CHOICES).aggregate(total=Sum('tickets'))['total'] or 0
                
#                 active_trips = Trip.objects.filter(expected_dep_time__date=datetime.datetime.today()).count()
#                 departed_trips = TripDetails.objects.filter(state=TripDetails.ARRIVAL, created_on__date=datetime.datetime.today()).count()
                
#                 branches = Branch.objects.all().count()
                
#                 pending_tickets = Ticket.objects.filter(status=Ticket.STATUS_PENDING).count()
                
#                 data = {
#                     'total_payments_made': total_payments,
#                     'tickets_booked': tickets_booked,
#                     'active_trips_today': active_trips,
#                     'departed_today': departed_trips,
#                     'no_of_branches': branches,
#                     'pending_tickets': pending_tickets,
#                 }
                
#                 return Response(data)