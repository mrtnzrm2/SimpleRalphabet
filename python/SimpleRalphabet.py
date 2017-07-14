import ROOT as r
from multiprocessing import Process
from optparse import OptionParser
from operator import add
import math
import sys
import time
import array
import re
from ROOT import std,RooDataHist

class SimpleRalphabet:
	def __init__(self , Set_Of_Input_Histograms , Axis1Min , Axis1Max , Axis2Formula="" , OutputName="test", name="ps"):
		self.histograms = Set_Of_Input_Histograms
		self.axis1min = Axis1Min
		self.axis1max = Axis1Max
		self.axis2for = Axis2Formula
		self.output = OutputName
		self.a1 = r.RooRealVar("Axis1_"+name,"a1_"+name, self.axis1min, self.axis1max)
		self.outputfile = r.TFile('%s.root'%(OutputName),"recreate")
		self.workspace = r.RooWorkspace("w","workspace")
		#category = r.RooCategory("sample","sample")
		H = self.simpleRalphabet()
		#H[0].Print()
		#xframe = r.RooPlot("a","a",self.a1,self.axis1min,self.axis1max,50)
		#H[0].plotOn(xframe)
		#xframe.Draw()
		self.setWorkspace(H)

	def simpleRalphabet(self , name="pseudocat"):
		rooH=[]
		min_ = self.histograms[0].GetXaxis().GetBinLowEdge(1)
		max_ = self.histograms[0].GetXaxis().GetBinUpEdge(self.histograms[0].GetXaxis().GetNbins())
		self.a2 = r.RooRealVar("Axis2_"+name, "a2_"+name, min_,max_)
		lHist = r.RooArgList()
		for n in range(1,self.histograms[0].GetNbinsX()+1):
			lHist.add(self.a2)
		for h,n in zip(self.histograms,range(len(self.histograms))):
			#print h,n
			fH = r.RooParametricHist("RooParametricHist_"+name+str(n),"RooParametricHist_"+name+str(n), self.a1 ,  lHist, h)
			#self.a1.Print()
			#self.a2.Print()
			#if self.axis2for is not "":
                        #	DecorVar = r.RooFormulaVar("DecoVar_"+name, "DecoVar_"+name ,self.axis2for, r.RooArgList(self.a1,self.a2))
			#	fH = r.RooParametricHist("RooParametricHist_"+name+str(n),"RooParametricHist_"+name+str(n), self.a1 , r.RooArgList(DecorVar), h)
			#fH.getNorm()	
			rooH.append(fH)
		return rooH
	def setWorkspace(self, lHis):
		for lh in lHis:
			getattr(self.workspace,'import')(lh,r.RooFit.RecycleConflictNodes())	
			#workspace.import(lh)
		self.workspace.writeToFile(self.output+"_.root")
