import pandas as pd
import numpy as np
import geopandas
from geopandas import GeoDataFrame, GeoSeries
import shapely
import fiona
from shapely.geometry import Point, Polygon
from geopandas.tools import sjoin
import matplotlib.pyplot as plt

def points2geo(data, lat, lon):
	coords = GeoSeries([Point(x, y) for y, x in zip(data[lon], data[lat])])
	data['geometry'] = coords
	data.index = [i for i in range(len(data))]
	return GeoDataFrame(data)

def main():
	# Read in Data
	grid = GeoDataFrame.from_file(igrid)
	points = pd.read_csv(ipoints)

	# create geopoints
	geopoints = points2geo(points, lat, lon)

	# match projection info:
	## Points - should already be in wgs84
	geopoints.crs =wgs84
	geopoints['geometry'] = geopoints['geometry'].to_crs(epsg=4326)
	## Grid - project from meters to wgs84
	grid.crs = gridproj
	grid['geometry'] = grid['geometry'].to_crs(epsg=4326)
	# create uid to groupby 
	grid['id'] = [i for i in range(len(grid))] 

	# Spatial join points to grid
	join_inner_df = sjoin(grid, geopoints, how="inner")
	# Group by the uid and geometry - return mean
	join_inner_df = join_inner_df.groupby(['id','geometry'])['Decibel'].mean()
	# join_inner_df = join_inner_df.groupby(['id','geometry'])['Decibel'].max()

	# Create geodataframe & reset the index of the file
	output = GeoDataFrame(join_inner_df)
	output = output.reset_index()

	# output

	# write to file
	output.to_file(ofile)

if __name__ == '__main__':

	# igrid = '/Users/Jozo/Dropbox/UBC/_RA/Geo311/data/grid/hexgrid100m.shp'
	igrid = '~/geog311-noisemapping/data/input/grid/SquareGrid/grid10m.shp'
	ipoints = '~/geog311-noisemapping/data/input/noise/2015/csv/GEOG311-Noise-2015.csv'

	lat = "Latitude"
	lon = "Longitude"

	gridproj = {'init': 'epsg:3740', 'no_defs': True}
	wgs84 = {'datum':'WGS84', 'no_defs':True, 'proj':'longlat'}

	# set output directory
	odir = '~/geog311-noisemapping/data/input/noise/2015/_gridavgs/10m'
	ofile = odir+ ipoints.split('/')[-1][:-4]+"_gridavg_10m.shp"

	main()



