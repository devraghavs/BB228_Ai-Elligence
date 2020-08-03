from django.shortcuts import render
from .generate_trains.generate_alternate_trains import *
from .ordering_alternate_routes import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FindTrains


def findTrains(request):
    try:
        return render(request,'railway/findTrains.html')
    except Exception as e:
        status = 200
        return Response({"status": status, "msg": "Error"})



@api_view(['POST'])
def showTrains(request):
    try:
        src = request.data['src']
        dest = request.data['dest']
        journey_date = request.data['journey_date']
        train_type = request.data['train_type']
        night_shift = request.data['night_shift']

        # Generate Trains
        trains_dic = generate_trains(src,dest,night_shift,journey_date,train_type)

        # Assign Route Rank
        trains_dic = assign_route_rank(trains_dic)

        # Reorder Routes
        trains_dic = reorder_routes(trains_dic)

        #Filtering Top Trains
        trains_dic = filtering_4_routes(trains_dic)

        #Storing Top Trains Data
        store_alternate_trains(trains_dic)

        return render(request,'railway/showTrains.html',context = {'trains_dic': trains_dic,'no_of_routes': len(trains_dic)})

    except Exception as e:
        status = 200
        return Response({"status": status, "msg": e})



@api_view(['GET','POST'])
def book_ticket(request,id):
    try:
        obj = FindTrains.objects.get(id=id)
        src = obj.src
        int_stop = obj.int_stop
        dest = obj.dest
        train_no_src_to_intStop = obj.train_no_src_to_intStop
        train_no_intStop_to_dest = obj.train_no_intStop_to_dest

        # Updating Route Rank
        update_route_rank(src,int_stop,dest,train_no_src_to_intStop,train_no_intStop_to_dest)
        return render(request,'railway/findTrains.html')

    except Exception as e:
        status = 200
        return Response({"status": status, "msg": e})