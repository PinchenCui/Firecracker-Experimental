import os
import sys
import string

path1 = "/home/auresearch/Firecracker/kernel.conf"
path2 = "/home/auresearch/Firecracker/coreos.conf"

if len(sys.argv) == 3:
    path1 = sys.argv[1]
    path2 = sys.argv[2]

dic = {}
diff = []
new = []
conf1 = open(path1,"r")
conf2 = open(path2,"r")

data1 = conf1.readlines()
data2 = conf2.readlines()

for line in data1:
    if line.startswith("#") or line.startswith("\n") or not line:
        continue
    else:
        s_line = line.split("=")
        dic[s_line[0]] = s_line[1].strip()

for line in data2:
    if line.startswith("#") or line.startswith("\n") or not line:
        continue
    else:
        s_line = line.strip("\n").split("=")
        if s_line[0] not in dic:
            new.append(line.strip("\n"))
        else:
            if dic[s_line[0]] != s_line[1]:
                tmp = line.strip("\n") +", was, " + dic[s_line[0]]
                diff.append(tmp)

print "Total ", len(new), " new configurations."
print "Total ", len(diff), " different configurations."
print "Total ", len(diff)+len(new), " different entries."

print "_______________________________________________________________________________"
print "New configurations in second file:"
print "###"
for n in new:
    print n
print "_______________________________________________________________________________"
print "Different configurations in second file:"
print "###"

for d in diff:
    print d

print "_______________________________________________________________________________"
print "Total ", len(new), " new configurations."
print "Total ", len(diff), " different configurations."
print "Total ", len(diff)+len(new), " different entries."
