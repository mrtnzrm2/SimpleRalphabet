import ROOT as r
from multiprocessing import Process
from optparse import OptionParser
from operator import add
import math
import sys
import time
import array
import re

class SimpleRalphabet:
	def __init__(self , Set_Of_Input_Histograms , Axis1Min , Axis1Max , Axis2Formula="" , OutputName="test", name="pseudocat"):
		self.histograms = Set_Of_Input_Histograms
		self.name = name
		self.axis1min = Axis1Min
		self.axis1max = Axis1Max
		self.axis2for = Axis2Formula
		self.output = OutputName
		self.a1 = r.RooRealVar("Axis1_"+self.name,"a1_"+self.name, self.axis1min, self.axis1max)
		outputfile = r.TFile('%s.root'%(OutputName),"recreate")
		workspace = r.RooWorskspace("test")
		category = r.RooCategory("sample","sample")
		H = self.simpleRalphabet()
		self.setWorkspace(H,workspace)

	def simpleRalphabet(self , name="pseudocat"):
		rooH=[]
		for h,n in (self.histograms,len(self.histograms)):
			min = h.GetXaxis().GetBinLowEdge(1)
			max = h.GetXaxis().GetBinUpEaaadge(h.GetXaxis().GetNbins())
			self.a2 = r.RooRealVar("Axis2_"+name+str(n), "a2_"+name+str(n), min, max)
			fH = self.createRooParametricHist("RooParametricHist_"+name+str(n),"RooParametricHist_"+name+str(n), self.a1 , r.RooArgList(self.a2) , h)
			if self.axis2for is not "":
                        	DecorVar = r.RooFormulaVar("DecoVar_"+name, self.axis2for, r.RooArgList(self.a1,self.a2))
				fH = r.RooParametricHist("RooParametricHist_"+name+str(n),"RooParametricHist_"+name+str(n), self.a1 , r.RooArgList(DecorVar), h)
			rooH.append(fH)
		return rooH
	def setWorkspace(self, lHis, workspace , name="workspace"):
		for lh in lHis:
			getattr(workspace,'import')(lh,r.RooFit.RecycleConflictNodes())	
		workspace.writeToFile(self.output+"_"+name)
