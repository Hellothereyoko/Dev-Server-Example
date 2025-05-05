# Author: Yoko Parks
# Class:  CSCD 330 EWU Tony Espinoza
# Date:   24th April 2025


# About The Program:
This Program is a Python FLASK web-server that hosts a self-made API. 
It is an iteration of The Weather API from last week.
It takes a domain via a curl call and passes it into several APIs & code. 
From there, the program will return: the physical 
address, network range, and the weather for the physical address. If
the same domain is queried, the data is stored in a cache for future reuse.

The functions inscribed in the program are as followed:

address: fetches address of domain
range: returns network range of the domain 
weather: fetches weather info for physical address associated with the domain


# Syntax:
	curl localhost:5000/<function>/<domain>


# Example:
	curl localhost:5000/address/google.com
	curl localhost:5000/range/google.com
	curl localhost:5000/weather/google.com




##################################################
#             Laboratory Questions:              #
##################################################

# 1) Identify in the URL: http://localhost:5000/weather/google.com

Domain: localhost
Path: weather/google.com
Port: 5000
Protocol: HTTP 


# 2) Identify in the URL: https://translate.google.com/

Domain: google.com
SubDomain: translate
TLD: .com
Path: /
Port: 443
Protocol: HTTPS


# 3) What is a Python Decorator?

A function that takes another as an argument and returns it
with increased functionality without changing its code. It can do stuff
like authentication, logging, memorization, etc.


# 4) Is there any problem with your cache implementation? Would your cache implementation work in production?

Yes, there are a couple of issues. I don't limit cache size due to
the simplicity of the app. So, if someone queried thousands of domains
I would eventually run out of memory. Second, I have no safeguards to
prevent data racing. This cache is global; so all users could access it.
A couple of the issues are simple enough to fix but session storing will
take a lot of work before it's ready.
