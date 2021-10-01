r=open("intern input.txt","r")
w=open("intern output.txt","w")

que=['who','what','when','where', "why", "how", "can", "does", "do"]
que_set=set(que)
data=r.readlines()

for line in data:
    line_=line.split()
    line_set=set(line_)
    if line_set.intersection(que_set):
        text=(line.replace("\n"," ") +" \tYes"+"\n")
        w.write(text)
    else:
        text = (line.replace("\n"," ") + " \tNo"+"\n")
        w.write(text)

r.close()
w.close()