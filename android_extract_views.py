import os, sys

def getTargetDirectory(path):
	for dirpath, dirnames, filenames in os.walk(path):
		for dirs in dirnames:
			if dirs == "layout" and os.path.split(dirpath)[-1] == "res":
				return os.path.join(dirpath, dirs)

def extractViewCode(path):
	views = dict()
	lookForId = False
	with open(path, "rb") as f:
		for line in f:
			line = line.strip()
			if line == "":
				continue;
			if line[0] == "<" and line[1] != "/":
				view = (line.split(" ")[0])[1:]
				lookForId = True
			if "android:id" in line and lookForId:
				raw = line.split("=")[1].strip()
				viewId = raw[raw.index("id/") + 3:-1]
				views[viewId] = view
				lookForId = False
	declaration = ["View v; //The parent view of all other views. Unnecessary in Activities\n"]
	findView = ["v = this.findViewById(android.R.id.content\n"]
	for view in views:
		print "Found View: ", views[view], "\nwith id:", view
		varName = ("".join([c.title() for c in (''.join(c if c.isalnum() else " " for c in view)).split(" ")]))
		varName = varName[0].lower() + varName[1:]
		declaration.append(views[view] + " " + varName + ";\n")
		findView.append(varName + " = v.findViewById(R.id." + view + ");\n")
	return declaration+ ["\n"] + findView


if __name__ == "__main__":
	project = os.path.abspath(sys.argv[1])
	print "Searching directory:\n", project, "..."

	lines = []
	target = getTargetDirectory(project)
	for filename in os.listdir(target):
		if filename.split(".")[-1] == "xml":
			lines.append("/*====================================================\n" + filename + "\n====================================================*/\n")
			lines += extractViewCode(os.path.join(target, filename))
			lines.append("\n")

	with open("outputCode.java", "wb") as f:
		f.writelines(lines)



