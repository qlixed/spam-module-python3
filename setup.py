from distutils.core import setup, Extension

spam_module = Extension('spam',
		sources = ['spam.c'])

setup ( name = 'Spam',
	version = '1.0',
	description = 'Sample module.',
ext_modules = [ spam_module ])
