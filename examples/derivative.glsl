float func(float);
vec3 func2(vec4 v);
float derivative(float t, float epsilon) {
	return 0.5 * (func(t+epsilon) - func(t-epsilon));
}
#pragma export(derivative)