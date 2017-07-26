#!/usr/bin/env python
# encoding: utf-8

name = "C:\Code\RMG-Py\importer\pentaneNO"
shortDesc = u"C:\Code\RMG-Py\importer\pentaneNO\therm.dat"
longDesc = u"""
Unknown source
"""
entry(
    index = 1,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.31515,-0.000847391,1.76404e-05,-2.26763e-08,9.0895e-12,-17706.7,3.27373], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57977,0.00405326,-1.29845e-06,1.98211e-10,-1.13969e-14,-18007.2,0.664971], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 8/03""",
    longDesc = 
u"""
T 8/03.
OO
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 2,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99198,-0.00240107,4.61664e-06,-3.87916e-09,1.3632e-12,3368.9,-0.103998], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.83853,0.00110741,-2.94e-07,4.20699e-11,-2.4229e-15,3697.81,5.84495], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU3/03""",
    longDesc = 
u"""
IU3/03.
[OH]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 3,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34433,0.00798052,-1.94782e-05,2.01572e-08,-7.37612e-12,-917.935,0.68301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.93287,0.000826608,-1.46402e-07,1.541e-11,-6.88805e-16,-813.066,-1.02433], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""TPIS78""",
    longDesc = 
u"""
TPIS78.
[H][H]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 4,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 6/94""",
    longDesc = 
u"""
L 6/94.
[H]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 5,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16827,-0.00327932,6.64306e-06,-6.12807e-09,2.11266e-12,29122.3,2.05193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54364,-2.73162e-05,-4.1903e-09,4.95482e-12,-4.79554e-16,29226,4.92229], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 1/90""",
    longDesc = 
u"""
L 1/90.
[O]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 6,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19864,-0.0020364,6.52034e-06,-5.48793e-09,1.77197e-12,-30293.7,-0.849009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67704,0.00297318,-7.73769e-07,9.44335e-11,-4.269e-15,-29885.9,6.88255], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 5/89""",
    longDesc = 
u"""
L 5/89.
O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 7,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,264.018,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.17229,0.00188118,-3.46277e-07,1.94658e-11,1.76257e-16,31.0207,2.95768], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""T 1/09""",
    longDesc = 
u"""
T 1/09.
[O]O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 8,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78246,-0.00299673,9.8473e-06,-9.6813e-09,3.24373e-12,-1063.94,3.65768], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.66096,0.000656366,-1.4115e-07,2.05798e-11,-1.29913e-15,-1215.98,3.41536], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""RUS 89""",
    longDesc = 
u"""
RUS 89.
[O][O]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 9,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""G 5/97""",
    longDesc = 
u"""
G 5/97.
[Ar]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 10,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""G 8/02""",
    longDesc = 
u"""
G 8/02.
N#N
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 11,
    label = "HE",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""G 5/97""",
    longDesc = 
u"""
G 5/97.
[He]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 12,
    label = "OHV",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63727,0.000185091,-1.67616e-06,2.3872e-09,-8.43144e-13,50021.3,1.35886], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.88273,0.00101397,-2.27688e-07,2.17468e-11,-5.12631e-16,50265,5.59571], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286""",
    longDesc = 
u"""
121286
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species OH (i.e. same molecular structure according to RMG)
[OH]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 13,
    label = "CO",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.04849,0.00135173,-4.85794e-07,7.88536e-11,-4.69807e-15,-14266.1,6.0171], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""RUS 79""",
    longDesc = 
u"""
RUS 79.
[C]=O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 14,
    label = "CO2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35681,0.00898413,-7.12206e-06,2.4573e-09,-1.42885e-13,-48372,9.9009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.63651,0.00274146,-9.95898e-07,1.60387e-10,-9.16199e-15,-49024.9,-1.9349], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
L 7/88.
O=C=O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 15,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.14911,-0.0136622,4.91454e-05,-4.84247e-08,1.66603e-11,-10246.6,-4.63849], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.65326,0.0100263,-3.31661e-06,5.36483e-10,-3.14697e-14,-10009.6,9.90506], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""G 8/99""",
    longDesc = 
u"""
G 8/99.
C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 16,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65718,0.0021266,5.45839e-06,-6.6181e-09,2.46571e-12,16422.7,1.67354], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97812,0.00579785,-1.97558e-06,3.07298e-10,-1.79174e-14,16509.5,4.72248], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU0702""",
    longDesc = 
u"""
IU0702.
[CH3]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 17,
    label = "C",
    molecule = 
