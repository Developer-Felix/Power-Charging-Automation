# Power Charging Automation
We are going to create a system to automate the charging phones in the streats were people suffer from charging 
due to lack of places to charge.
This system we are going to write code for the app that one will mae payments from and the point were he will 
put the code for the access to charging. This pace will be a physical place were there will be a keyboard to
to input the code.

# Logic

## Client Payment App or Web based side
- At this side the will be one page or one screen that disp‬lays the button options for which plan you are choosing 
the examples of plans will be 10 minutes which is Sh. 10 , 20 minutes will be sh.20, 30 minutes should be 30 shillings and upto 50 minutes
- Ones User clicks the plan it will pop up the modal or screen to recieve phone number which will send the stk push to the phone . Once there
is a successfull payment the user will be send with a 4 digit random code that will be used to get access to a charging port once the user gets 
the physical charging groud. The backend should have table to store Payments data which  has phone number, access code  and minutes paid for. There
will be another table for the devices and the location. that we will explain in the client charging side.


## Client Charging side and recieving code side

This place we will have a keyboard to recive the 4 digit code that the customer was given after the payments. 
once the user inputs the 4 digits code there system should be able to allocate the user a charging port that is 
empty to start charging and once the charging minutes is over the port is disabled and no charging should take place. 
Each charging location shoud have 50 charging ports for phones and there should be table to relate the code with the 
devices. They should share the backend.

we will design two systems one with django and the other with python terminal. The code should query one database.
This means we should have a django api for the client charging with is terminal to query the django database that will be in the frontend sides.
