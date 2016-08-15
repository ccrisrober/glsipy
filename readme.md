# glsipy
Python module based on glsify.
```bash
python gen_shader.py input output minification
```
- input: Shader input file (String)
- output: Shader output file (String)
- minification: Enable/disable minification (True/False)

## Example
```bash
python gen_shader.py entry.glsl output.glsl False
```

## How to use

### Define module export:
```glsl
#pragma glsipy: export(<ModuleName>)
```

### Import module:
Module name same as previous module export section
```glsl
#pragma glsipy: <ModuleName> = require("./<route>")
```

### Higher-order function
- Define module export
```glsl
# example.glsl
float func(float);
vec3 func2(vec4 v);
float derivative(float t, float epsilon) {
	return 0.5 * (func(t+epsilon) - func(t-epsilon));
}
#pragma export(example)
```
- Import module export
```glsl
#pragma glsipy: example = require('./example.glsl', func = myfunc, func2 = phongShading)
float myfunc(float t) {
	return 0.5 * t * t - t + 1.0;
}
vec3 phongShading(vec4 n) {
	return n.xyz;
}
```