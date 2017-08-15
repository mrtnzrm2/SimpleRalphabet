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
		self.outputfile = r.TFile('%s.root'%(OutputName),"recreate")
		self.workspace = r.RooWorkspace("w","workspace")
		#category = r.RooCategory("sample","sample")
		#H = self.simpleRal_v1()
		H = self.simpleRal_v2()
		self.setWorkspace(H)
	def simpleRal_v2(self , name="pseudocat"):
		rooH=[]
		min_ = self.histograms[0].GetXaxis().GetBinLowEdge(1)
		max_ = self.histograms[0].GetXaxis().GetBinUpEdge(self.histograms[0].GetXaxis().GetNbins())
		self.a1 = r.RooRealVar("m","m", self.axis1min, self.axis1max)
		#print int(min_),max_
		lVar2 = r.RooRealVar("pt", "pt", int(min_),int(max_))			
		self.a2 = lVar2
		lHist = r.RooArgList()
                if self.axis2for is not "":
			self.a2 = r.RooFormulaVar("DecoVar_"+name, "DecoVar_"+name,self.axis2for,r.RooArgList(lVar2,self.a1))
		for n in range(1,self.histograms[0].GetNbinsX()+1):
			lHist.add(self.a2)
		self.a1.Print()
		self.a2.Print()
		for h,n in zip(self.histograms,range(len(self.histograms))):
			fH = r.RooParametricHist("RooParametricHist_"+name+str(n),"RooParametricHist_"+name+str(n), self.a1 ,  lHist, h)
			rooH.append(fH)
		return rooH

	def simpleRal_v1(self , name="pseudocat"):
		rooH=[]
		min_ = self.histograms[0].GetXaxis().GetBinLowEdge(1)
		max_ = self.histograms[0].GetXaxis().GetBinUpEdge(self.histograms[0].GetXaxis().GetNbins())
		self.a1 = r.RooRealVar("m","m", self.axis1min/100, self.axis1max/100)
		#print int(min_),max_
		lVar2 = r.RooRealVar("pt", "pt", int(min_),int(max_))			
		self.a2 = lVar2
		lHist = r.RooArgList()
                if self.axis2for is not "":
			self.a2 = r.RooFormulaVar("DecoVar_"+name, "DecoVar_"+name,self.axis2for,r.RooArgList(self.a1,lVar2))
		for n in range(1,self.histograms[0].GetNbinsX()+1):
			lHist.add(self.a2)
		self.a1.Print()
		self.a2.Print()
		for h,n in zip(self.histograms,range(len(self.histograms))):
			fH = r.RooParametricHist("RooParametricHist_"+name+str(n),"RooParametricHist_"+name+str(n), self.a1 ,  lHist, h)
			rooH.append(fH)
		return rooH
	def setWorkspace(self, lHis):
		for lh in lHis:
			getattr(self.workspace,'import')(lh,r.RooFit.RecycleConflictNodes())	
		self.workspace.writeToFile(self.output+"_.root")
