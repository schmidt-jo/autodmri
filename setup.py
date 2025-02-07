from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='autodmri',
    version='0.2.6',
    author='Samuel St-Jean',
    packages=find_packages(),
    scripts=['scripts/autodmri_get_distribution'],
    url='https://github.com/samuelstjean/autodmri',
    license='MIT',
    description='Implementation of "Automated characterization of noise distributions in diffusion MRI data".',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy>=1.10',
                      'scipy>=0.19',
                      'joblib>=0.12',
                      'nibabel>=2.2'],
)
