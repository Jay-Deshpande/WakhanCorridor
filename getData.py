import pandas as pd
#import matplotlib.pyplot as plot

pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('gtdbcsv.csv', low_memory=False)
# delete these unnecessary columns
colForDel = [
	'approxdate',
	'extended',
	'resolution',
	'country',
	'country_txt',
	'region',
	'region_txt',
	'multiple',
	'related',
	'attacktype2',
	'attacktype2_txt',
	'attacktype3',
	'attacktype3_txt',
	'targsubtype1',
	'targsubtype1_txt',
	'corp1',
	'target1',
	'targtype2',
	'targtype2_txt',
	'targsubtype2',
	'targsubtype2_txt',
	'corp2',
	'target2',
	'natlty2',
	'natlty2_txt',
	'targtype3',
	'targtype3_txt',
	'targsubtype3',
	'targsubtype3_txt',
	'corp3',
	'target3',
	'natlty3',
	'natlty3_txt',
	'gsubname',
	'gname2',
	'gsubname2',
	'gname3',
	'gsubname3',
	'guncertain2',
	'guncertain3',
	'nperpcap',
	'claimed',
	'claimmode',
	'claimmode_txt',
	'compclaim',
	'claim2',
	'claimmode2',
	'claimmode2_txt',
	'claim3',
	'claimmode3',
	'claimmode3_txt',
	'motive',
	'nkillus',
	'nwoundus',
	'propvalue',
	'propcomment',
	'nhostkidus',
	'nhours',
	'ndays',
	'divert',
	'kidhijcountry',
	'ransom',
	'ransomamt',
	'ransomamtus',
	'ransompaid',
	'ransompaidus',
	'ransomnote',
	'addnotes',
	'scite1',
	'scite2',
	'scite3',
	'INT_IDEO',
	'INT_MISC',
	'INT_ANY',
	'dbsource',
	'weaptype2',
	'weaptype2_txt',
	'weapsubtype2',
	'weapsubtype2_txt',
	'weaptype3',
	'weaptype3_txt',
	'weapsubtype3',
	'weapsubtype3_txt',
	'weaptype4',
	'weaptype4_txt',
	'weapsubtype4',
	'weapsubtype4_txt',
	'property',
	'propextent',
	'propextent_txt',
	'crit1',
	'crit2',
	'crit3',
	'doubtterr',
	'alternative',
	'alternative_txt',
	'guncertain1',
	'individual',
	'vicinity'
]
# get dataframe of Pakistan - idf
afghanDF = df.loc[df['country'] == 44]
# drop unnecessary columns
afghanDF = afghanDF.drop(colForDel, axis=1)
#ax = idf[['attacktype1']].plot(kind='hist', legend=True)
#plot.show()
# get dataframe with certain year
afghanDF = afghanDF.loc[afghanDF['nkill'] > 0]
afghanDF = afghanDF.loc[afghanDF['iyear'] > 1999]
###assassination = idf.loc[idf['attacktype1'] == 1]
#idf.to_csv('/Users/jaydeshpande/Desktop/Geog426/FinalReport/allIsrael.csv', index=False)
#bombings.to_csv('/Users/jaydeshpande/Desktop/Geog426/FinalReport/allBombings.csv', index=False)
#armedAssault.to_csv('/Users/jaydeshpande/Desktop/Geog426/FinalReport/armedAssault.csv', index=False)
#assassination.to_csv('/Users/jaydeshpande/Desktop/Geog426/FinalReport/assassination.csv', index=False)
afghanDF.to_csv('/Users/jaydeshpande/Programming/WakhanCorridor/china2000.csv', index=False)
