import numpy as np

class TimeSeries:
    '''
    TimeSeries object class
    Defines time series
    '''
    def __init__(self, t, y):
        '''
        Time series object initiation with 
        t and y as lists or 1D arrays.
        If t is a scalar, then the array is 
        autogenerated with scalar value as dt.
        '''
        if (type(t) == float) or (type(t) == int):
            t = np.arange(0.0, len(y)*t-1E-5*t, t)
        self.t = t
        self.y = y

    def setTunit(self, unit):
        '''
        Set unit for T(time) coordinates.
        Unit should be a string.
        '''
        self.tunit = unit

    def setYunit(self, unit):
        '''
        Set unit for y coordinates.
        Unit should be a string.
        '''
        self.yunit = unit

    def sett(self, coords):
        '''
        Set T(time) coordinates.
        Should be a list or numpy array (1D)
        '''
        self.t = coords

    def setEqName(self, name):
        ''' Set earthquake name '''
        self.eqName = name

    def setEqDate(self, date):
        ''' Set earthquake date '''
        self.eqDate = date

    def setStation(self, station):
        ''' Recording station '''
        self.station = station

    def setComponent(self, comp):
        ''' Directional component of record '''
        self.component = comp

    def setDt(self, dt):
        ''' Time step between data points '''
        self.dt = dt

    def setNpts(self, npts):
        ''' Total number of points in the record '''
        self.npts = npts

    def setFilepath(self, filepath):
        ''' Record filepath '''
        self.filepath = filepath
        
