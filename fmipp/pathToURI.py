# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

try:
	import urlparse, urllib
except:
	pass
try: # python 3
	import urllib.parse as urlparse, urllib.request as urllib
except:
	pass

# Convert path to URI.
def pathToURI( path ):
	return urlparse.urljoin( 'file:', urllib.pathname2url( path ) )


# Concatenate two paths and return URI of resulting path
def concatPathsToURI( path1, path2 ):
	import os.path
	return urlparse.urljoin( 'file:', urllib.pathname2url( os.path.join( path1, path2 ) ) )
