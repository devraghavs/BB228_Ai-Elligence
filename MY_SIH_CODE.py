import requests
import json
import time
from datetime import datetime
FMT = '%H:%M:%S'
f = open('ALL_Train_Schedule.json',) 
trn_sch = json.load(f) 
f=open('All_train_from_a_station.json')
all_trn=json.load(f)
f=open('train_arr_dept.json')
trn_arr_dept=json.load(f)
f=open('All_Station_Nearbuy.json')
stat_neig=json.load(f)

class Book_Ticket():
    routes=[]
    final_routes=[]
    def __init__(self,src,dest):
        self.source=src
        self.destination=dest
        self.src=self.station_name_to_code(src)  #station code call
        self.dest=self.station_name_to_code(dest) 
        if self.src=="NOT" or self.dest=="NOT":  #IF STATION CODE NOT FOUND
            print("______________________________Check Your Staion Name Again________________________________")
    def display(self):
        print("NO. OF POSSIBLE ALTERNATE ROUTE USING 1 STOPOVER =",len(self.final_routes))
        counter=1
        for i in self.final_routes:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print()
            part1=i[0]
            part2=i[1]
            print("Route-",counter)
            print()
            print(part1[1][0],"-------->",part1[1][1])
            print("Train No-",part1[0])
            print("-------------------------------------------------------")
            print()
            print(part2[1][0],"-------->",part2[1][1])
            print("Train No-",part2[0])
            print()
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            counter+=1
    def train_between_station(self,src,dest):
        #src= source staion code
        #dest= destination station code
        
        train_number=[]
        url = "http://indianrailapi.com/api/v2/TrainBetweenStation/apikey/0fe3b963408929419d6d519b06fd4110/From/"+src+"/To/"+dest+"/"
        response = requests.get(url)
        data=response.text
        
        if data[17:20]!='200':        #CASE:- NO Train Exist Between SrC and DEST Gives status Code:- 201     
            return None
        
        # print(data[])
        parsed=json.loads(data)
        #print(json.dumps(parsed, indent=4))
        date=parsed['Trains']
        #print(date)
        for i in date:
            train_number.append(i['TrainNo'])
        #train_number=list(set(train_number)-set(exception))
        return train_number
    
    def station_name_to_code(self,name,flag=0):
        url =" http://indianrailapi.com/api/v2/StationNameToCode/apikey/0fe3b963408929419d6d519b06fd4110/StationName/"+name+"/"
        response = requests.get(url)
        # print(response) successfully
        data=response.text
        # print(data[])
        parsed=json.loads(data)
        #print(json.dumps(parsed, indent=4))
        code=parsed['Station']['StationCode']
        if code==None:
            if flag==1:
                return "NOT"
            name=name.upper()+" "+"JN"
            flag=1
            return self.station_name_to_code(name,flag)
        #print([code,name])
        return code
    
    def train_no_to_station(self,trn_num):
        return [i[0] for i in trn_sch[trn_num]]
    
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
    
    def alternate_train(self):
        inter_stat=self.poss_station()
        for i in inter_stat:
            self.create_tuple(i)
        for i,j in self.routes:
            #print("_________MAIN LOOP___________")
            trn_list_p1=self.train_between_station(i[0],i[1])
            trn_list_p2=self.train_between_station(j[0],j[1])
            if trn_list_p1==None:
                continue
            if trn_list_p2==None:
                continue
            #print(trn_list_p1)
            for t in trn_list_p1:
                #print("LOOP1")
                #print(t)
                try:
                    arr,dept=trn_arr_dept[t][i[1]] 
                    #print(arr,dept,end="$$$$$$$$\n")
                    for k in trn_list_p2:
                        if t==k:
                            continue
                        #print("LOOP2")
                        #print(k)
                        arr2,dept2=trn_arr_dept[k][i[1]]
                        #print(arr2,dept2,end="$$$$$$$$\n")
                        td = datetime.strptime(arr2, FMT) - datetime.strptime(arr, FMT)
                        #print("END_LOOP2")
                        days = td.days
                        hours, remainder = divmod(td.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        # If you want to take into account fractions of a second
                        seconds += td.microseconds / 1e6
                        if hours<4:
                            temp=[]
                            temp.append(t)
                            temp.append(i)
                            temp2=[]
                            temp2.append(k)   
                            temp2.append(j)
                            temp3=[]
                            temp3.append(temp)
                            temp3.append(temp2)
                            self.final_routes.append(temp3)
                    if (len(self.final_routes))>=5:
                        break
                except:
                    continue
                #print("END_LOOP1")
        self.display()
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
    
cus5=Book_Ticket("New Delhi","Chittaurgarh")
cus5.alternate_train()

#for i in intern
#source to intermediate = ["tr1","tr2","tr3"]
#intermediate to desti = ["tr5","tr6","tr7"]