import sys

def translate(path):
	first = True

	with open("output.xml", 'wb') as g:
		with open(path, 'rb') as f:
			for line in f:
				if "<" in line:
					if first:
						g.write("<style name=\"\" parent=\"@android:style/Widget." + line.strip()[1:].split()[0] + "\">\n")
						first = False
						continue
				else:
					if "@+id" in line:
						continue
					parts = line.strip().split("=")
					if "/>" in line:
						parts[1] = parts[1][:-2]
					g.write("\t<item name=\"" + parts[0] + "\">" + parts[1][1:-1] + "</item>\n")

			g.write("</style>")


if __name__ == "__main__":
	translate(sys.argv[1])
