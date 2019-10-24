import sys
import xml.etree.ElementTree as ET
import matplotlib.cm as cm
import matplotlib.colors as clrs

def graph_color(data, area, max_pop, max_area, svg_file):
	tree = ET.parse(svg_file)
	root = tree.getroot()
	gselect = r'{http://www.w3.org/2000/svg}g'
	paths = []

	for p in root.iter(gselect):
			paths.append(p)
	
	denom = max_pop / max_area

	for path in paths:
		try:
			scale = (data[path.attrib['id']] / area[path.attrib['id']]) / denom
			s = clrs.rgb2hex(cm.OrRd(scale))
			path.attrib['style'] = 'fill:' + s
		except KeyError:
			continue
	
	tree.write('out1.svg')

def data_pop(csv_file):
	f = open(csv_file, 'r')
	data = {}
	area = {}
	l = []

	f.readline()
	for line in f:
		l = line.strip('\n').split(',')
		data[l[1]] = int(l[6])
		area[l[1]] = int(l[5])

	return data, area

def maximum_pop(csv_file):
	f = open(csv_file, 'r')
	max_pop = 0
	max_area = 0
	data = []
	
	f.readline()
	for line in f:
		data = line.strip('\n').split(',')
		if max_area < int(data[5]):
			max_area = int(data[5])
		if max_pop < int(data[6]):
			max_pop = int(data[6])

	return max_pop, max_area

if __name__ == '__main__':
	csv_file = sys.argv[1]
	svg_file = sys.argv[2]
	data = data_pop(csv_file)
	maximum = maximum_pop(csv_file)
	graph_color(data[0],data[1], maximum[0], maximum[1], svg_file)
