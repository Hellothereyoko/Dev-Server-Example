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




