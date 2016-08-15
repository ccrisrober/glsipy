#!/usr/bin/python
'''
Copyright (c) 2016, maldicion069 (Cristian Rodríguez) <ccrisrober@gmail.con>
//
Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.
//
THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''

import re, os

class ModuleData:
	def __init__(self, name, content):
		self.name = name.replace(" ", "")
		self.content = content
	def __str__(self):
		return "{\n\tName=" + self.name + ", \n\tContent=" + str(self.content) + "\n}"

class ShaderCompiler:
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

	import_modules = dict()

	def __match__(self, items, line):
		for item in items:
			v = re.match(item, line)
			if not v is None:
				return v
		return None

	def __format_key__(self, key):
		return key.replace("\"", "").replace('\'', "")

	def __format_values__(self, values):
		if(len(values) > 0):
			values = [x.replace(" ", "") for x in values]
			values = dict(s.split('=') for s in values)
		else: 
			values = dict()
		return values

	def __init__(self):
		self.frag_repeat = []

	def read_file(self, file, exit_src, minification):
		self.frag_repeat = []

		dir_path = os.path.dirname(os.path.realpath(os.getcwd() + "/" + file)) + "/../"
		#print "dir_path=>" + dir_path
		#print "dpath=>" + "C:\Users\maldicion069\Desktop\glsify python"
		
		content = ''.join(self.__read_file__(dir_path, file, False))
		
		with open(exit_src, 'w') as file_:
			if minification is True:
				content = content.split("\n");
				file_.write(content[0] + "\n")
				del content[0]
				content = "".join(content).replace('\t', ' ')
			file_.write(content)
		'''
		pt = os.path.dirname(os.path.abspath(file))
		print "dir_path=>" + dir_path
		print "file=>" + file
		print "pt=>" + pt
		'''

	def __read_file__(self, dir_path, file, is_module, mod = "", others = []):
		file = (dir_path + "/" + file)
		#print file
		#return [file]
		#print mod
		if is_module:
			#print mod + "~>" + file
			if mod in ShaderCompiler.import_modules:
				#print(mod + " repeated")
				return ShaderCompiler.import_modules[mod].content 
		with open(file, "r") as ins:
			array = []
			for line in ins:

				if line.startswith("#pragma glsipy:"):
					v = self.__match__(ShaderCompiler.items1, line)
					if not v is None:
						if not v.group(1) in self.frag_repeat:
							self.frag_repeat.append(v.group(1))
							values = v.group(2).split(",")
							key = self.__format_key__(values[0])
							del values[0]
							pt = os.path.dirname(os.path.abspath(file))
							#print pt
							array += self.__read_file__(pt, key, True, v.group(1), self.__format_values__(values))
				elif line.startswith("#pragma export"):
					v_ = self.__match__(ShaderCompiler.items2, line)
					if not v_ is None:
						for k, v in others.items():
							array = [s.replace(k, v) for s in array]
				else:
					array.append(line)

			if is_module:
				v = self.__match__(ShaderCompiler.items3, line)	# line value is the last value of file
				if not v is None:
					ShaderCompiler.import_modules[v.group(1)] = ModuleData(file, array)

			return array



# End of shaderimport.py