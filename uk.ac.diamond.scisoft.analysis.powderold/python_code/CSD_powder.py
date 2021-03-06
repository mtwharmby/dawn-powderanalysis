from ccdc.io import EntryReader
from ccdc.descriptors import PowderPattern
import numpy as np
import sys
class CSD_powder:
    """
    CSD_powder class
    #######################
    this class calculates d_spacing, intensities and two theta for a specific crystal
    
    Attributes
    -------------
    
    entry [ccdc entry reader method]
    crystal_name str the name of a crystal of form 'AABHTZ'
    
    Methods
    ---------------
    
    __init__()
    ---------------
    takes 2 arguments self,name [str]
    sets crystal name
    
    load_d_space()
    ---------------
    uses name atr
    calls ccdc PowderPattern class
    calculates d_spacing using braggs law
    
    returns d_space[list of d_spacing], intensities[list of peak intensities]
    
    load_intensities()
    ------------------
    uses name atr
    calls ccdc PowderPattern class
    returns list[intensities]
    
    load_two_theta()
    -------------------
    uses name atr
    calls ccdc PowderPattern class
    returns list[two theta angles]
    """
    
    def __init__(self):
        self.entry = EntryReader('CSD')
        
        
    def get_crystal_name(self):
        return self.crystal_name
    
    def set_crystal_name(self,value):
        self.crystal_name = value
    
    def load_d_space(self):
        # creates a d_space list with intensities as a second option
        crystal = self.entry.crystal(self.crystal_name)
        pattern = PowderPattern.from_crystal(crystal)
        self.wavelength = PowderPattern.Wavelength.Wavelength_CuKa1
        peak_thetas = []
        #intents = pattern.intensity
        two_t = pattern.two_theta
        intents = pattern.intensity # all pattern intensity
        intensity = [] # final list of intensities
        for i in pattern.tick_marks:
            l = i.two_theta # two theta vals
            for j,I in zip(two_t,intents):
                if abs(l-j) < 0.01:
                    # compare lists and find peak 2theta values the above assumption may be changed
                    peak_thetas.append(j) # tick two theta val
                    intensity.append(I) # add the intensity of those peaks to a list
                    break
        d_space = [] # list of d_spaces
        peak_thetas = np.array(peak_thetas)/2 # theta vals instead of 2theta
        peak_radians = peak_thetas*np.pi/180 # to radians
        for peak in peak_radians:
            d = self.wavelength/(2*np.sin(peak)) # get the space values in Angstorms
            d_space.append(d) # append final values to a list
            
        return d_space,intensity
    
    def load_intensities(self):
        # loads the intensities of a given crsytal
        crystal = self.entry.crystal(self.crystal_name)
        pattern = PowderPattern.from_crystal(crystal)
        return pattern.intensity
        
    def load_two_theta(self):
        crystal = self.entry.crystal(self.crystal_name)
        pattern = PowderPattern.from_crystal(crystal)
        return pattern.two_theta
    
    def get_data(self,option):
        if option == 1:
            d_space,intensities = self.load_d_space()
            for i,j in zip(d_space,intensities):
                print i,j
        if option == 2:
            """all the data"""
            x1 = self.load_intensities()
            x2 = self.load_two_theta()
            for i,j in zip(x1,x2):
                print i,j
        else:
            sys.exit(1)
        
if __name__ == "__main__":
    crystal = sys.argv[1] # the crystal name
    option = sys.argv[2] # the option
    #crystal = "AABHTZ"
    #option = 2
    pow = CSD_powder()
    pow.set_crystal_name(crystal)
    pow.get_data(option)
