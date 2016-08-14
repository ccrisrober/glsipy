float position(float t) {
	return 0.5 * t * t - t + 1.0;
}
#pragma glsipy: derivative = require(./derivative.glsl, func = position)