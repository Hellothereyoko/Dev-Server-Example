
<div align="center">
	
# $${\color{red}About} {} {\color{red}The} {} {\color{red}Program:}$$

</div>

<br>
This Program is a Python FLASK web-server that hosts a self-made API. 
It is an iteration of The Weather API from last upload.
It takes a domain via a curl call and passes it into several APIs & application code. 
From there, the program will return: the physical 
address, network range, and the weather for the physical address. If
the same domain is queried, the data is stored in a cache for future reuse.


The functions inscribed in the program are as followed:

- address: fetches address of domain
- range: returns network range of the domain 
- weather: fetches weather info for physical address associated with the domain

</br>


<div align="center">
	
# $${\color{red}Syntax:}$$

</div>

	curl localhost:5000/<function>/<domain>


<div align="center">
	
# $${\color{red}Example:}$$

</div> 

	curl localhost:5000/address/google.com
	curl localhost:5000/range/google.com
	curl localhost:5000/weather/google.com




