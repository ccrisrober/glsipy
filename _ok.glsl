#version 430

out vec4 fragColor;

float position(float);
vec3 normal(vec4 v);
float derivative(float t, float epsilon) {
	return 0.5 * (position(t+epsilon) - normal(vec4(vec3(t-epsilon), 1.0));
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
const vec3 vampiro = vec3(6.0, 6.0, 6.0);
struct PointLight {
	vec3 position;
	vec3 diffuse;
	vec3 ambient;
};
vec3 omg() {
	return vec3(1.0);
}

void main() {
	vec3 omg = omg();
	float dev = derivative(omg.x, omg.y);
	fragColor = normal(vec4(vampiro, dev));
}