countC=0
countG=0
DNA=open("vivi.txt").read()
totallength=len(DNA)

for i in range(len(DNA)):
    if DNA[i]=="C":
        countC=countC+1.00

    if DNA[i]=="G":
        countG=countG+1.00

print"Total number of C+G strands: ",(countC+countG)
print"Total number of DNA: ",len(DNA)
print"The percentage of C+G is: ", (((countC+countG)/totallength)*100)
