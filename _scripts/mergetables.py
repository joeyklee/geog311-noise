import numpy as np
import pandas as pd
import geopandas
from geopandas import GeoDataFrame
lefter = pd.read_csv('/Users/Jozo/Dropbox/UBC/Geo311/data/joined/popd_da.csv')
righter = pd.read_csv('/Users/Jozo/Dropbox/UBC/Geo311/data/joined/income.csv')
census_data = pd.merge(lefter, righter, left_on="DAUID", right_on="COL0")
census_data.columns = ['DAUID', 'PRUID', 'CDUID', 'DANAME', 'Pop11', 'TotPriv', 'OccPriv', 'Areakm2', 'PopD', 'GeoId', 'NHHNFNR', 'MedHVal', 'AvgHVal', 'TotHHI', 'MedHHI', 'AvgHHI', 'MedHHItax', 'AvgHHItax']

das = GeoDataFrame.from_file('/Users/Jozo/Dropbox/UBC/Geo311/data/census2011/da/boundaries/MVAN_da_2011_carto.shp')

output = GeoDataFrame.merge(das, census_data, on="DAUID")

output.to_file('/Users/Jozo/Dropbox/UBC/Geo311/data/joined/census2011.shp')


'''
'CCSNAME' -
'CCSUID' -
'CDNAME' -
'CDTYPE' -
'CDUID_x' -
'CMANAME' -
'CMAPUID' -
'CMATYPE' -
'CMAUID' -
'CSDNAME' -
'CSDTYPE' -
'CSDUID' -
'CTNAME' -
'CTUID' -
'DAUID' -
'ERNAME' -
'ERUID' -
'PRNAME' -
'PRUID_x' -
'SACCODE' -
'SACTYPE' -
'geometry' -
'PRUID_y' -
'CDUID_y' -
'DANAME' -
'Pop11' - Population 2011
'TotPriv' - total private dwellings
'OccPriv' - private dellings occuoied by usal residents
'Areakm2' - land area in sq km
'PopD' - population density (Pop11 / Areakm2)
'GeoId' - GEO UID
'NHHNFNR' - Number of owner households in non-farm non-reserve private dwellings
'MedHVal' - Median value of dwellings ($)
'AvgHVal' - Average value of dwellings ($)
'TotHHI' - Household income in 2010 of private households
'MedHHI' - Median household total income $
'AvgHHI' - Average household total income $
'MedHHItax' - Median after-tax household income $
'AvgHHItax' - Average after-tax household income $

'''