from SimpleRalphabet import SimpleRalphabet
import ROOT as r


h1 = r.TH2F("a","a",50,0,100,5,200,1000)
h2 = r.TH2F("b","b",50,0,100,5,200,1000)
h3 = r.TH2F("c","c",50,0,100,5,200,1000)
h4 = r.TH2F("d","d",50,0,100,5,200,1000)
H=[h1,h2,h3,h4]
pt=0.
m=0.
for h in H:
	for i in range(25000):
		r.gRandom.Rannor(pt,m)
		h.Fill(pt,4*m)

SimpleRalphabet(H,0,100,"@0+@1")