"""
1 C u0 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85442.7,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.60558,-0.000195934,1.06737e-07,-1.64239e-11,8.18706e-16,85411.7,4.19239], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
L 7/88.
[C]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 18,
    label = "CH",
    molecule = 
"""
multiplicity 4
1 C u3 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48976,0.000324322,-1.68998e-06,3.16284e-09,-1.40618e-12,70612.6,2.08428], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.52094,0.00176536,-4.61477e-07,5.92897e-11,-3.34745e-15,70946.8,7.40518], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU3/03""",
    longDesc = 
u"""
IU3/03.
[CH]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 19,
    label = "CHV",
    molecule = 
"""
multiplicity 4
1 C u3 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2002,0.00207288,-5.13443e-06,5.73389e-09,-1.95553e-12,103937,3.33159], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.19622,0.00234038,-7.0582e-07,9.00758e-11,-3.85504e-15,104196,9.17837], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""073003""",
    longDesc = 
u"""
073003
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Duplicate of species CH (i.e. same molecular structure according to RMG)
[CH]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 20,
    label = "CH3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.65851,-0.0162983,6.91938e-05,-7.58373e-08,2.80428e-11,-25612,-0.897331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.52727,0.0103179,-3.62893e-06,5.77448e-10,-3.42183e-14,-26002.9,5.16759], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T06/02""",
    longDesc = 
u"""
T06/02.
CO
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 21,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.29143,-0.00550155,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66679], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.04666,0.0153539,-5.47039e-06,8.77827e-10,-5.23168e-14,-12447.3,-0.968698], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""G 8/88""",
    longDesc = 
u"""
G 8/88.
CC
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 22,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3273,0.0176657,-6.14927e-06,-3.01143e-10,4.38618e-13,13428.4,17.1789], Tmin=(298,'K'), Tmax=(1387,'K')),
            NASAPolynomial(coeffs=[5.88784,0.0103077,-3.46844e-06,5.32499e-10,-3.06513e-14,11506.5,-8.49652], Tmin=(1387,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/ 4/ 4 THERM""",
    longDesc = 
u"""
8/ 4/ 4 THERM
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH2]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 23,
    label = "C2H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.481118,0.0183778,-9.99634e-06,2.73211e-09,-3.01837e-13,5443.87,18.5867], Tmin=(298,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[5.07061,0.00911141,-3.10507e-06,4.80734e-10,-2.78321e-14,3663.91,-6.64501], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/12/15""",
    longDesc = 
u"""
8/12/15
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 24,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89868,0.0132988,-2.80733e-05,2.89485e-08,-1.07502e-11,67061.6,6.18548], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.6627,0.00382492,-1.36633e-06,2.13455e-10,-1.23217e-14,67168.4,3.92206], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 5/10""",
    longDesc = 
u"""
T 5/10.
[C]#C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 25,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.240878,0.0339549,-1.60931e-05,2.83481e-09,2.78195e-14,-14036.3,21.6501], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[9.15541,0.0172574,-5.85615e-06,9.0419e-10,-5.22524e-14,-17576.2,-27.7419], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/12/15""",
    longDesc = 
u"""
8/12/15
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 26,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.80868,0.0233616,-3.55172e-05,2.80153e-08,-8.50075e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.65878,0.00488397,-1.60829e-06,2.46975e-10,-1.38606e-14,25759.4,-3.99838], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""G 1/91""",
    longDesc = 
u"""
G 1/91.
C#C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 27,
    label = "CH3OCH3",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.05597,0.0207019,-5.00382e-06,-1.6228e-09,6.8433e-13,-23549.4,14.503], Tmin=(298,'K'), Tmax=(1999,'K')),
            NASAPolynomial(coeffs=[6.03233,0.0156155,-5.50761e-06,8.75666e-10,-5.17181e-14,-25269,-8.25885], Tmin=(1999,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/11/14 THERM""",
    longDesc = 
