import re

class ModuleData:
	def __init__(self, name, content):
		self.name = name.replace(" ", "")
		self.content = content
	def __str__(self):
		return "{\n\tName=" + self.name + ", \n\tContent=" + str(self.content) + "\n}"

import_modules = dict()

items1 = [
	re.compile('#pragma glsipy: (.+?) = require\(\'(.+?)\'\)'),
	re.compile("#pragma glsipy: (.+?) = require\(\"(.+?)\"\)"),
	re.compile("#pragma glsipy: (.+?) = require\((.+?)\)")
]
items2 = [
	re.compile('#pragma export\(\'(.+?)\'\)'),
	re.compile("#pragma export\(\"(.+?)\"\)"),
	re.compile("#pragma export\((.+?)\)")
]
items3 = [
	re.compile('#pragma glsipy: export\(\'(.+?)\'\)'),
	re.compile("#pragma glsipy: export\(\"(.+?)\"\)"),
	re.compile("#pragma glsipy: export\((.+?)\)")
]
def match(items, line):
	for item in items:
		v = re.match(item, line)
		if not v is None:
			return v
	return v

def format_key(key):
	return key.replace("\"", "").replace('\'', "")

def format_values(values):
	if(len(values) > 0):
		values = [x.replace(" ", "") for x in values]
		values = dict(s.split('=') for s in values)
	else: 
		values = dict()
	return values

frag_repeat = []

def read_file(file, exit_src, minification):
	global frag_repeat
	frag_repeat = []
	content = __read_file__(file, False)
	content = ''.join( content )
	
	with open(exit_src, 'w') as file_:
		if minification is True:
			content = content.split("\n");
			file_.write(content[0] + "\n")
			del content[0]
			content = "".join(content).replace('\t', ' ')
			file_.write(content)
		else:
			file_.write(content)

def __read_file__(file, is_module, mod = "", others = []):
	#print mod
	if is_module:
		print mod + "~>" + file
		if mod in import_modules:
			print(mod + " repeated")
			return import_modules[mod].content 
	with open(file, "r") as ins:
		array = []
		for line in ins:
			#print line
			if line.startswith("#pragma glsipy:"):
				v = match(items1, line)	#
				if not v is None:
					if not v.group(1) in frag_repeat:
						frag_repeat.append(v.group(1))
						values = v.group(2).split(",")
						key = format_key(values[0])
						del values[0]
						array += __read_file__(key, True, v.group(1), format_values(values))
			elif line.startswith("#pragma export"):
				v = match(items2, line)
				if not v is None:
					for k, v in others.items():
						array = [s.replace(k, v) for s in array]
			else:
				array.append(line)

		if is_module:
			v = match(items3, line)	# line value is the last value of file
			if not v is None:
				import_modules[v.group(1)] = ModuleData(file, array)

		return array

if __name__ == "__main__":
	print "FILE 1"
	read_file("foo.glsl", "finalShader.glsl", False)

	print "FILE 2"
	read_file("demo2.glsl", "finalShader2.glsl", False)

	print "FILE 3"
	read_file("shader.glsl", "finalShader3.glsl", False)
	
	#for k, v in import_modules.items():
	#	print ("KEY= " + k + ", VALUE= " + str(v))
	#print import_modules
