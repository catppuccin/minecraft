#version 120

varying vec2 texcoord;
varying vec4 color;

void main() {
	gl_Position = ftransform();
	texcoord = (gl_MultiTexCoord0).xy;
	color = gl_Color;
}
