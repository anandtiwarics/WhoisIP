from ipwhois import IPWhois
import csv

__outFile__ = raw_input("Provide your output File Path with .csv file name: ");

c = csv.writer(open(__outFile__, "wb"))
c.writerow(['IP Address','Country','State','City','Description','Name','Emails','Range'])

__inputFile__ = raw_input("Input your File Path: ");

fileOpne = open( __inputFile__ , 'r')
lines = fileOpne.read().strip().split()

for ip in lines:
    obj = IPWhois(ip)
    out = obj.lookup()

    f = out["nets"][0]['city']
    a = out["nets"][0]['country']
    g = out["nets"][0]['description']
    b = out["nets"][0]['emails']
    h = out["nets"][0]['name']
    rangs = out["nets"][0]['range']
    e = out["nets"][0]['state']

    c.writerow([ip,a,e,f,g,h,b,rangs])

fileOpne.close()
