import ManageData as md #loads and saves data
import TransformData as td #Cleans and transforms data
import FactorTester as ft #Test factors for suitability in models
import numpy as np
def LoadData(CapRange):
#CapRange can be All, High, Mid, or Low
SaveFile='Data' + CapRange + 'Cap' #Save loaded data in this file
Filename = SaveFile + '.xlsm' #load data in this file
R1 = md.removeloadeddata(SaveFile+'.pkl') #deletes any previously saved
D = md.initialize() #Creats a Python dictionary to store data
D = md.loaddataFormat1(D,Filename)#Load data from spreadsheet
Success = md.saveproject(D,SaveFile+'.pkl') #Saves the loaded data to a pickel file
D = md.loadproject(SaveFile+'.pkl')
return D
Dall = LoadData('Low')
def LoadData(CapRange):
#CapRange can be All, High, Mid, or Low
SaveFile = 'Data' + CapRange + 'Cap' #Save loaded data in this file
Filename = SaveFile + '.xlsm' #load data in this file
R1 = md.removeloadeddata(SaveFile+'.pkl') #deletes any previously saved
D = md.initialize() #Creats a Python dictionary to store data
D = md.loaddataFormat1(D,Filename)#Load data from spreadsheet
Success = md.saveproject(D,SaveFile+'.pkl') #Saves the loaded data to a pickel file
D = md.loadproject(SaveFile+'.pkl')
return D
D=Dall
def LoadData(CapRange):
#CapRange can be All, High, Mid, or Low
SaveFile = 'Data' + CapRange + 'Cap' #Save loaded data in this file
Filename = SaveFile + '.xlsm' #load data in this file
R1 = md.removeloadeddata(SaveFile+'.pkl') #deletes any previously saved
D = md.initialize() #Creats a Python dictionary to store data
D = md.loaddataFormat1(D,Filename)#Load data from spreadsheet
Success = md.saveproject(D,SaveFile+'.pkl') #Saves the loaded data to a pickel file
D = md.loadproject(SaveFile+'.pkl')
return D
def Run_Lab_1(D,SaveFile):
# D could by Dall, Dhigh, Dmid, or Dlow
#SaveFile could be RunNumber_5
TD = {} #Dictionary for transformed data
FA = {} #Dictionary for factors
N = np.int_(5) #Used to control data cleaning, see notes
#Next 4 lines were added so forward returns will be used
Returns_AP = D['Returns_AP'].copy()
TD['ForwardReturns_AP'] = D['ForwardReturns_AP'].copy()

TD['Price_Book_AP'] = -D['Price_Book_AP'].copy() #Change the sign of price to book because high is bad, low is good
TD['Price_Book_AP'] = td.CleanData(TD['Price_Book_AP'],N) #Moderate outliers so model building is better
TransformList = ['ZSBT','ZSCSBS'] #z-score by time, decile crosssection by sector
TD['Price_Book_AP'] = td.Transform(TD['Price_Book_AP'],TransformList,D)
X = TD['Price_Book_AP']
TD.key()
Dall=LoadData ('Low')
D=Dall
TD = {} #Dictionary for transformed data
FA = {} #Dictionary for factors
N = np.int_(5) #Used to control data cleaning, see notes
#Next 4 lines were added so forward returns will be used
Returns_AP = D['Returns_AP'].copy()
TD['ForwardReturns_AP'] = D['ForwardReturns_AP'].copy()
Run
Run_Lab1(Dall,SaveFile)
Run_Lab_1(Dall,SaveFile)
TD = {} #Dictionary for transformed data
FA = {} #Dictionary for factors
N = np.int_(5) #Used to control data cleaning, see notes
#Next 4 lines were added so forward returns will be used
Returns_AP = D['Returns_AP'].copy()
TD['ForwardReturns_AP'] = D['ForwardReturns_AP'].copy()
TD = {} #Dictionary for transformed data
FA = {} #Dictionary for factors
N = np.int_(5) #Used to control data cleaning, see notes
#Next 4 lines were added so forward returns will be used
Returns_AP = D['Returns_AP'].copy()
TD['ForwardReturns_AP'] = D['ForwardReturns_AP'].copy()
D.Keys()
Dall=LoadData ('Low')
D=Dall
def Run_Lab_1(D,SaveFile):
# D could by Dall, Dhigh, Dmid, or Dlow
#SaveFile could be RunNumber_5
TD = {} #Dictionary for transformed data
FA = {} #Dictionary for factors
N = np.int_(5) #Used to control data cleaning, see notes
#Next 4 lines were added so forward returns will be used
Returns_AP = D['Returns_AP'].copy()
TD['ForwardReturns_AP'] = D['ForwardReturns_AP'].copy()
D.Keys()
VMalpha_AP = 1.0*FA['Price_Book_AP']['SignalTile_AP'] + 1.0*FA['STMomentum_AP']['SignalTile_AP'] 
TD['VMalpha_AP'] = VMalpha_AP.copy()
TransformList = ['ZSCSBS']
TD['VMalpha_AP'] = td.Transform(TD['VMalpha_AP'],TransformList,D)
NumTile = 5 #Number of quantiles to use in AnalyzeFactor
FA['VMalpha_AP'] = ft.AnalyzeFactor('VMalpha',TD['VMalpha_AP'],TD['ForwardReturns_AP'],NumTile)
NumPointsS2 = 100 #Number of grid points to search, 100 is usually enough
S2 = ft.Optimize_IRitp_2(TD['Price_Book_AP'],TD['STMomentum_AP'] ,TD['ForwardReturns_AP'],NumPointsS2)
NumPointsS3 = 100 #Number of grid points to search, 100 is usually enough
VMalpha_AP = 1.0*FA['Price_Book_AP']['SignalTile_AP'] + 1.0*FA['STMomentum_AP']['SignalTile_AP'] 
TD['VMalpha_AP'] = VMalpha_AP.copy()
TransformList = ['ZSCSBS']
TD['VMalpha_AP'] = td.Transform(TD['VMalpha_AP'],TransformList,D)
NumTile = 5 #Number of quantiles to use in AnalyzeFactor
FA['VMalpha_AP'] = ft.AnalyzeFactor('VMalpha',TD['VMalpha_AP'],TD['ForwardReturns_AP'],NumTile)
NumPointsS2 = 100 #Number of grid points to search, 100 is usually enough
S2 = ft.Optimize_IRitp_2(TD['Price_Book_AP'],TD['STMomentum_AP'] ,TD['ForwardReturns_AP'],NumPointsS2)
FA['VMalpha_AP'] = ft.AnalyzeFactor('VMalpha',TD['VMalpha_AP'],TD['ForwardReturns_AP'],NumTile)
FA['VMalpha_AP']['ICitp']
#calculate ICITP , combine two variable to get higher

