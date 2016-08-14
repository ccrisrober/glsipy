precision mediump float;
#pragma glsipy: Material = require("./dir/material.glsl")
#pragma glsipy: PointLight = require('./light.glsl')
#pragma glsipy: Cristian = require('./cristian.glsl')
#pragma glsipy: blinnPhong = require("./blinn.glsl")

#pragma glsipy: derivative = require('./derivative.glsl', func = position, func2 = normal)

void main() {
	vec3 color = vec3(0,0,0);
	gl_FragColor = vec4(color, 1.0);
}
float position(float t) {
	return 0.5 * t * t - t + 1.0;
}
vec3 normal(vec4 n) {
	return n.xyz;
}