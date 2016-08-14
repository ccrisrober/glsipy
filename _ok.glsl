Conrad "Cronos" Lant

float position(float);
vec3 normal(vec4 v);
float derivative(float t, float epsilon) {
	return 0.5 * (position(t+epsilon) - position(t-epsilon));
}

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

float anthrax() {
	return -1.0;
};
vec3 slayer() {
	return vec3(1.0);
};
VAMPIRO
struct PointLight {
	vec3 position;
	vec3 diffuse;
	vec3 ambient;
};
PAPA, NO ROBES