u"""
2/11/14 THERM
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
COC
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 28,
    label = "O3",
    molecule = 
"""
1 O u0 p1 c+1 {2,S} {3,D}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40738,0.00205379,1.38486e-05,-2.23312e-08,9.76073e-12,15864.5,8.28248], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.3303,-0.0119325,7.98741e-06,-1.77195e-09,1.26076e-13,12675.6,-40.8823], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 5/90""",
    longDesc = 
u"""
L 5/90.
O=OO
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 29,
    label = "N",
    molecule = 
"""
multiplicity 4
1 N u3 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,56104.6,4.19391], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.41594,0.000174891,-1.19024e-07,3.02262e-11,-2.0361e-15,56133.8,4.64961], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 6/88""",
    longDesc = 
u"""
L 6/88.
[N]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 30,
    label = "NO2",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6706,0.0078385,-8.06386e-06,6.16171e-09,-2.32015e-12,2896.3,11.612], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.68286,0.00246243,-1.04226e-06,1.9769e-10,-1.392e-14,2261.3,0.989], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
N(=O)[O]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 31,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71181,-0.00280463,3.76551e-05,-4.73072e-08,1.86588e-11,1295.7,6.57241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75779,0.00744142,-2.69705e-06,4.38091e-10,-2.63537e-14,378.112,-1.9668], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU1/03""",
    longDesc = 
u"""
IU1/03.
C[O]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 32,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47834,-0.0013507,2.78485e-05,-3.64869e-08,1.47907e-11,-3500.73,3.30913], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09314,0.00594761,-2.06497e-06,3.23008e-10,-1.88126e-14,-4034.1,-1.84691], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU2/03""",
    longDesc = 
u"""
IU2/03.
[CH2]O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 33,
    label = "CH2O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14379.2,0.602798], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16953,0.00619321,-2.25056e-06,3.65976e-10,-2.20149e-14,-14548.7,6.04208], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 5/11""",
    longDesc = 
u"""
T 5/11.
C=O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 34,
    label = "NC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.20121,0.0529642,-7.23641e-05,6.36997e-08,-2.29333e-11,11513.1,34.3669], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.48614,0.0165769,-5.74876e-06,9.04104e-10,-5.30867e-14,8937.1,-14.2595], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""8/12/15""",
    longDesc = 
u"""
8/12/15.
[CH2]CC
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 35,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23755,-0.00332075,1.4003e-05,-1.3424e-08,4.37416e-12,3872.41,3.30835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.92002,0.00252279,-6.71004e-07,1.05616e-10,-7.43798e-15,3653.43,3.58077], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 5/03""",
    longDesc = 
u"""
T 5/03.
[CH]=O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 36,
    label = "HONO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29041,0.0140992,-1.36787e-05,7.49878e-09,-1.87691e-12,-10431.9,13.281], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.48689,0.00421806,-1.64914e-06,2.9719e-10,-2.021e-14,-11268.6,-2.997], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
N(=O)O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 37,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.25545,0.0157482,-1.12218e-05,4.50916e-09,-7.74862e-13,34743.6,16.9664], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[4.99675,0.00655838,-2.20922e-06,3.393e-10,-1.95317e-14,33460.4,-3.01451], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/12/15""",
    longDesc = 
u"""
8/12/15
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 38,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71758,0.00127391,2.17347e-06,-3.48858e-09,1.65209e-12,45872.4,1.75298], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.14632,0.00303671,-9.96474e-07,1.50484e-10,-8.57336e-15,46041.3,4.72342], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU3/03""",
    longDesc = 
u"""
IU3/03.
[CH2]
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 39,
    label = "CH3OCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {3,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58875,0.0224414,-1.19435e-05,3.3716e-09,-4.15077e-13,-1372.08,18.7549], Tmin=(298,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[6.62622,0.0122219,-4.12417e-06,6.34128e-10,-3.65317e-14,-3339.66,-8.95306], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""2/11/14 THERM""",
    longDesc = 
