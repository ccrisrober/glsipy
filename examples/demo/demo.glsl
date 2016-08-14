Conrad "Cronos" Lant

#pragma glsipy: derivative = require('./../derivative.glsl', func = position, func2 = normal)

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

#pragma glsipy: Anthrax = require('./anthrax.glsl')
#pragma glsipy: PointLight = require('./../light.glsl')
#pragma glsipy: export(Demo)