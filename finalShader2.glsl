
float cristian() {
	return -1.0;
};
float jaja(float);
vec3 jeje(vec4 v);
float derivative(float t, float epsilon) {
	return 0.5 * (jaja(t+epsilon) - jaja(t-epsilon));
}
float jaja(float t) {
	return 0.5 * t * t - t + 1.0;
}
vec3 jeje(vec4 n) {
	return n.xyz;
}