import re

import win32gui
import mss

class WebcamWindowInfo(object):
	def __init__( self, title, bounds ):
		self.title = title
		self.bounds = bounds # (top, left, right, bottom)

	def get_bounds_dict_tlwh( self ):
		return dict(
			top = window.bounds[0],
			left = window.bounds[1],
			width = window.bounds[2]-window.bounds[1],
			height = window.bounds[3]-window.bounds[0]
		)

def find_webcam_windows( title_search_expressions ):
	window_data = dict( keywords=title_search_expressions, matches=[] )
	win32gui.EnumWindows( _is_webcam_window, window_data )
	results = [ WebcamWindowInfo(
		win32gui.GetWindowText( m ),
		win32gui.GetClientRect( m )
	) for m in window_data['matches'] ]
	return results

def _is_webcam_window( window_handle, extra ):
	title = win32gui.GetWindowText( window_handle )
	for keyword in extra['keywords']:
		if keyword.search(title) != None:
			extra['matches'].append( window_handle )

def capture_region_to_file( region, filename ):
	with mss.mss() as sct:
		sct_img = sct.grab(region)
		mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)

if __name__ == '__main__':
	windows = find_webcam_windows([
		re.compile('skype',re.I),
		re.compile('hangout',re.I),
		re.compile('zoom',re.I),
		re.compile('notepad',re.I)
	])

	for window in windows:
		print('Capturing window: %s' % window.title)
		capture_region_to_file( window.get_bounds_dict_tlwh(), 'capture.png' )
