#!/bin/bash

# Author: Yoko Parks
# Class:  CSCD 330 Tony Espinoza 
# Date:   23 April 2025



#VARIABLES:
usr_confirm=""
proceed=false
test_num=3


#STORED DOMAINS:
dmn1=poptropica.com       #Personal Favorite of all time
dmn2=bsideportfolio.com #Boo's Portfolio (Pls check it out)
dmn3=oldnet.com           #An older website


# INITIAL USER PROMPT:
while [ "$proceed" = false ]

do
   echo -ne "Please Start The Python Server Before Starting! \n"
   sleep 1
   echo -ne "Is The Server Started? (Y or N): "
   read usr_confirm 

# Server Is Started & Testing Can Begin
   if [[ "$usr_confirm" == [Yy] ]]; then
      proceed=true

   clear # Clear Garbage from Terminal

   echo -ne "Executing API Tests \r"
   sleep 1
   echo -ne "Executing API Tests. \r"
   sleep 1
   echo -ne "Executing API Tests.. \r"
   sleep 1
   echo -ne "Executing API Tests... \r"

   echo -ne " \n"
   sleep 1


   for((i = 1; i < test_num + 1; i++));

   do

   domain_var="dmn$i"
   domain="${!domain_var}"

   echo -ne "******************************* \n"
   echo -ne "Starting Test $i: $domain \n"
   echo -ne "******************************* \n"

# Commands Used to Call API
   curl localhost:5000/address/"$domain"
   curl localhost:5000/range/"$domain"
   echo -ne " \n"
   curl localhost:5000/weather/"$domain"
   sleep 3

# DeadSpace to Seperate Test Cases
   echo -ne " \n"
   echo -ne " \n"



   done



# Do if Server Isn't Started
   elif [[ "$usr_confirm" == [Nn] ]]; then
      echo -ne ""



# Error Condition Handling
   else
      echo -ne "Invalid Input Detected. Try Again... \n"
      sleep 2 




fi #EoCondition Block
done #EoProgram
   
     
