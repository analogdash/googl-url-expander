import urllib.request

input  = open("in.txt", "r") 
output = open("out.txt", "w")

for line in input:
    output.write(urllib.request.urlopen(line).geturl())
    print(line)

output.close()
input.close()
