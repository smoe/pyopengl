'''OpenGL extension EXT.shader_framebuffer_fetch

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.shader_framebuffer_fetch to provide a more 
Python-friendly API

Overview (from the spec)
	
	Conventional OpenGL blending provides a configurable series of operations
	that can be used to combine the output values from a fragment shader with
	the values already in the framebuffer. While these operations are
	suitable for basic image compositing, other compositing operations or
	operations that treat fragment output as something other than a color
	(normals, for instance) may not be expressible without multiple passes or
	render-to-texture operations.
	
	This extension provides a mechanism whereby a fragment shader may read
	existing framebuffer data as input. This can be used to implement
	compositing operations that would have been inconvenient or impossible with
	fixed-function blending. It can also be used to apply a function to the
	framebuffer color, by writing a shader which uses the existing framebuffer
	color as its only input.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/shader_framebuffer_fetch.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.shader_framebuffer_fetch import *
from OpenGL.raw.GLES2.EXT.shader_framebuffer_fetch import _EXTENSION_NAME

def glInitShaderFramebufferFetchEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION