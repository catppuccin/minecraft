#version 120

#include "shaders.settings"

varying vec2 texcoord;
uniform sampler2D gcolor;
uniform sampler2D gaux4;

vec3 colorLUT(vec3 color, sampler2D lut, int palette) {
    color = round(color * 63.0);

    float u = color.r + mod(color.g, 8.0) * 64.0;
    float v = color.b * 8.0 + floor(color.g / 8.0);
    vec2 lutcoord = vec2(u, v) / 512.0;
    
    vec2 offset = vec2(mod(float(palette), 2.0), floor(float(palette) / 2.0));
    lutcoord += offset;
    lutcoord /= 2.0;

	return texture2D(lut, lutcoord).rgb;
}

void main() {
	vec3 color = texture2D(gcolor, texcoord).rgb;
	color = colorLUT(color, gaux4, flavour);
	gl_FragData[0] = vec4(color, 1.0);
}
