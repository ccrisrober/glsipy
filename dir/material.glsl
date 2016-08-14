struct Material {
	vec3 color;
	float kAmbient, kDiffuse, kSpecular;
	float phongExponent;
};
#pragma glsipy: export(Material)