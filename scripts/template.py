import sys

fn = (sys.argv[1]) if (len(sys.argv)>1) else "template_input"

with open(fn) as f:
    content = f.readlines()

flag = "out"
cname = ""
f = None

for i in range(0, len(content)):
	if (content[i][0] == "#"):
		continue
	elif (content[i].find(":")>0):
		if (flag == "in"):
			open("_" + cname, "w").write(f)
		name = content[i].replace(":", "").replace("\n", "")
		cname = name
		flag = "in"
		f = open(name).read()
		print f
	else:
		keys = content[i].strip().replace(" ", "").split("->")[0].split(" ")
		values = content[i].strip().replace(" ", "").split("->")[1].split(" ")
		print keys
		print values
		for j in range(0, len(keys)):
			f = f.replace("{" + keys[j] + "}", values[j])

if (flag == "in"):
			open("_" + cname, "w").write(f)