N = np.int_(5)
TD['STMomentum_AP'] = D['STMomentum_AP'].copy()
TD['STMomentum_AP'] = td.CleanData(TD['STMomentum_AP'],N) #Moderate outliers so model building is better
TransformList = ['ZSBT','ZSCSBS'] #z-score by time, decile crosssection by sector
TD['STMomentum_AP'] = td.Transform(TD['STMomentum_AP'],TransformList,D)
NumTile = np.int_(5) #Number of quantiles to use in AnalyzeFactor
FA['STMomentum_AP'] = ft.AnalyzeFactor('STMomentum',TD['STMomentum_AP'],TD['ForwardReturns_AP'],NumTile)


N = np.int_(5)
TD['SurpriseMomentum_AP'] = D['SurpriseMomentum_AP'].copy()
TD['SurpriseMomentum_AP'] = td.CleanData(TD['SurpriseMomentum_AP'] ,N) #Moderate outliers so model building is better
TransformList = ['ZSBT','ZSCSBS'] #z-score by time, decile crosssection by sector
NumTile = 5 #Number of quantiles to use in AnalyzeFactor
TD['SurpriseMomentum_AP'] = td.Transform(TD['SurpriseMomentum_AP'] ,TransformList,D)
FA['SurpriseMomentum_AP'] = ft.AnalyzeFactor('SurpriseMomentum_AP',TD['SurpriseMomentum_AP'] ,TD['ForwardReturns_AP'],NumTile)

N = 5
TD['Month12ChangeF12MEarningsEstimate_AP'] = D['Month12ChangeF12MEarningsEstimate_AP'].copy()
TD['Month12ChangeF12MEarningsEstimate_AP'] = td.CleanData(TD['Month12ChangeF12MEarningsEstimate_AP'],N) #Moderate outliers so model building is better
TransformList = ['ZSBT','ZSCSBS'] #z-score by time, decile crosssection by sector
NumTile = np.int_(5) #Number of quantiles to use in AnalyzeFactor
TD['Month12ChangeF12MEarningsEstimate_AP'] = td.Transform(TD['Month12ChangeF12MEarningsEstimate_AP'],TransformList,D)
FA['Month12ChangeF12MEarningsEstimate_AP'] = ft.AnalyzeFactor('Month12ChangeF12MEarningsEstimate_AP',TD['Month12ChangeF12MEarningsEstimate_AP'] ,TD['ForwardReturns_AP'],NumTile)

VMalpha_AP = 1.0*FA['Price_Book_AP']['SignalTile_AP'] + 1.0*FA['STMomentum_AP']['SignalTile_AP'] 
TD['VMalpha_AP'] = VMalpha_AP.copy()
TransformList = ['ZSCSBS']
TD['VMalpha_AP'] = td.Transform(TD['VMalpha_AP'],TransformList,D)
NumTile = 5 #Number of quantiles to use in AnalyzeFactor
FA['VMalpha_AP'] = ft.AnalyzeFactor('VMalpha',TD['VMalpha_AP'],TD['ForwardReturns_AP'],NumTile)
NumTile = np.int_(5)
FA['Price_Book_AP'] = ft.AnalyzeFactor('Price_Book',TD['Price_Book_AP'],TD['ForwardReturns_AP'],NumTile)
FA['Price_Book_AP'] ['ICitp']


FA['Price_Book_AP'] 
['ICitp']
