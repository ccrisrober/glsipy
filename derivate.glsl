float func(float);
float func2(float);
float exec(float t, float eps) {
	return func(t * eps) * func2(eps);
}
#pragma export(exec)