import re

class ModuleData:
	def __init__(self, name, content, replaces):
		self.name = name.replace(" ", "")
		self.content = content
		self.replaces = replaces
	def __str__(self):
		return "{Name=" + self.name + ", Content=" + str(self.content) + ", Replaces=" + str(self.replaces) + "}"

import_modules = dict()

regexes = [
	re.compile("#pragma export\(\'(.+?)\'\)"),
	re.compile("#pragma export\(\"(.+?)\"\)"),
	re.compile("#pragma export\((.+?)\)")
]

def match1(rgs, line):
	v = re.match(re.compile('#pragma glsipy: (.+?) = require\(\"(.+?)\"\)'), line)
	if v is None:
		v = re.match(re.compile("#pragma glsipy: (.+?) = require\(\'(.+?)\'\)"), line)
		if v is None:
			v = re.match(re.compile("#pragma glsipy: (.+?) = require\((.+?)\)"), line)
	return v

def match2(rgs, line):
	v = re.match(re.compile("#pragma export\(\'(.+?)\'\)"), line)
	if v is None:
		v = re.match(re.compile("#pragma export\(\"(.+?)\"\)"), line)
		if v is None:
			v = re.match(re.compile("#pragma export\((.+?)\)"), line)
	return v

def read_file(file, is_module, mod):
	if is_module:
		#print mod + " " + file
		if mod in import_modules:
			print(mod + " repeated")
			return [] #import_modules[mod].content 
	with open(file, "r") as ins:
		array = []
		for line in ins:
			#print line
			if line.startswith("#pragma glsipy:"):
				v = match1([], line)
				if not v is None:
					#print v.group(1) + "=>" + v.group(2)
					#print import_modules.keys()
					#if not v.group(1) in import_modules:
					array = array + read_file(v.group(2), True, v.group(1))
			else:
				array.append(line)

		if is_module:
			#print line
			v = re.match(r"#pragma glsipy: export\((.+?)\)", line)
			#print v.group(1)
			import_modules[v.group(1)] = ModuleData(file, array, dict())

		return array

if __name__ == "__main__":
	content = read_file("shader.glsl", False, "")

	# Remove lines who contains "#pragma"
	content = [line for line in content if not line.startswith("#pragma")]

	content = ''.join( content )
	print ("-----------------------------");
	print ("-----------------------------");
	print ("-----------------------------");
	print ("-----------------------------");
	print ("-----------------------------");
	print (content)
	#for k, v in import_modules.items():
	#	print ("KEY= " + k + ", VALUE= " + str(v))
	#print import_modules