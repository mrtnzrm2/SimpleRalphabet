from SimpleRalphabet import SimpleRalphabet
import ROOT as r

r.gROOT.SetBatch()

c1 = r.TCanvas("a","a",200,400)
#gaussian_50 = TF1("gaussian_50","r.Gaus(x,50,25)",0,100)
#h1 = r.TH2F("a","a",50,0,100,5,200,1000)
#h2 = r.TH2F("b","b",50,0,100,5,200,1000)
#h3 = r.TH2F("c","c",50,0,100,5,200,1000)
#h4 = r.TH2F("d","d",50,0,100,5,200,1000)
h1 = r.TH1F("a","a",50,0,100)
h2 = r.TH1F("b","b",50,0,100)
h3 = r.TH1F("c","c",50,0,100)
h4 = r.TH1F("d","d",50,0,100)
H=[h1,h2,h3,h4]
rand = r.TRandom()
for h in H:

	for i in range(10000):
		#p = 1
		#r.gBenchmark.Start( 'fillrandom' )
		rand.SetSeed(i)
		p = rand.Uniform(0,100)
		#print p
		h.Fill(p)	
#	h.FillRandom("gaus",10000)

#H[0].Draw()
#c1.SaveAs("he1.pdf")
#H[1].Draw()
#c1.SaveAs("he2.pdf")


#SimpleRalphabet(H,0,100,Axis2Formula="@0*@1")
SimpleRalphabet(H,0,100)


