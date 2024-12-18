import requests  
  
domain = "google.com"  
  
file = open("wordlist.txt")  
content = file.read()  
subdomains = content.splitlines()  
  
discovered = []  
for subdomain in subdomains:  
    url = "https://{}.{}".format(subdomain, domain)  
  
try:  
  requests.get(url)  
except:  
  pass  
else:  
  discovered.append(url)  

for subdomain in discovered:  
  print(subdomain)