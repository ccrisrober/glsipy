
#pragma glsipy: Cristian = require('./cristian.glsl')
#pragma glsipy: Cristian = require('./cristian.glsl')
#pragma glsipy: Cristian = require('./cristian.glsl')
#pragma glsipy: derivative = require('./derivative.glsl', func = jaja, func2 = jeje)
float jaja(float t) {
	return 0.5 * t * t - t + 1.0;
}
vec3 jeje(vec4 n) {
	return n.xyz;
}