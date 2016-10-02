#version 430

out vec4 fragColor;

#pragma glsipy: Demo = require('./demo/demo.glsl')
#pragma glsipy: Omg = require('./omg.glsl')

void main() {
	vec3 omg = omg();
	float dev = derivative(omg.x, omg.y);
	fragColor = normal(vec4(vampiro, dev));
}