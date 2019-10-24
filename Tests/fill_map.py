import sys
import xml.etree.ElementTree as ET
import matplotlib.cm as cm
import matplotlib.colors as clrs

def graph_color(data, maximum, svg_file):
	tree = ET.parse(svg_file)
	root = tree.getroot()
	gselect = r'{http://www.w3.org/2000/svg}g'
	paths = []

	for p in root.iter(gselect):
			paths.append(p)

	for path in paths:
		try:
			scale = data[path.attrib['id']] / maximum
			s = clrs.rgb2hex(cm.OrRd(scale))
			path.attrib['style'] = 'fill:' + s
		except KeyError:
			continue
	
	tree.write('out1.svg')

def data_pop(csv_file):
	f = open(csv_file, 'r')
	data = {}
	l = []

	f.readline()
	for line in f:
		l = line.strip('\n').split(',')
		data[l[1]] = int(l[6])

	return data

def maximum_pop(csv_file):
	f = open(csv_file, 'r')
	maximum = 0
	data = []
	
	f.readline()
	for line in f:
		data = line.strip('\n').split(',')
		if maximum < int(data[6]):
			maximum = int(data[6])

	return maximum

if __name__ == '__main__':
	csv_file = sys.argv[1]
	svg_file = sys.argv[2]
	data = data_pop(csv_file)
	maximum = maximum_pop(csv_file)
	graph_color(data, maximum, svg_file)