u"""
2/11/14 THERM
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]OC
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 40,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.54607,0.0436553,-5.61392e-05,4.98422e-08,-1.84799e-11,2070.56,29.9232], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.59032,0.0152593,-5.30369e-06,8.35511e-10,-4.91216e-14,-247.481,-11.5748], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""8/12/15""",
    longDesc = 
u"""
8/12/15.
C=CC
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 41,
    label = "IC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.897467,0.0415744,-4.94778e-05,4.56494e-08,-1.79085e-11,9939.5,29.2642], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.70776,0.0174048,-6.07616e-06,9.60084e-10,-5.65656e-14,7553.78,-10.3687], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""8/12/15""",
    longDesc = 
u"""
8/12/15.
C[CH]C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 42,
    label = "C3H5-A",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.32899,0.0538423,-7.65501e-05,6.35512e-08,-2.14283e-11,20342.1,36.8038], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.37604,0.012345,-4.26464e-06,6.69046e-10,-3.92203e-14,17733.3,-16.1758], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""8/12/15""",
    longDesc = 
u"""
8/12/15.
[CH2]C=C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 43,
    label = "C3H5-T",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29257,0.0198528,-6.42636e-06,-5.90016e-10,5.05491e-13,28577.3,13.9407], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[7.69949,0.0117804,-4.07792e-06,6.38119e-10,-3.7223e-14,26174.7,-16.8306], Tmin=(1376,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/12/15""",
    longDesc = 
u"""
8/12/15
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 44,
    label = "C3H5-S",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61793,0.0244804,-1.41857e-05,4.16402e-09,-4.90905e-13,30429.1,16.6341], Tmin=(298,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[7.95954,0.0111163,-3.75198e-06,5.77246e-10,-3.32769e-14,28056.8,-17.98], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""8/12/15""",
    longDesc = 
u"""
8/12/15
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 45,
    label = "C3H4-A",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61304,0.0121226,1.85399e-05,-3.45251e-08,1.53351e-11,21541.6,10.2261], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.31687,0.0111337,-3.96294e-06,6.35642e-10,-3.78755e-14,20117.5,-10.9958], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 8/89""",
    longDesc = 
u"""
L 8/89.
C=C=C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 46,
    label = "C3H4-P",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68039,0.0157997,2.50706e-06,-1.36576e-08,6.61543e-12,20802.4,9.87694], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.02524,0.0113365,-4.02234e-06,6.43761e-10,-3.82996e-14,19620.9,-8.60438], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 2/90""",
    longDesc = 
u"""
T 2/90.
C#CC
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 47,
    label = "NO",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37654,0.00125306,-3.30275e-06,5.21781e-09,-2.44626e-12,9818,5.83], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.24544,0.00126914,-5.0159e-07,9.169e-11,-6.28e-15,9800.8,6.417], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""------------------------------------------------------------------------------------------------------""",
    longDesc = 
u"""
------------------------------------------------------------------------------------------------------
-------------------------------------- AJOUT DAGAUT --------------------------------------------------
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[N]=O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 48,
    label = "C3H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35111,0.0327411,-4.73827e-05,3.7631e-08,-1.18541e-11,40768,15.2059], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.14222,0.00761902,-2.6746e-06,4.24915e-10,-2.51475e-14,39571,-12.5849], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 7/11""",
    longDesc = 
u"""
T 7/11.
[CH]=C=C
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 49,
    label = "HNO",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7844,0.00660965,-9.30022e-06,9.43798e-09,-3.75315e-12,10918.8,9.036], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.61514,0.00321249,-1.26034e-06,2.2673e-10,-1.536e-14,10661.9,4.81], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
N=O
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

entry(
    index = 50,
    label = "FULVENE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,D}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u0 p0 c0 {3,D} {4,S} {9,S}
6  C u0 p0 c0 {1,D} {11,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.718132,0.0379343,1.13988e-05,-4.13335e-08,1.80559e-11,24223.8,27.8557], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.1035,0.0206007,-7.53022e-06,1.23887e-09,-7.5416e-14,20361.8,-36.6652], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""0""",
    longDesc = 
u"""
0.
C=C1C=CC=C1
Imported from C:\Code\RMG-Py\importer\pentaneNO\therm.dat.
""",
)

