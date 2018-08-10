from shutil import copyfile
import os
python=3.6 ##3.7 or 3.6
win=64 ##32 or 64 ##32 not in use atm



if (python==3.7 and win==64):
	inputdir='C:/Development/fmipp/msvc_py37-64/'
	outputdir='C:/Development/py-fmipp-py37-64/'
	sundialsdir='C:/Tools/sundials-2.5.0-install/lib/'
	boostdir='C:/local/boost_1_64_0/lib64-msvc-14.1/'
elif (python==3.6 and win==64):
	inputdir='C:/Development/fmipp/msvc_py36-64/'
	outputdir='C:/Development/py-fmipp-py36-64/'
	sundialsdir='C:/Tools/sundials-2.5.0-install/lib/'
	boostdir='C:/local/boost_1_64_0/lib64-msvc-14.1/'
##endif


##no changes should be needed below except for the boost library names

copyfile(inputdir + 'import/swig/fmippim.py', outputdir + 'fmipp/fmippim.py')
copyfile(inputdir + 'export/swig/fmippex.py', outputdir + 'fmipp/export/fmippex.py')

copyfile(inputdir + 'export/swig/Release/_fmippex.pyd', outputdir + 'fmipp/lib/_fmippex.pyd')
copyfile(inputdir + 'import/swig/Release/_fmippim.pyd', outputdir + 'fmipp/lib/_fmippim.pyd')

copyfile(inputdir + 'Release/fmippim.dll', outputdir + 'fmipp/lib/fmippim.dll')
copyfile(inputdir + 'Release/fmippex.dll', outputdir + 'fmipp/lib/fmippex.dll')

copyfile(sundialsdir + 'sundials_cvode.lib', outputdir + 'fmipp/lib/sundials_cvode.lib')
copyfile(sundialsdir + 'sundials_nvecserial.lib', outputdir + 'fmipp/lib/sundials_nvecserial.lib')

copyfile(boostdir + 'boost_filesystem-vc141-mt-1_64.dll', outputdir + 'fmipp/lib/boost_filesystem-vc141-mt-1_64.dll')
copyfile(boostdir + 'boost_system-vc141-mt-1_64.dll', outputdir + 'fmipp/lib/boost_system-vc141-mt-1_64.dll')

'''
if (win==64):
	if (os.path.isdir(outputdir + 'test/zigzag/binaries/win64/')==False):
		makedirs(outputdir + 'test/zigzag/binaries/win64/')
	copyfile(inputdir + 'test/zigzag/binaries/win64/zigzag.dll', outputdir + 'test/zigzag/binaries/win64/zigzag.dll')
	copyfile(inputdir + 'test/zigzag/binaries/win64/givezero.dll', outputdir + 'test/zigzag/binaries/win64/givezero.dll')
##elif (win=32):
'''

copyfile(inputdir + 'Release/fmi2.dll', outputdir + 'fmipp/export/bin/fmi2.dll')
copyfile(inputdir + 'Release/libfmipp_fmu_frontend.lib', outputdir + 'fmipp/export/bin/libfmipp_fmu_frontend.lib')






