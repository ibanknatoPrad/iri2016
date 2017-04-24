#!/usr/bin/env python
req = ['nose','numpy','scipy','matplotlib','seaborn','pathlib2',]
pipreq=['timeutil']
# %%
import pip
try:
    try:
        import conda.cli
        conda.cli.main('install',*req)
    except Exception:
        pip.main(['install',*req])
    pip.main(['install',*pipreq])
except Exception: # py27
    pass
# %%
import setuptools # enables develop
from numpy.distutils.core import Extension, setup
from glob import glob
from os.path import join

name = 'pyiri2016'
sourcePath = 'source'
f77CompileArgs = ['-w']

iriSource1 = ['iriwebg.for', 'irisub.for', 'irifun.for',
    'iritec.for', 'iridreg.for', 'igrf.for', 'cira.for', 'iriflip.for']

sources1 = [join(sourcePath, s) for s in iriSource1]

ext1 = Extension(name='iriweb', sources=sources1, 
                 f2py_options=['--quiet','skip:','dfridr',':'],
                 extra_f77_compile_args=f77CompileArgs)


ccirData = glob(join(join('data', 'ccir'), '*.asc'))
igrfData = glob(join(join('data', 'igrf'), '*.dat'))
indexData = glob(join(join('data', 'index'), '*.dat'))
mcsatData = glob(join(join('data', 'mcsat'), '*.dat'))
ursiData = glob(join(join('data', 'ursi'), '*.asc'))


iriDataFiles = [(join(name, join('data', 'ccir')), ccirData),
                (join(name, join('data', 'igrf')), igrfData),
                (join(name, join('data', 'index')), indexData),
                (join(name, join('data', 'mcsat')), mcsatData),
                (join(name, join('data', 'ursi')), ursiData)
                ]

if __name__ == '__main__':

    setup(name=name,
          packages=[name],
        version='1.2.0',
        author=['Ronald Ilma','Michael Hirsch, Ph.D.'],
        url = 'https://github.com/rilma/pyIRI2016',
        description='IRI2016 International Reference Ionosphere via Python',
        classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering :: Atmospheric Science',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          ],
        ext_package=name,
        ext_modules=[ ext1 ],
        data_files=iriDataFiles,
        install_requires=req+pipreq,
        dependency_links=[
      'https://github.com/rilma/TimeUtilities/zipball/master#egg=timeutil']
        )
