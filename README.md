# BB228_Ai-Elligence

# Problem Statement:
"AI Based Reservation System"

# Description: 
Getting quicker and earliest booking in Indian Railways system is sometimes a challenge for passengers. The challenge is to devise an optimization using latest technologies which improves probability of getting ticket, improve booking time and customer experience remarkably. Expectation from solution are

(1) Once passenger enters origin and destination, probable options and alternatives should be provided to 
    him, within predefined/limited time frame. This should help passenger in getting confirm seat. 
(2) Additional functionality could be added to help passenger getting confirmed seats, improve booking time. 
(3) Data available in public domain/internet can be used by students to approach problem.

# Organization: Ministry of Railways

# Concept:

The aim is to provide confirmed tickets to the passengers in minimum travelling time and to provide technology which improves  probability of getting tickets . When the passenger enters origin  and destination, a list of all the possible routes will appear to the user .This will help the passenger to opt for the best route to reach his destination in less journey time .
The key concept used in finding the alternate routes between source and destination is to find the intersection of the in-between station of source and destination  and  applying the constraints like time, fare etc. by using an algorithm. It will further help in the optimization and provide the user with a list of alternative routes. Additionally, we are implementing the route rank concept using reinforcement learning, so the 
user will get the most suitable route. 

# Detailed Description:
Datasets:
  All Train Schedule
  Intermediate Stations
  Arrival Departure of Trains
API’s:
  Train between Station i.e. Source and Destination
  Station name to Station code
  Train Fare
  Train Live Status
  
Features:
  User will get probable options and alternative routes.
  User can choose the train types.
  Route ranking: 
  Optimized with the help of reinforcement learning
  
Constraints:

  Time constraint according to Journey Time
  No. of  Stops
  Day/Night Stop
  Fare
  
# Optimization:
  We have optimised our algorithm by reducing the complexity and decreasing the execution time of the code .It is achieved through various steps:

-->>Pre Computation of  Data - Initially we were fetching our data from API’s  but now we have stored our data locally to reduce the amount of  time  used to fetch the data .

-->>Caching- A cache is a high-speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster than is possible by accessing the data’s primary storage location. Caching allows us to efficiently reuse previously retrieved or computed data.

Conquering the difficulties faced by the Indian Railways system with respect to booking, we have effectively executed the initial step of our proposed solution. This progression would give simplicity to the passengers in getting a confirmed booking when they enter the origin and destination, by giving probable options and alternatives routes to reach their desired destination.
 
 Our Algorithim is optimize and precise and able to find the most efficient alternative routes between source and destination within seconds.
 
 
 # THANK YOU !! 



