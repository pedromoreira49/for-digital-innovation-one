from setuptools import setup

with open("README.md", "r") as f:
	page_description = f.read()


setup(
	name="operation_mat",
	version="0.0.1",
	author="Pedro Moreira",
	description="Operações básicas de matemática",
	long_description=page_description,
	long_description_content_type="text/markdown",
	url="",
	python_requires='>=3.4',
)