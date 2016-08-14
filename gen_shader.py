#!/usr/bin/python

import sys

from shaderimport import *

ss = ShaderCompiler()

def str2bool(v):
	return v.lower() in ("yes", "true", "t", "1", "True", "Yes", "T")

if __name__ == "__main__":

	#if len(sys.argv) == 4:

	entry_src = "./examples/jaja.glsl"	#sys.argv[1]
	exit_src = "_ok.glsl"			#sys.argv[2]
	minification = False			#str2bool(sys.argv[3])
	
	ss.read_file(entry_src, exit_src, minification)