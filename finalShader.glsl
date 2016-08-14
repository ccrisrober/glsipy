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
