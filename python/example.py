from SimpleRalphabet import SimpleRalphabet
import ROOT as r


#h1 = r.TH2F("a","a",50,0,100,5,200,1000)
#h2 = r.TH2F("b","b",50,0,100,5,200,1000)
#h3 = r.TH2F("c","c",50,0,100,5,200,1000)
#h4 = r.TH2F("d","d",50,0,100,5,200,1000)
h1 = r.TH1F("a","a",50,0,100)
h2 = r.TH1F("b","b",50,0,100)
h3 = r.TH1F("c","c",50,0,100)
h4 = r.TH1F("d","d",50,0,100)
H=[h1,h2,h3,h4]
pt=0.
m=0.
for h in H:
	for i in range(25000):
		r.gRandom.Rannor(r.Double(pt),r.Double(m))
		h.Fill(pt)

SimpleRalphabet(H,0,100,"@0+@1")


