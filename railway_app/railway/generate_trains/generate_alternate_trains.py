import requests
import json
import time
from datetime import datetime
import os
FMT = '%H:%M:%S'

curr_path = os.path.abspath(os.getcwd())
f = open(curr_path+r'\json\ALL_Train_Schedule.json',)
trn_sch = json.load(f) 
f=open(curr_path+r'\json\All_train_from_a_station.json')
all_trn=json.load(f)
f=open(curr_path+r'\json\train_arr_dept.json')
trn_arr_dept=json.load(f)
f=open(curr_path+r'\json\All_Station_Nearbuy.json')
stat_neig=json.load(f)
f=open(curr_path+r'\json\station_code_to_name.json')
code_to_name=json.load(f)
f=open(curr_path+r'\json\station_name_to_code.json')
name_to_code=json.load(f)
f=open(curr_path+r'\json\total_time_stat.json')
total_time_stat=json.load(f)


class Book_Ticket():

    def __init__(self,src,dest,day_night,date=None,train_type=None):
        self.routes = []
        self.final_routes = []
        self.source=src
        self.destination=dest
        self.day_night=day_night
        self.src=self.station_name_to_code(src.upper())  #station code call
        self.dest=self.station_name_to_code(dest.upper())
        if self.src=="NOT" or self.dest=="NOT":  #IF STATION CODE NOT FOUND
            print("______________________________Check Your Staion Name Again________________________________")

    def display(self):
        rtn_dict = dict()
        counter = 1
        Final_print_index = self.Sort()

        for i in Final_print_index:
            key = "Route" + str(counter)
            rtn_dict[key] = dict()
            part1 = i[0]
            part2 = i[1]
            part3 = i[2]
            part4 = i[3]
            n = part1[2]
            if "." in str(n):  # THIS
                index = str(n).index('.')  # THIS
                minutes = str(n)[:index:-1]  # THIS
                minutes = minutes[::-1]  # THIS
                minutes = "0." + minutes  # THIS
                minutes = 60 * float(minutes)  # THIS
                minutes = str(int(minutes))  # THIS
                hour = str(int(n))  # THIS
                time_display = hour + ":" + minutes  # THIS
            else:  # THIS
                hour = str(int(n))  # THIS
                time_display = hour + ":" + "00"  # THIS

            key_pass1 = "src_to_inter_stop"
            rtn_dict[key][key_pass1] = dict()
            rtn_dict[key][key_pass1]["waiting_time"] = int(part4)
            rtn_dict[key][key_pass1]['id'] = counter
            rtn_dict[key][key_pass1]['train_no'] = part1[0]
            rtn_dict[key][key_pass1]['train_type'] = "Special"
            rtn_dict[key][key_pass1]['src'] = code_to_name[part1[1][0]]
            rtn_dict[key][key_pass1]['dest'] = code_to_name[part1[1][1]]
            rtn_dict[key][key_pass1]['dep_time_at_src'] = trn_arr_dept[part1[0]][part1[1][0]][0]
            rtn_dict[key][key_pass1]["arr_time_at_dest"] = trn_arr_dept[part1[0]][part1[1][1]][0]
            rtn_dict[key][key_pass1]["journey_time"]=time_display
            key_pass2 = "inter_stop_to_dest"
            n2 = part2[2]
            if '.' in str(n2):  # THIS
                index = str(n2).index('.')  # THIS
                minutes2 = str(n2)[:index:-1]  # THIS
                minutes2 = minutes2[::-1]  # THIS
                minutes2 = "0." + minutes2  # THIS
                minutes2 = 60 * float(minutes2)  # THIS
                minutes2 = str(int(minutes2))  # THIS
                hour2 = str(int(n2))  # THIS
                time_display2 = hour2 + ":" + minutes2  # THIS
            else:  # THIS
                hour2 = str(int(n2))  # THIS
                time_display2 = hour2 + ":" + "00"  # THIS
            rtn_dict[key][key_pass2] = dict()
            rtn_dict[key][key_pass2]['train_no'] = part2[0]
            rtn_dict[key][key_pass2]['train_type'] = "Special"
            rtn_dict[key][key_pass2]['src'] = code_to_name[part2[1][0]]
            rtn_dict[key][key_pass2]['dest'] = code_to_name[part2[1][1]]
            rtn_dict[key][key_pass2]['dep_time_at_src'] = trn_arr_dept[part2[0]][part2[1][0]][1]
            rtn_dict[key][key_pass2]["arr_time_at_dest"] = trn_arr_dept[part2[0]][part2[1][1]][0]
            rtn_dict[key][key_pass2]["journey_time"]=time_display2          #THIS
            counter += 1

        return rtn_dict


    def train_no_to_station(self,trn_num):
        return [i[0] for i in trn_sch[trn_num]]

    def Sort(self):
        sub_li = self.final_routes
        return (sorted(sub_li, key=lambda x: x[2]))

    def train_between_station(self,src,dest):
        final=[]
        #src= source staion code
        #dest= destination station code
        temp=list(set(all_trn[src]).intersection(set(all_trn[dest])))
        for i in temp:
            jun_list=self.train_no_to_station(i)
            if jun_list.index(src)<jun_list.index(dest):
                final.append(i)
        return final
    def station_name_to_code(self,name,flag=0):
        #url =" http://indianrailapi.com/api/v2/StationNameToCode/apikey/0fe3b963408929419d6d519b06fd4110/StationName/"+name+"/"
        #response = requests.get(url)
        # print(response) successfully
        #data=response.text
        # print(data[])
        #parsed=json.loads(data)
        #print(json.dumps(parsed, indent=4))
        #code=parsed['Station']['StationCode']
        try:
            #print(flag)
            if flag==0:
                code=name_to_code[name]
                #print(code)
                return code
            if flag==1:
                code=name_to_code[name]
                #print(code)
                return code
        except:
            if flag==1:
                return "NOT"
            name2=name.upper()+" "+"JN"
            flag=1
            return self.station_name_to_code(name2,flag)

    def poss_station(self):
        #src_stat=[self.train_no_to_station(i) for i in all_trn[self.src]]
        #dest_stat=[self.train_no_to_station(i) for i in all_trn[self.dest]]
        #src_stat_set=set()
        #dest_stat_set=set()
        #for i in src_stat:
            #for j in i:
                #src_stat_set.add(j)
        #for i in dest_stat:
            #for j in i:
                #dest_stat_set.add(j)
        src_stat_set=set(stat_neig[self.src])
        dest_stat_set=set(stat_neig[self.dest])
        final_set=src_stat_set.intersection(dest_stat_set)
        if self.src in final_set:
            final_set.remove(self.src)
        if self.dest in final_set:
            final_set.remove(self.dest)
        return list(final_set)

    def time_difference(self, arr2, arr):
        td = datetime.strptime(arr2, FMT) - datetime.strptime(arr, FMT)
        days = td.days
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        seconds += td.microseconds / 1e6
        return [days, hours, minutes]

    def alternate_train(self):


        inter_stat=self.poss_station()
        for i in inter_stat:
            self.create_tuple(i)
        for i,j in self.routes:
            try:
                total_time=total_time_stat[i[0]][j[1]]
                if total_time<=10:
                    total_time=total_time*1.5
                elif total_time>10 and total_time<=30:
                    total_time=total_time*1.25
                elif total_time>30:
                    total_time=total_time*1.2
            except:
                continue
            #print("_________MAIN LOOP___________")
            trn_list_p1=self.train_between_station(i[0],i[1])
            trn_list_p2=self.train_between_station(j[0],j[1])
            #trn_list_p1=
            #trn_list_p2=list(set(all_trn[j[0]]).intersection(set(all_trn[j[1]])))
            if trn_list_p1==None:
                continue
            if trn_list_p2==None:
                continue
            #print(trn_list_p1)
            for t in trn_list_p1:
                #print("LOOP1")
                #print(t)
                try:
                    arr,dept,time_1=trn_arr_dept[t][i[1]]
                    arr_src,dept_src,time_src=trn_arr_dept[t][i[0]]
                    time_arr=int(arr[:2])
                    if self.day_night=="N":
                        if time_arr<6 and time_arr>-1:
                            continue
                    inter1_time=time_1-time_src
                    inter1_time=round(inter1_time,2)
                    #print(arr,dept,end="$$$$$$$$\n")
                    for k in trn_list_p2:
                        if t==k:
                            continue
                        #print("LOOP2")
                        #print(k)
                        arr2,dept2,time_2=trn_arr_dept[k][i[1]]
                        arr2_dest,dept2_dest,time_dest=trn_arr_dept[k][j[1]]
                        time_arr_int=int(arr2[:2])
                        if self.day_night=="N":
                            if time_arr_int<6 and time_arr_int>-1:
                                continue
                        inter2_time=time_dest-time_2
                        inter2_time=round(inter2_time)
                        days,hours,minutes=self.time_difference(arr2,arr)
                        days_transit,hours_transit,minutes_transit=self.time_difference(dept2,arr)
                        time_transit=hours_transit+(minutes_transit/60)
                        time_transit=round(time_transit,2)
                        total_Journey_time=inter1_time+inter2_time+time_transit
                        #total_Journey_time=inter1_time+inter2_time

                        if total_Journey_time>total_time:
                            continue
                        if days==-1:
                            continue
                        if hours<4 and hours>1:
                            temp=[]
                            temp.append(t)
                            temp.append(i)
                            temp.append(inter1_time)
                            temp2=[]
                            temp2.append(k)
                            temp2.append(j)
                            temp2.append(inter2_time)
                            temp3=[]
                            temp3.append(temp)
                            temp3.append(temp2)
                            temp3.append(total_Journey_time)
                            temp3.append(time_transit)

                            self.final_routes.append(temp3)
                    #if (len(self.final_routes))>=5:
                        #break
                except:
                    continue
                #print("END_LOOP1")

        return self.display()
    def create_tuple(self,i):
        temp=[]
        temp2=[]
        temp.append(self.src)
        temp.append(i)
        temp2.append(i)
        temp2.append(self.dest)
        temp3=[]
        temp3.append(temp)
        temp3.append(temp2)
        self.routes.append(temp3)

def generate_trains(src,dest,night_shift,journey_date,train_type):
    cus65=Book_Ticket(src,dest,night_shift,journey_date,train_type)
    x = cus65.alternate_train()
    print(x)
    return x

#for i in intern
#source to intermediate = ["tr1","tr2","tr3"]
#intermediate to desti = ["tr5","tr6","tr7"]