from .models import RouteRank,FindTrains
from rest_framework.response import Response
from collections import defaultdict


def assign_route_rank(trains_dic):
    try:
        for routenum,routedetails in trains_dic.items():
            for part,details in routedetails.items():
                src,dest,train_no = details["src"],details["dest"],details["train_no"]
                trains_dic[routenum][part]["Route_score"] = 0
                ob = RouteRank.objects.filter(src=src, dest=dest, train_no=train_no)
                if len(ob)>0:
                    obj1 = RouteRank.objects.get(src=src, dest=dest, train_no=train_no)
                    trains_dic[routenum][part]["Route_score"] = obj1.score
        return trains_dic
    except Exception as e:
        status = 200
        return Response({"status": status, "msg": e})


def reorder_routes(trains_dic):
    try:
        trains_dic = dict(sorted(trains_dic.items(),key=lambda x:x[1]["src_to_inter_stop"]["Route_score"]+x[1]["inter_stop_to_dest"]["Route_score"],reverse=True))
        return trains_dic
    except Exception as e:
        status = 200
        return Response({"status": status, "msg": e})


def filtering_4_routes(trains_dic):
    try:
        top_trains_dic = dict()
        c = 1
        for routeNum,routeDetails in trains_dic.items():
            if c>4: break
            top_trains_dic["Route"+str(c)] = routeDetails
            c += 1
        return top_trains_dic

    except Exception as e:
        status = 200
        return Response({"status": status, "msg": e})


def update_route_rank(src,int_stop,dest,train_no_src_to_intStop,train_no_intStop_to_dest):
    try:
        ob = RouteRank.objects.filter(src=src,dest=int_stop,train_no=train_no_src_to_intStop)
        if len(ob)>0:
            obj1 = RouteRank.objects.get(src=src,dest=int_stop,train_no=train_no_src_to_intStop)
            obj1.score += 1
            obj1.save()
        else:
            obj1 = RouteRank(src=src,dest=int_stop,train_no=train_no_src_to_intStop,score=0)
            obj1.save()

        ob = RouteRank.objects.filter(src=int_stop, dest=dest, train_no=train_no_intStop_to_dest)
        if len(ob) > 0:
            obj1 = RouteRank.objects.get(src=int_stop, dest=dest, train_no=train_no_intStop_to_dest)
            obj1.score += 1
            obj1.save()
        else:
            obj1 = RouteRank(src=int_stop, dest=dest, train_no=train_no_intStop_to_dest,score=0)
            obj1.save()
    except Exception as e:
        status = 200
        return Response({"status": status, "msg": e})

def store_alternate_trains(trains_dic):
    try:
        for rowNum,rowDetails in trains_dic.items():
            id = rowDetails["src_to_inter_stop"]["id"]
            src = rowDetails["src_to_inter_stop"]["src"]
            dest = rowDetails["inter_stop_to_dest"]["dest"]
            int_stop = rowDetails["src_to_inter_stop"]["dest"]
            train_no_src_to_intStop = rowDetails["src_to_inter_stop"]["train_no"]
            train_no_intStop_to_dest = rowDetails["inter_stop_to_dest"]["train_no"]

            obj = FindTrains(id= id, src=src, dest=dest,int_stop= int_stop, train_no_src_to_intStop =train_no_src_to_intStop, train_no_intStop_to_dest= train_no_intStop_to_dest )
            obj.save()
    except Exception as e:
        status = 200
        return Response({"status": status, "msg": e})