precision mediump float;
#pragma glsipy: Material = require(./material.glsl)
#pragma glsipy: Light = require(./light.glsl)
#pragma glsipy: blinnPhong = require(./blinn.glsl)

void main() {
	vec3 color = vec3(0,0,0);
	gl_FragColor = vec4(color, 1.0);
}