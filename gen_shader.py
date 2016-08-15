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

import sys

from shaderimport import *

ss = ShaderCompiler()

def str2bool(v):
	return v.lower() in ("yes", "true", "t", "1", "True", "Yes", "T")

if __name__ == "__main__":

	'''
	entry_src = "./examples/jaja.glsl"
	exit_src = "_ok.glsl"
	minification = False
	
	ss.read_file(entry_src, exit_src, minification)
	'''

	if len(sys.argv) == 4:
		entry_src = sys.argv[1]
		exit_src = sys.argv[2]
		minification = str2bool(sys.argv[3])
		
		ss.gen_file(entry_src, exit_src, minification)