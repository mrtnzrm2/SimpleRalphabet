# SimpleRalphabet
Simple (Linear) version of Ralphabet

#### PsuedoCode:
List of Classes:
  SimpleRalphabet(Set_Of_Input_Histograms, Axis1Min, Axis1Max, Axis2Formula, OutputName):
    # Ralphabet should work in any two variables, which I'll call Axis1 and Axis2 (e.g. pT and rho). Initializes with a set of input TH1Fs (Set_Of_Input_Histograms), starting and ending bins in the first Axis (Axis1Min, Axis1Max), a Ralphabet-Variable formula (Axis2Formula) which is a string telling us how to calculate the deccorrelation-variable matrix (e.g. if Axis1 is pT and Axis2 is mass, then you would pass "log((a2*a2)/(a1*a1))" if we wanted to use rho as our second deimension of decorrelation, or just "a2" if we wanted to use mass as our second axis of decorrelation) and a name to be used for outputs (OutputName).
    # The inputs should be seperated into bins of Axis1, with the actual x-axis of the histograms representing the variables we'll set a limit in Axis2.
    # Create RooRealVars that we'll need:
    min = Set_Of_Input_Histograms[somebody].GetMin() # Find the start of the analysis bins (range of the limit essentially)
    max = Set_Of_Input_Histograms[somebody].GetMax() # Find the end of the analysis bins
    self.a1 = RooRealVar("Axis1_"+name, "a1", Axis1Min, Axis1Max)
    self.a2 = RooRealVar("Axis2_"+name, "a2"+name, min, max)
    self.DecorVar = RooFormulaVar("DecoVar_"+name, Axis2Formula, RooArgList(self.a1, self.a2))
    # Create the Array of values in the decorrelation matrix:
  




List of Functions:
  createRooParametricHist(name, var, bins, bin_map)
  # Takes (string, RooRealVar, {RooRealVars or RooFormulaVars}, TH1F)
  # Creates a RooParametricHist (A COMBINE object for storing complex "histogram-like" objects) which will have a name (name), an x-axis variable (var), which is what variable the limit or measurement is computed in e.g. jet mass, Z' resonance mass, etc... a set of bins (bins) which can be RooRealVars or RooForumlaVars; this set is ordered but really just a set of numbers without defined binning. Said binning is defined by the TH1F (bin_map) which is passed: the first RooSomethingVar goes into the first bin, the second in to the second bin, etc... until the whole RooParametricHist is filled:
    RPH = RooParametricHist(name, name, var, bins, bin_map)
    return RPH
