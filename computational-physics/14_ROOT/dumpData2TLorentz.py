#! /usr/bin/env python
"""
A program which reads in a simple ascii file
containing particle physics data events. It prints the invariant
mass of the missing four-momenta for the first 10 particles, then
it computes the invariant mass of the four-momenta for various
combinations of particles and histograms them.

Leon Hostetler, Apr. 16, 2017

USAGE: python dumpData2TLorentz.py
"""

from __future__ import division, print_function
from ROOT import TLorentzVector, TCanvas, TFile, TH1F
import sys

# Create a ROOT file
rootFile = TFile("mass_dist.root", "RECREATE")

#
nEvents = 0  # Count the number of events
npip = 0  # Count the number of pi+ particles
neutronMass = []  # Create a list of the neutron masses

beam =  TLorentzVector()  # The beam is the incoming photon
target =  TLorentzVector(0,0,0,0.938)  # The target is a proton at rest
pip = [TLorentzVector(), TLorentzVector()]  # A list containing the vectors for the pair of pi+ particles
pim = TLorentzVector()  # The vector for the pi- particle
neutron = TLorentzVector() # A vector object for the neutron

hn3pi = TH1F("hn3pi", "Mass(n3pi)", 150, -0.1, 0.1)
h3pi = TH1F("h3pi", "Mass(3pi)", 150, 0.8, 2.3)
hpip1pim = TH1F("hpip1pim", "Mass(pip1pim)", 150, 0.2, 1.6)
hpip2pim = TH1F("hpip2pim", "Mass(pip2pim)", 150, 0.2, 1.8)
h2pip = TH1F("h2pip", "Mass(2pip)", 150, 0.2, 2.0)
hnpip1 = TH1F("hnpip1", "Mass(npip1)", 150, 1.0, 3.0)
hnpip2 = TH1F("hnpip2", "Mass(npip2)", 150, 1.0, 2.8)
hnpim = TH1F("hnpim", "Mass(npim)", 150, 1.0,3.0)

#
with open("n3pi.dat", "r") as f:
	# open file and read in ascii events line-by-line
	# the line will contain either the number of particles which indicates start of an event
	# or the line contains particle information: id charge Px Py Pz E
	# 
    for line in f:
        token = line.split()
        tokenValue = int(token[0])
        if tokenValue == 4: 
            if nEvents % 10000 ==0:
                print(nEvents,"\r",end='')
                sys.stdout.flush()
            npip = 0
            nEvents += 1
        elif tokenValue == 1:
            # beam particle
            beam.SetPxPyPzE( float(token[2]), float(token[3]), float(token[4]), float(token[5]) )
        elif tokenValue == 8:
            # piPlus meson 
            pip[npip].SetPxPyPzE(float(token[2]), float(token[3]), float(token[4]), float(token[5]) )
            npip += 1
        elif tokenValue == 9:
            # piMinus meson 
            pim.SetPxPyPzE(float(token[2]), float(token[3]), float(token[4]), float(token[5]) )

        # Now process the event
	if nEvents > 1 and tokenValue == 4: # we have the full event

	    # Calculate invariant mass of neutron
	    neutron = beam + target - (pip[0] + pip[1] + pim)
	    neutronMass += [neutron.Mag()]

	    # Calculate invariant mass [n pi+ pi+ pi-]
	    massn3pi = (neutron + pip[0] + pip[1] + pim).Mag()
	    hn3pi.Fill(massn3pi)

	    # Calculate invariant mass [ pi+ pi+ pi- ]
	    mass3pi = (pip[0] + pip[1] + pim).Mag()
	    h3pi.Fill(mass3pi)

	    # Calculate invariant mass [ pi+1 pi- ]
	    masspip1pim = (pip[0] + pim).Mag()
	    hpip1pim.Fill(masspip1pim)

	    # Calculate invariant mass [ pi+2 pi- ]
	    masspip2pim = (pip[1] + pim).Mag()
	    hpip2pim.Fill(masspip2pim)

	    # Calculate invariant mass [ pi+ pi+ ]
	    mass2pip = (pip[0] + pip[1]).Mag()
	    h2pip.Fill(mass2pip)

	    # Calculate invariant mass [ n pip1 ]
	    massnpip1 = (neutron + pip[0]).Mag()
	    hnpip1.Fill(massnpip1)

	    # Calculate invariant mass [ n pip2 ]
	    massnpip2 = (neutron + pip[1]).Mag()
	    hnpip2.Fill(massnpip2)

	    # Calculate invariant mass [ pi+2 pi- ]
	    massnpim = (neutron + pim).Mag()
	    hnpim.Fill(massnpim)

	    
# Print the first several neutron masses
for i in range(10):
    print("For event", i, "the missing invariant mass is", neutronMass[i])

# Done reading all events from data file
print("\nTotal events read:", nEvents)

cc = TCanvas("cc", "Invariant Mass Distributions", 10, 10, 2400, 3200)
cc.Divide(2,4)
cc.cd(1)
hn3pi.Draw()
cc.cd(2)
h3pi.Draw()
cc.cd(3)
hpip1pim.Draw()
cc.cd(4)
hpip2pim.Draw()
cc.cd(5)
h2pip.Draw()
cc.cd(6)
hnpip1.Draw()
cc.cd(7)
hnpip2.Draw()
cc.cd(8)
hnpim.Draw()

cc.Update()

# Save the plot as an image
cc.Print("histograms.eps")

# Save ROOT objects to ROOT file
rootFile.Write()

