float func(float);
vec3 func2(vec4 v);
float derivative(float t, float epsilon) {
	return 0.5 * (func(t+epsilon) - func2(vec4(vec3(t-epsilon), 1.0));
}
#pragma export(derivative)