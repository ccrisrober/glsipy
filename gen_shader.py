import re


class ModuleData:
	def __init__(self, name, content):
		self.name = name.replace(" ", "")
		self.content = content
	def __str__(self):
		return "{\n\tName=" + self.name + ", \n\tContent=" + str(self.content) + "\n}"

import_modules = dict()


def match1(line):
	v = re.match(re.compile('#pragma glsipy: (.+?) = require\(\"(.+?)\"\)'), line)
	if v is None:
		v = re.match(re.compile("#pragma glsipy: (.+?) = require\(\'(.+?)\'\)"), line)
		if v is None:
			v = re.match(re.compile("#pragma glsipy: (.+?) = require\((.+?)\)"), line)
	return v

def match2(line):
	v = re.match(re.compile("#pragma export\(\'(.+?)\'\)"), line)
	if v is None:
		v = re.match(re.compile("#pragma export\(\"(.+?)\"\)"), line)
		if v is None:
			v = re.match(re.compile("#pragma export\((.+?)\)"), line)
	return v

def read_file(file, is_module, mod, others = []):
	#print mod
	if is_module:
		#print mod + " " + file
		if mod in import_modules:
			print(mod + " repeated")
			return import_modules[mod].content 
	with open(file, "r") as ins:
		array = []
		for line in ins:
			#print line
			if line.startswith("#pragma glsipy:"):
				v = match1(line)
				if not v is None:
					if not v.group(1) in import_modules:
						values = v.group(2).split(",")
						key = values[0]
						del values[0]
						array = array + read_file(key, True, v.group(1), values)
			elif line.startswith("#pragma export"):
				v = match2(line)
				if not v is None:
					print v.group(1)
					a = [x.replace(" ", "") for x in others]

					d = dict(s.split('=') for s in a)
					for k, v in d.items():
						array = [s.replace(k, v) for s in array]
			else:
				array.append(line)

		if is_module:
			pass
			#print line
			v = re.match(r"#pragma glsipy: export\((.+?)\)", line)
			#print v.group(1)
			if not v is None:
				import_modules[v.group(1)] = ModuleData(file, array)

		return array

if __name__ == "__main__":
	content = read_file("shader.glsl", False, "")

	# Remove lines who contains "#pragma"
	content = [line for line in content if not line.startswith("#pragma")]

	content = ''.join( content )
	#print ("-----------------------------");
	#print ("-----------------------------");
	#print ("-----------------------------");
	#print ("-----------------------------");
	#print ("-----------------------------");
	#print (content)

	with open('finalShader.glsl', 'w') as file_:
		#content = content.split("\n");
		#file_.write(content[0] + "\n")
		#del content[0]
		#content = "".join(content)
		#content = content.replace('\t', ' ')
		#print (content)
		#file_.write(content)
		print (content)
		file_.write(content)
	
	#for k, v in import_modules.items():
	#	print ("KEY= " + k + ", VALUE= " + str(v))
	#print import_modules