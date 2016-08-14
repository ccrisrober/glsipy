precision mediump float;
struct Material {
	vec3 color;
	float kAmbient, kDiffuse, kSpecular;
	float phongExponent;
};
struct PointLight {
	vec3 position;
	vec3 diffuse;
	vec3 ambient;
};
float cristian() {
	return -1.0;
};
vec3 blinnPhong (Material material, PointLight light) {
	return vec3(0.0);
}

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