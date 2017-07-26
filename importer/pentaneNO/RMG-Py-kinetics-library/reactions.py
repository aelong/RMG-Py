#!/usr/bin/env python
# encoding: utf-8

name = "C:\Code\RMG-Py\importer\pentaneNO"
shortDesc = u"C:\Code\RMG-Py\importer\pentaneNO\chem.inp"
longDesc = u"""
Unknown source
"""
entry(
    index = 1,
    label = "H2 <=> H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.83, '[C]=O': 1.9},
    ),
    shortDesc = u"""The chemkin file reaction is H2 <=> H + H""",
)

entry(
    index = 2,
    label = "H2 + O <=> H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(50800, 'cm^3/(mol*s)'), n=2.67, Ea=(6292, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is H2 + O <=> H + OH""",
)

entry(
    index = 3,
    label = "H2 + OH <=> H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.38e+13, 'cm^3/(mol*s)'), n=0, Ea=(6990, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is H2 + OH <=> H + H2O""",
)

entry(
    index = 4,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.165e+15, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.83, '[C]=O': 1.9, '[Ar]': 0.83},
    ),
    shortDesc = u"""The chemkin file reaction is O + O <=> O2""",
)

entry(
    index = 5,
    label = "O2 + H <=> O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+14, 'cm^3/(mol*s)'), n=0, Ea=(15286, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O2 + H <=> O + OH""",
)

entry(
    index = 6,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'CC': 3, 'C': 2, '[H][H]': 0.73, 'O': 3.65, '[Ar]': 0.38},
    ),
    shortDesc = u"""The chemkin file reaction is H + OH <=> H2O""",
)

entry(
    index = 7,
    label = "O + H2O <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+07, 'cm^3/(mol*s)'),
        n = 1.704,
        Ea = (14986.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is O + H2O <=> OH + OH""",
)

entry(
    index = 8,
    label = "O + H <=> OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.75, '[C]=O': 1.5, '[Ar]': 0.75},
    ),
    shortDesc = u"""The chemkin file reaction is O + H <=> OH""",
)

entry(
    index = 9,
    label = "H + O <=> OHV",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.5e+13, 'cm^6/(mol^2*s)'), n=0, Ea=(5975, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 1, '[O][O]': 0.4, 'O': 6.5, 'N#N': 0.4, '[Ar]': 0.35},
    ),
    shortDesc = u"""The chemkin file reaction is H + O <=> OHV""",
)

entry(
    index = 10,
    label = "OHV + H2O <=> OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.93e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is OHV + H2O <=> OH + H2O""",
)

entry(
    index = 11,
    label = "OHV + H2 <=> OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.95e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-444, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is OHV + H2 <=> OH + H2""",
)

entry(
    index = 12,
    label = "OHV + N2 <=> OH + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+11, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-1242, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is OHV + N2 <=> OH + N2""",
)

entry(
    index = 13,
    label = "OHV + OH <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.01e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-764, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is OHV + OH <=> OH + OH""",
)

entry(
    index = 14,
    label = "OHV + H <=> OH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.31e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-167, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is OHV + H <=> OH + H""",
)

entry(
    index = 15,
    label = "OHV + AR <=> OH + AR",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.69e+12, 'cm^3/(mol*s)'), n=0, Ea=(4135, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is OHV + AR <=> OH + AR""",
)

entry(
    index = 16,
    label = "OHV <=> OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+06, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is OHV <=> OH""",
)

entry(
    index = 17,
    label = "OHV + O2 <=> OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(-478, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is OHV + O2 <=> OH + O2""",
)

entry(
    index = 18,
    label = "OHV + CO2 <=> OH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.75e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-968, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is OHV + CO2 <=> OH + CO2""",
)

entry(
    index = 19,
    label = "OHV + CO <=> OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.23e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-787, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is OHV + CO <=> OH + CO""",
)

entry(
    index = 20,
    label = "OHV + CH4 <=> OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.36e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-635, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is OHV + CH4 <=> OH + CH4""",
)

entry(
    index = 21,
    label = "H2O2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48749, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.49e+24, 'cm^3/(mol*s)'),
            n = -2.3,
            Ea = (48749, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.43,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'OO': 7.7, 'O=C=O': 1.6, 'O': 7.65, '[H][H]': 3.7, '[He]': 0.65, '[O][O]': 1.2, 'N#N': 1.5, '[C]=O': 2.8},
    ),
    shortDesc = u"""The chemkin file reaction is H2O2 <=> OH + OH""",
)

entry(
    index = 22,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is H2O2 + H <=> H2O + OH""",
)

entry(
    index = 23,
    label = "H2O2 + H <=> H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+10, 'cm^3/(mol*s)'), n=1, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is H2O2 + H <=> H2 + HO2""",
)

entry(
    index = 24,
    label = "H2O2 + O <=> OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is H2O2 + O <=> OH + HO2""",
)

entry(
    index = 25,
    label = "H2O2 + OH <=> H2O + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(318, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.59e+13, 'cm^3/(mol*s)'), n=0, Ea=(7269, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(318, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.59e+13, 'cm^3/(mol*s)'), n=0, Ea=(7270, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is H2O2 + OH <=> H2O + HO2""",
)

entry(
    index = 26,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.079e+13, 'cm^3/(mol*s)'), n=0, Ea=(295, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HO2 + H <=> OH + OH""",
)

entry(
    index = 27,
    label = "HO2 + H <=> H2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1402e+10, 'cm^3/(mol*s)'),
        n = 1.0827,
        Ea = (553.78, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is HO2 + H <=> H2 + O2""",
)

entry(
    index = 28,
    label = "HO2 + O <=> OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HO2 + O <=> OH + O2""",
)

entry(
    index = 29,
    label = "OH + HO2 <=> H2O + O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1092.96, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.5e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (10929.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is OH + HO2 <=> H2O + O2""",
)

entry(
    index = 30,
    label = "HO2 + HO2 <=> H2O2 + O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(11040.9, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.9e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1408.92, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(4.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(11982, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.3e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1629.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is HO2 + HO2 <=> H2O2 + O2""",
)

entry(
    index = 31,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.65e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.737e+19, 'cm^6/(mol^2*s)'),
            n = -1.23,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.67,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 10, '[H][H]': 1.3, '[He]': 0.64, '[C]=O': 1.9, '[Ar]': 0.5},
    ),
    shortDesc = u"""The chemkin file reaction is H + O2 <=> HO2""",
)

entry(
    index = 32,
    label = "CO + O <=> CO2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.362e+10, 'cm^3/(mol*s)'), n=0, Ea=(2384, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.173e+24, 'cm^6/(mol^2*s)'),
            n = -2.79,
            Ea = (4191, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.6, 'O': 12, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.75, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is CO + O <=> CO2""",
)

entry(
    index = 33,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (70150, 'cm^3/(mol*s)'),
                n = 2.053,
                Ea = (-355.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.757e+12, 'cm^3/(mol*s)'),
                n = -0.664,
                Ea = (331.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (70460, 'cm^3/(mol*s)'),
                n = 2.053,
                Ea = (-276.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.757e+12, 'cm^3/(mol*s)'),
                n = -0.664,
                Ea = (331.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CO + OH <=> CO2 + H""",
)

entry(
    index = 34,
    label = "CO + HO2 <=> CO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CO + HO2 <=> CO2 + OH""",
)

entry(
    index = 35,
    label = "CO + O2 <=> CO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.119e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CO + O2 <=> CO2 + O""",
)

entry(
    index = 39,
    label = "CH3 + H <=> CH4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.27e+16, 'cm^3/(mol*s)'),
            n = -0.63,
            Ea = (383, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.477e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (2440, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + H <=> CH4""",
)

entry(
    index = 40,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(614000, 'cm^3/(mol*s)'), n=2.5, Ea=(9587, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH4 + H <=> CH3 + H2""",
)

entry(
    index = 41,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH4 + O <=> CH3 + OH""",
)

entry(
    index = 42,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(58300, 'cm^3/(mol*s)'), n=2.6, Ea=(2190, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH4 + OH <=> CH3 + H2O""",
)

entry(
    index = 43,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11.3, 'cm^3/(mol*s)'), n=3.74, Ea=(21010, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH4 + HO2 <=> CH3 + H2O2""",
)

entry(
    index = 45,
    label = "CH3 + HO2 <=> CH4 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (116000, 'cm^3/(mol*s)'),
        n = 2.23,
        Ea = (-3022, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + HO2 <=> CH4 + O2""",
)

entry(
    index = 46,
    label = "CH4 + CH2 <=> CH3 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(8270, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH4 + CH2 <=> CH3 + CH3""",
)

entry(
    index = 60,
    label = "CH2 + H <=> CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.2e+27, 'cm^6/(mol^2*s)'),
            n = -3.14,
            Ea = (1230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.68,
        T3 = (78, 'K'),
        T1 = (1995, 'K'),
        T2 = (5590, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is CH2 + H <=> CH3""",
)

entry(
    index = 61,
    label = "CH2 + O2 <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+13, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + O2 <=> HCO + OH""",
)

entry(
    index = 62,
    label = "CH2 + O2 => CO2 + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + O2 => CO2 + H + H""",
)

entry(
    index = 63,
    label = "CH2 + O => CO + H + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + O => CO + H + H""",
)

entry(
    index = 64,
    label = "CH2 + H <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + H <=> CH + H2""",
)

entry(
    index = 65,
    label = "CH2 + OH <=> CH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + OH <=> CH + H2O""",
)

entry(
    index = 66,
    label = "CHV + AR <=> CH + AR",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CHV + AR <=> CH + AR""",
)

entry(
    index = 67,
    label = "CHV + H2O <=> CH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CHV + H2O <=> CH + H2O""",
)

entry(
    index = 68,
    label = "CHV + CO <=> CH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CHV + CO <=> CH + CO""",
)

entry(
    index = 69,
    label = "CHV + CO2 <=> CH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.241, 'cm^3/(mol*s)'), n=4.3, Ea=(-1694, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CHV + CO2 <=> CH + CO2""",
)

entry(
    index = 70,
    label = "CHV + O2 <=> CH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.48e+06, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (-1720, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CHV + O2 <=> CH + O2""",
)

entry(
    index = 71,
    label = "CHV + H2 <=> CH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.47e+14, 'cm^3/(mol*s)'), n=0, Ea=(1361, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CHV + H2 <=> CH + H2""",
)

entry(
    index = 72,
    label = "CHV + CH4 <=> CH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+13, 'cm^3/(mol*s)'), n=0, Ea=(167, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CHV + CH4 <=> CH + CH4""",
)

entry(
    index = 73,
    label = "CHV <=> CH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.86e+06, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CHV <=> CH""",
)

entry(
    index = 74,
    label = "CHV + N2 <=> CH + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(303, 'cm^3/(mol*s)'), n=3.4, Ea=(-381, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CHV + N2 <=> CH + N2""",
)

entry(
    index = 75,
    label = "C + H <=> CHV",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(6940, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    shortDesc = u"""The chemkin file reaction is C + H <=> CHV""",
)

entry(
    index = 76,
    label = "CH + O2 <=> CO + OHV",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.04e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (6.6e+09, 'cm^3/(mol*s)'),
                n = 1.008,
                Ea = (-489.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH + O2 <=> CO + OHV""",
)

entry(
    index = 77,
    label = "CH + O2 <=> HCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH + O2 <=> HCO + O""",
)

entry(
    index = 78,
    label = "CH + O <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH + O <=> CO + H""",
)

entry(
    index = 79,
    label = "CH + H <=> C + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH + H <=> C + H2""",
)

entry(
    index = 80,
    label = "CH + OH <=> HCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH + OH <=> HCO + H""",
)

entry(
    index = 81,
    label = "CH + H2O <=> H + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.774e+16, 'cm^3/(mol*s)'),
        n = -1.22,
        Ea = (23.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH + H2O <=> H + CH2O""",
)

entry(
    index = 82,
    label = "CH + CO2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(685, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH + CO2 <=> HCO + CO""",
)

entry(
    index = 83,
    label = "C + OH <=> CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C + OH <=> CO + H""",
)

entry(
    index = 84,
    label = "C + O2 <=> CO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C + O2 <=> CO + O""",
)

entry(
    index = 86,
    label = "CH3 + O2 <=> CH3O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.546e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28320, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + O2 <=> CH3O + O""",
)

entry(
    index = 87,
    label = "CH3 + O2 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.641, 'cm^3/(mol*s)'), n=3.283, Ea=(8105, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3 + O2 <=> CH2O + OH""",
)

entry(
    index = 88,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.54e+13, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (-136, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + O <=> CH2O + H""",
)

entry(
    index = 90,
    label = "CH3 + OH <=> CH2O + H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (350200, 'cm^3/(mol*s)'),
                n = 1.441,
                Ea = (-3244, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (885400, 'cm^3/(mol*s)'),
                n = 1.327,
                Ea = (-2975, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.65e+07, 'cm^3/(mol*s)'),
                n = 0.973,
                Ea = (-2010, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.374e+09, 'cm^3/(mol*s)'),
                n = 0.287,
                Ea = (280, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.494e+18, 'cm^3/(mol*s)'),
                n = -2.199,
                Ea = (9769, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + OH <=> CH2O + H2""",
)

entry(
    index = 91,
    label = "CH3 + OH <=> CH2OH + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.621e+10, 'cm^3/(mol*s)'),
                n = 0.965,
                Ea = (3214, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.807e+10, 'cm^3/(mol*s)'),
                n = 0.95,
                Ea = (3247, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.686e+10, 'cm^3/(mol*s)'),
                n = 0.833,
                Ea = (3566, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.525e+13, 'cm^3/(mol*s)'),
                n = 0.134,
                Ea = (5641, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.59e+14, 'cm^3/(mol*s)'),
                n = -0.186,
                Ea = (8601, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + OH <=> CH2OH + H""",
)

entry(
    index = 92,
    label = "CH3 + OH <=> H + CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.186e+09, 'cm^3/(mol*s)'),
                n = 1.016,
                Ea = (11940, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.188e+09, 'cm^3/(mol*s)'),
                n = 1.016,
                Ea = (11940, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.23e+09, 'cm^3/(mol*s)'),
                n = 1.011,
                Ea = (11950, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.798e+09, 'cm^3/(mol*s)'),
                n = 0.965,
                Ea = (12060, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.242e+10, 'cm^3/(mol*s)'),
                n = 0.551,
                Ea = (13070, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + OH <=> H + CH3O""",
)

entry(
    index = 94,
    label = "CH3 + OH <=> CH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42930, 'cm^3/(mol*s)'),
        n = 2.568,
        Ea = (3997.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + OH <=> CH2 + H2O""",
)

entry(
    index = 95,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0.269,
        Ea = (-687.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + HO2 <=> CH3O + OH""",
)

entry(
    index = 107,
    label = "CH3OH <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.084e+18, 's^-1'), n=-0.615, Ea=(92540.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.5e+43, 'cm^3/(mol*s)'),
            n = -6.995,
            Ea = (97992.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.4748,
        T3 = (35580, 'K'),
        T1 = (1116, 'K'),
        T2 = (9023, 'K'),
        efficiencies = {},
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH <=> CH3 + OH""",
)

entry(
    index = 109,
    label = "CH3OH <=> CH2OH + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(0.007896, 's^-1'), n=5.038, Ea=(84467.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.39e+42, 'cm^3/(mol*s)'),
            n = -7.244,
            Ea = (105230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -73.91,
        T3 = (37050, 'K'),
        T1 = (41500, 'K'),
        T2 = (5220, 'K'),
        efficiencies = {},
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH <=> CH2OH + H""",
)

entry(
    index = 110,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (199000, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (10300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + H <=> CH3O + H2""",
)

entry(
    index = 111,
    label = "CH3OH + H <=> CH2OH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(307000, 'cm^3/(mol*s)'), n=2.55, Ea=(5440, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OH + H <=> CH2OH + H2""",
)

entry(
    index = 112,
    label = "CH3OH + O <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(38800, 'cm^3/(mol*s)'), n=2.5, Ea=(3080, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OH + O <=> CH3O + OH""",
)

entry(
    index = 113,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(388000, 'cm^3/(mol*s)'), n=2.5, Ea=(3080, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OH + O <=> CH2OH + OH""",
)

entry(
    index = 114,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=3.03, Ea=(-763, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OH + OH <=> CH3O + H2O""",
)

entry(
    index = 115,
    label = "CH3OH + OH <=> CH2OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30800, 'cm^3/(mol*s)'),
        n = 2.65,
        Ea = (-806.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + OH <=> CH2OH + H2O""",
)

entry(
    index = 116,
    label = "CH3OH + O2 <=> CH3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (35800, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (42764.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + O2 <=> CH3O + HO2""",
)

entry(
    index = 117,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (358000, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (42764.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + O2 <=> CH2OH + HO2""",
)

entry(
    index = 118,
    label = "CH3OH + HO2 <=> CH3O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.22e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20070.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + HO2 <=> CH3O + H2O2""",
)

entry(
    index = 119,
    label = "CH3OH + HO2 <=> CH2OH + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.26e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18782.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + HO2 <=> CH2OH + H2O2""",
)

entry(
    index = 120,
    label = "CH3OH + CH3 <=> CH2OH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.213, 'cm^3/(mol*s)'),
        n = 3.953,
        Ea = (7055.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + CH3 <=> CH2OH + CH4""",
)

entry(
    index = 121,
    label = "CH3OH + CH3 <=> CH3O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3220, 'cm^3/(mol*s)'),
        n = 2.425,
        Ea = (8579.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + CH3 <=> CH3O + CH4""",
)

entry(
    index = 122,
    label = "CH3OH + HCO <=> CH2OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9630, 'cm^3/(mol*s)'), n=2.9, Ea=(13110, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OH + HCO <=> CH2OH + CH2O""",
)

entry(
    index = 123,
    label = "CH3OH + CH3O <=> CH2OH + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(4074, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OH + CH3O <=> CH2OH + CH3OH""",
)

entry(
    index = 125,
    label = "CH2OH + O2 <=> CH2O + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.51e+15, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.41e+14, 'cm^3/(mol*s)'), n=0, Ea=(5017, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH2OH + O2 <=> CH2O + HO2""",
)

entry(
    index = 126,
    label = "CH2OH + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + H <=> CH2O + H2""",
)

entry(
    index = 127,
    label = "CH2OH + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + HO2 <=> CH2O + H2O2""",
)

entry(
    index = 128,
    label = "CH2OH + HCO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + HCO <=> CH2O + CH2O""",
)

entry(
    index = 129,
    label = "CH2OH + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + HCO <=> CH3OH + CO""",
)

entry(
    index = 130,
    label = "CH2OH + CH3O <=> CH2O + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + CH3O <=> CH2O + CH3OH""",
)

entry(
    index = 131,
    label = "CH2OH + OH <=> H2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + OH <=> H2O + CH2O""",
)

entry(
    index = 132,
    label = "CH2OH + O <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + O <=> OH + CH2O""",
)

entry(
    index = 133,
    label = "CH2OH + CH2OH <=> CH2O + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + CH2OH <=> CH2O + CH3OH""",
)

entry(
    index = 135,
    label = "CH3O + O2 <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.38e-19, 'cm^3/(mol*s)'),
        n = 9.5,
        Ea = (-5501, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3O + O2 <=> CH2O + HO2""",
)

entry(
    index = 136,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + H <=> CH2O + H2""",
)

entry(
    index = 137,
    label = "CH3O + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + HO2 <=> CH2O + H2O2""",
)

entry(
    index = 138,
    label = "CH3O + CH3 <=> CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + CH3 <=> CH2O + CH4""",
)

entry(
    index = 139,
    label = "CH3O + CH3O <=> CH3OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + CH3O <=> CH3OH + CH2O""",
)

entry(
    index = 146,
    label = "HCO + H <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.09e+12, 'cm^3/(mol*s)'),
            n = 0.48,
            Ea = (-260, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.35e+24, 'cm^6/(mol^2*s)'),
            n = -2.57,
            Ea = (1425, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7824,
        T3 = (271, 'K'),
        T1 = (2755, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is HCO + H <=> CH2O""",
)

entry(
    index = 147,
    label = "CO + H2 <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.3e+07, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (79600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.07e+27, 'cm^6/(mol^2*s)'),
            n = -3.42,
            Ea = (84348, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is CO + H2 <=> CH2O""",
)

entry(
    index = 148,
    label = "CH2O + O2 <=> HCO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.07e+15, 'cm^3/(mol*s)'), n=0, Ea=(53420, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2O + O2 <=> HCO + HO2""",
)

entry(
    index = 149,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.26e+09, 'cm^3/(mol*s)'),
        n = 1.15,
        Ea = (2260, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2O + O <=> HCO + OH""",
)

entry(
    index = 150,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2740, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2O + H <=> HCO + H2""",
)

entry(
    index = 151,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.82e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1055, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2O + OH <=> HCO + H2O""",
)

entry(
    index = 152,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18800, 'cm^3/(mol*s)'), n=2.7, Ea=(11520, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2O + HO2 <=> HCO + H2O2""",
)

entry(
    index = 153,
    label = "CH2O + CH3 <=> HCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(38.3, 'cm^3/(mol*s)'), n=3.36, Ea=(4312, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2O + CH3 <=> HCO + CH4""",
)

entry(
    index = 156,
    label = "CH2O + CH3O <=> HCO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(2294, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2O + CH3O <=> HCO + CH3OH""",
)

entry(
    index = 158,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.7e+11, 'cm^3/(mol*s)'),
            n = 0.66,
            Ea = (14870, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
    shortDesc = u"""The chemkin file reaction is HCO <=> H + CO""",
)

entry(
    index = 159,
    label = "HCO + O2 <=> CO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(410, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + O2 <=> CO + HO2""",
)

entry(
    index = 160,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + O <=> CO + OH""",
)

entry(
    index = 161,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + H <=> CO + H2""",
)

entry(
    index = 162,
    label = "HCO + OH <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.011e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + OH <=> CO + H2O""",
)

entry(
    index = 163,
    label = "HCO + CH3 <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.65e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + CH3 <=> CH4 + CO""",
)

entry(
    index = 164,
    label = "HCO + HCO <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + HCO <=> CH2O + CO""",
)

entry(
    index = 165,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + O <=> CO2 + H""",
)

entry(
    index = 166,
    label = "HCO + HO2 => CO2 + H + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + HO2 => CO2 + H + OH""",
)

entry(
    index = 167,
    label = "HCO + HCO => H2 + CO + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + HCO => H2 + CO + CO""",
)

entry(
    index = 168,
    label = "CH2O + H <=> CH2OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (3600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.27e+32, 'cm^6/(mol^2*s)'),
            n = -4.82,
            Ea = (6530, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7187,
        T3 = (103, 'K'),
        T1 = (1291, 'K'),
        T2 = (4160, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
    shortDesc = u"""The chemkin file reaction is CH2O + H <=> CH2OH""",
)

entry(
    index = 169,
    label = "CH3O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.8e+13, 's^-1'), n=0, Ea=(26170, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.867e+25, 'cm^3/(mol*s)'),
            n = -3,
            Ea = (24307, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9,
        T3 = (2500, 'K'),
        T1 = (1300, 'K'),
        T2 = (1e+99, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
    shortDesc = u"""The chemkin file reaction is CH3O <=> CH2O + H""",
)

entry(
    index = 189,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.277e+15, 'cm^3/(mol*s)'),
            n = -0.69,
            Ea = (174.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (8.054e+31, 'cm^6/(mol^2*s)'),
            n = -3.75,
            Ea = (981.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        T3 = (570, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + CH3 <=> C2H6""",
)

entry(
    index = 190,
    label = "C2H5 + H <=> C2H6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.842,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is C2H5 + H <=> C2H6""",
)

entry(
    index = 191,
    label = "C2H6 + O2 <=> C2H5 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(51870, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H6 + O2 <=> C2H5 + HO2""",
)

entry(
    index = 192,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.55e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5830, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H6 + O <=> C2H5 + OH""",
)

entry(
    index = 193,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H6 + H <=> C2H5 + H2""",
)

entry(
    index = 194,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.48e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(950, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H6 + OH <=> C2H5 + H2O""",
)

entry(
    index = 195,
    label = "C2H6 + HO2 <=> C2H5 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34.6, 'cm^3/(mol*s)'), n=3.61, Ea=(16920, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H6 + HO2 <=> C2H5 + H2O2""",
)

entry(
    index = 196,
    label = "C2H6 + CH <=> C2H5 + CH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(-260, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H6 + CH <=> C2H5 + CH2""",
)

entry(
    index = 198,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000555, 'cm^3/(mol*s)'),
        n = 4.72,
        Ea = (3231, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H6 + CH3 <=> C2H5 + CH4""",
)

entry(
    index = 199,
    label = "C2H6 + CH3O <=> C2H5 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+11, 'cm^3/(mol*s)'), n=0, Ea=(7090, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H6 + CH3O <=> C2H5 + CH3OH""",
)

entry(
    index = 202,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (9.569e+08, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1355, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.419e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.569,
        T3 = (299, 'K'),
        T1 = (-9147, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + H <=> C2H5""",
)

entry(
    index = 203,
    label = "C2H5 + H <=> C2H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + H <=> C2H4 + H2""",
)

entry(
    index = 204,
    label = "C2H4 + C2H4 <=> C2H5 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+14, 'cm^3/(mol*s)'), n=0, Ea=(71530, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H4 + C2H4 <=> C2H5 + C2H3""",
)

entry(
    index = 205,
    label = "C2H5 + CH3 <=> CH4 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11800, 'cm^3/(mol*s)'), n=2.45, Ea=(-2921, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + CH3 <=> CH4 + C2H4""",
)

entry(
    index = 209,
    label = "CH3 + CH3 <=> H + C2H5",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.74e+12, 'cm^3/(mol*s)'),
                n = 0.105,
                Ea = (10664.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.57e+13, 'cm^3/(mol*s)'),
                n = -0.096,
                Ea = (11406.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.1e+14, 'cm^3/(mol*s)'),
                n = -0.362,
                Ea = (13372.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.15e+10, 'cm^3/(mol*s)'),
                n = 0.885,
                Ea = (13532.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (103.2, 'cm^3/(mol*s)'),
                n = 3.23,
                Ea = (11236.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + CH3 <=> H + C2H5""",
)

entry(
    index = 212,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.094e+09, 'cm^3/(mol*s)'),
                n = 0.49,
                Ea = (-391.4, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.843e+07, 'cm^3/(mol*s)'),
                n = 1.13,
                Ea = (-720.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.561e+14, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (4749, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H5 + O2 <=> C2H4 + HO2""",
)

entry(
    index = 239,
    label = "C2H3 + H <=> C2H4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.08e+12, 'cm^3/(mol*s)'),
            n = 0.27,
            Ea = (280, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3320, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (207.5, 'K'),
        T1 = (2663, 'K'),
        T2 = (6095, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + H <=> C2H4""",
)

entry(
    index = 241,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (57623.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + O2 <=> C2H3 + HO2""",
)

entry(
    index = 242,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.07e+07, 'cm^3/(mol*s)'),
        n = 1.93,
        Ea = (12950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + H <=> C2H3 + H2""",
)

entry(
    index = 243,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22300, 'cm^3/(mol*s)'),
        n = 2.745,
        Ea = (2215.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + OH <=> C2H3 + H2O""",
)

entry(
    index = 244,
    label = "C2H4 + CH3O <=> C2H3 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6750, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H4 + CH3O <=> C2H3 + CH3OH""",
)

entry(
    index = 248,
    label = "C2H4 + CH3 <=> C2H3 + CH4",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(976, 'cm^3/(mol*s)'), n=2.947, Ea=(15148, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (8.13e-05, 'cm^3/(mol*s)'),
                n = 4.417,
                Ea = (8835.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + CH3 <=> C2H3 + CH4""",
)

entry(
    index = 249,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.453e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + O <=> CH3 + HCO""",
)

entry(
    index = 251,
    label = "CH + CH4 <=> C2H4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH + CH4 <=> C2H4 + H""",
)

entry(
    index = 253,
    label = "C2H4 + OH <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.35, 'cm^3/(mol*s)'),
                n = 2.92,
                Ea = (-1732.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (31.9, 'cm^3/(mol*s)'),
                n = 2.71,
                Ea = (-1172.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(555, 'cm^3/(mol*s)'), n=2.36, Ea=(-180.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (178000, 'cm^3/(mol*s)'),
                n = 1.68,
                Ea = (2060.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.37e+09, 'cm^3/(mol*s)'),
                n = 0.56,
                Ea = (6006.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.76e+13, 'cm^3/(mol*s)'),
                n = -0.5,
                Ea = (11455.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + OH <=> CH3 + CH2O""",
)

entry(
    index = 260,
    label = "C2H2 + H <=> C2H3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.71e+10, 'cm^3/(mol*s)'),
            n = 1.266,
            Ea = (2709, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.346e+31, 'cm^6/(mol^2*s)'),
            n = -4.664,
            Ea = (3780, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.788,
        T3 = (-10200, 'K'),
        T1 = (1e-30, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is C2H2 + H <=> C2H3""",
)

entry(
    index = 267,
    label = "C2H3 + O2 <=> C2H2 + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.08e+07, 'cm^3/(mol*s)'),
                        n = 1.28,
                        Ea = (3322, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.75e+06, 'cm^3/(mol*s)'),
                        n = 1.33,
                        Ea = (3216, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.21e+07, 'cm^3/(mol*s)'),
                        n = 1.27,
                        Ea = (3311, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.15e+07, 'cm^3/(mol*s)'),
                        n = 1.19,
                        Ea = (3367, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1.13e+08, 'cm^3/(mol*s)'), n=1, Ea=(3695, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (1.31e+11, 'cm^3/(mol*s)'),
                        n = 0.12,
                        Ea = (5872, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.19e+09, 'cm^3/(mol*s)'),
                        n = 0.82,
                        Ea = (5617, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+17, 'cm^3/(mol*s)'),
                        n = -1.45,
                        Ea = (12230, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(47.6, 'cm^3/(mol*s)'), n=2.75, Ea=(-796.4, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(51.6, 'cm^3/(mol*s)'), n=2.73, Ea=(-768.3, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(55.5, 'cm^3/(mol*s)'), n=2.73, Ea=(-658.5, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(46, 'cm^3/(mol*s)'), n=2.76, Ea=(-492.8, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.75, 'cm^3/(mol*s)'), n=3.07, Ea=(-601, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.48, 'cm^3/(mol*s)'), n=3.07, Ea=(85.7, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.47e+08, 'cm^3/(mol*s)'), n=0, Ea=(955, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(20.2, 'cm^3/(mol*s)'), n=2.94, Ea=(1847, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + O2 <=> C2H2 + HO2""",
)

entry(
    index = 272,
    label = "C2H3 + O2 <=> CH2O + HCO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.49e+36, 'cm^3/(mol*s)'),
                        n = -7.6,
                        Ea = (12640, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.43e+36, 'cm^3/(mol*s)'),
                        n = -7.6,
                        Ea = (12610, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.95e+36, 'cm^3/(mol*s)'),
                        n = -7.57,
                        Ea = (12490, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.73e+35, 'cm^3/(mol*s)'),
                        n = -7.32,
                        Ea = (11820, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.43e+36, 'cm^3/(mol*s)'),
                        n = -7.47,
                        Ea = (12460, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.18e+35, 'cm^3/(mol*s)'),
                        n = -7.2,
                        Ea = (13430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.19e+20, 'cm^3/(mol*s)'),
                        n = -2.57,
                        Ea = (5578, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.73e+33, 'cm^3/(mol*s)'),
                        n = -6.28,
                        Ea = (16000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.54e+15, 'cm^3/(mol*s)'),
                        n = -1.28,
                        Ea = (515.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.59e+15, 'cm^3/(mol*s)'),
                        n = -1.28,
                        Ea = (513, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.81e+15, 'cm^3/(mol*s)'),
                        n = -1.29,
                        Ea = (520.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.08e+15, 'cm^3/(mol*s)'),
                        n = -1.31,
                        Ea = (645.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.45e+15, 'cm^3/(mol*s)'),
                        n = -1.36,
                        Ea = (1066, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.56e+15, 'cm^3/(mol*s)'),
                        n = -1.18,
                        Ea = (1429, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.03e+69, 'cm^3/(mol*s)'),
                        n = -19.23,
                        Ea = (14760, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.21e+10, 'cm^3/(mol*s)'),
                        n = 0.19,
                        Ea = (830.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + O2 <=> CH2O + HCO""",
)

entry(
    index = 273,
    label = "C2H3 + O2 => CH2O + H + CO",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (5.82e+36, 'cm^3/(mol*s)'),
                        n = -7.6,
                        Ea = (12640, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.66e+36, 'cm^3/(mol*s)'),
                        n = -7.6,
                        Ea = (12610, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.55e+36, 'cm^3/(mol*s)'),
                        n = -7.57,
                        Ea = (12490, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.36e+35, 'cm^3/(mol*s)'),
                        n = -7.32,
                        Ea = (11820, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.35e+36, 'cm^3/(mol*s)'),
                        n = -7.47,
                        Ea = (12460, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.21e+36, 'cm^3/(mol*s)'),
                        n = -7.2,
                        Ea = (13430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.43e+20, 'cm^3/(mol*s)'),
                        n = -2.57,
                        Ea = (5578, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.36e+33, 'cm^3/(mol*s)'),
                        n = -6.28,
                        Ea = (16000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.06e+16, 'cm^3/(mol*s)'),
                        n = -1.28,
                        Ea = (515.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.07e+16, 'cm^3/(mol*s)'),
                        n = -1.28,
                        Ea = (513, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.13e+16, 'cm^3/(mol*s)'),
                        n = -1.29,
                        Ea = (520.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.42e+16, 'cm^3/(mol*s)'),
                        n = -1.31,
                        Ea = (645.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.2e+16, 'cm^3/(mol*s)'),
                        n = -1.36,
                        Ea = (1066, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.98e+15, 'cm^3/(mol*s)'),
                        n = -1.18,
                        Ea = (1429, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.39e+69, 'cm^3/(mol*s)'),
                        n = -19.23,
                        Ea = (14760, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.81e+10, 'cm^3/(mol*s)'),
                        n = 0.19,
                        Ea = (830.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + O2 => CH2O + H + CO""",
)

entry(
    index = 274,
    label = "C2H3 + O2 <=> CO + CH3O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.19e+18, 'cm^3/(mol*s)'),
                        n = -2.66,
                        Ea = (3201, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.06e+14, 'cm^3/(mol*s)'),
                        n = -1.32,
                        Ea = (885.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.34e+14, 'cm^3/(mol*s)'),
                        n = -1.33,
                        Ea = (900.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.03e+11, 'cm^3/(mol*s)'),
                        n = -0.33,
                        Ea = (-747.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.89e+12, 'cm^3/(mol*s)'),
                        n = -3,
                        Ea = (-8995, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.93e+24, 'cm^3/(mol*s)'),
                        n = -5.63,
                        Ea = (1.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.1e+18, 'cm^3/(mol*s)'),
                        n = -2.22,
                        Ea = (5178, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.79e+32, 'cm^3/(mol*s)'),
                        n = -6.45,
                        Ea = (16810, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.29e+09, 'cm^3/(mol*s)'),
                        n = 0.18,
                        Ea = (-1717, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.99e+11, 'cm^3/(mol*s)'),
                        n = -2.93,
                        Ea = (-9564, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.91e+11, 'cm^3/(mol*s)'),
                        n = -2.93,
                        Ea = (-10120, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.77e+21, 'cm^3/(mol*s)'),
                        n = -3.54,
                        Ea = (4772, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.99e+15, 'cm^3/(mol*s)'),
                        n = -1.62,
                        Ea = (1849, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.33e+16, 'cm^3/(mol*s)'),
                        n = -1.96,
                        Ea = (3324, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.02e+72, 'cm^3/(mol*s)'),
                        n = -20.69,
                        Ea = (15860, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.1e+09, 'cm^3/(mol*s)'),
                        n = 0.31,
                        Ea = (1024, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + O2 <=> CO + CH3O""",
)

entry(
    index = 275,
    label = "C2H3 + O2 <=> CO2 + CH3",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.37e+35, 'cm^3/(mol*s)'),
                        n = -7.76,
                        Ea = (12630, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.73e+35, 'cm^3/(mol*s)'),
                        n = -7.72,
                        Ea = (12520, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.47e+34, 'cm^3/(mol*s)'),
                        n = -7.55,
                        Ea = (12140, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.25e+31, 'cm^3/(mol*s)'),
                        n = -6.7,
                        Ea = (10440, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.63e+35, 'cm^3/(mol*s)'),
                        n = -7.75,
                        Ea = (12830, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.09e+35, 'cm^3/(mol*s)'),
                        n = -7.53,
                        Ea = (14050, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.84e+18, 'cm^3/(mol*s)'),
                        n = -2.44,
                        Ea = (5408, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.21e+32, 'cm^3/(mol*s)'),
                        n = -6.32,
                        Ea = (16190, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 0.316, 1, 3.16, 10, 31.6, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (6.27e+13, 'cm^3/(mol*s)'),
                        n = -1.16,
                        Ea = (406.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.24e+13, 'cm^3/(mol*s)'),
                        n = -1.16,
                        Ea = (401.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.12e+13, 'cm^3/(mol*s)'),
                        n = -1.16,
                        Ea = (397, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.32e+13, 'cm^3/(mol*s)'),
                        n = -1.14,
                        Ea = (446.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.45e+14, 'cm^3/(mol*s)'),
                        n = -1.26,
                        Ea = (987.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.02e+13, 'cm^3/(mol*s)'),
                        n = -1.11,
                        Ea = (1409, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.4e+70, 'cm^3/(mol*s)'),
                        n = -20.11,
                        Ea = (15430, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.21e+08, 'cm^3/(mol*s)'),
                        n = 0.25,
                        Ea = (855.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + O2 <=> CO2 + CH3""",
)

entry(
    index = 291,
    label = "C2H3 + H <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H3 + H <=> C2H2 + H2""",
)

entry(
    index = 293,
    label = "C2H3 + OH <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.011e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H3 + OH <=> C2H2 + H2O""",
)

entry(
    index = 294,
    label = "C2H3 + CH3 <=> CH4 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.92e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H3 + CH3 <=> CH4 + C2H2""",
)

entry(
    index = 295,
    label = "C2H3 + C2H3 <=> C2H2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H3 + C2H3 <=> C2H2 + C2H4""",
)

entry(
    index = 296,
    label = "C2H + H <=> C2H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.646,
        T3 = (132, 'K'),
        T1 = (1315, 'K'),
        T2 = (5566, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is C2H + H <=> C2H2""",
)

entry(
    index = 298,
    label = "C2H2 + O <=> CH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.395e+08, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (2472, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H2 + O <=> CH2 + CO""",
)

entry(
    index = 301,
    label = "C2H2 + HCO <=> C2H3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H2 + HCO <=> C2H3 + CO""",
)

entry(
    index = 308,
    label = "C2H2 + OH <=> C2H + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.632e+06, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (17060, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H2 + OH <=> C2H + H2O""",
)

entry(
    index = 311,
    label = "C2H2 + OH <=> CH3 + CO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (475700, 'cm^3/(mol*s)'),
                n = 1.68,
                Ea = (-329.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.372e+06, 'cm^3/(mol*s)'),
                n = 1.4,
                Ea = (226.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.648e+07, 'cm^3/(mol*s)'),
                n = 1.05,
                Ea = (1115, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.277e+09, 'cm^3/(mol*s)'),
                n = 0.73,
                Ea = (2579, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.312e+08, 'cm^3/(mol*s)'),
                n = 0.92,
                Ea = (3736, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(825000, 'cm^3/(mol*s)'), n=1.77, Ea=(4697, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H2 + OH <=> CH3 + CO""",
)

entry(
    index = 314,
    label = "C2H + O2 <=> CO2 + CHV",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H + O2 <=> CO2 + CHV""",
)

entry(
    index = 315,
    label = "C2H + O2 <=> HCO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H + O2 <=> HCO + CO""",
)

entry(
    index = 316,
    label = "C2H + O <=> CO + CHV",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(6.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H + O <=> CO + CHV""",
)

entry(
    index = 317,
    label = "C2H + H2 <=> H + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(490000, 'cm^3/(mol*s)'), n=2.5, Ea=(560, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H + H2 <=> H + C2H2""",
)

entry(
    index = 418,
    label = "CH3OCH3 <=> CH3 + CH3O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.33e+19, 's^-1'), n=-0.661, Ea=(84139, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.72e+59, 'cm^3/(mol*s)'),
            n = -11.4,
            Ea = (93295.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1e-30, 'K'),
        T1 = (880, 'K'),
        efficiencies = {'C': 3, 'O=C=O': 3, 'CC': 4.5, '[H][H]': 3, 'O': 9, 'COC': 5, 'N#N': 1.5, '[C]=O': 2.25},
    ),
    shortDesc = u"""The chemkin file reaction is CH3OCH3 <=> CH3 + CH3O""",
)

entry(
    index = 419,
    label = "CH3OCH3 + OH <=> CH3OCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (935000, 'cm^3/(mol*s)'),
        n = 2.29,
        Ea = (-780.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OCH3 + OH <=> CH3OCH2 + H2O""",
)

entry(
    index = 420,
    label = "CH3OCH3 + H <=> CH3OCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.721e+06, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (3384, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OCH3 + H <=> CH3OCH2 + H2""",
)

entry(
    index = 421,
    label = "CH3OCH3 + O <=> CH3OCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.75e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (2250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OCH3 + O <=> CH3OCH2 + OH""",
)

entry(
    index = 422,
    label = "CH3OCH3 + HO2 <=> CH3OCH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00317, 'cm^3/(mol*s)'),
        n = 4.64,
        Ea = (10556, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OCH3 + HO2 <=> CH3OCH2 + H2O2""",
)

entry(
    index = 424,
    label = "CH3OCH3 + CH3 <=> CH3OCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.02, 'cm^3/(mol*s)'), n=3.78, Ea=(9687.1, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OCH3 + CH3 <=> CH3OCH2 + CH4""",
)

entry(
    index = 425,
    label = "CH3OCH3 + O2 <=> CH3OCH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(44910, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OCH3 + O2 <=> CH3OCH2 + HO2""",
)

entry(
    index = 426,
    label = "CH3OCH3 + CH3O <=> CH3OCH2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(4074, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OCH3 + CH3O <=> CH3OCH2 + CH3OH""",
)

entry(
    index = 430,
    label = "CH3OCH2 + CH3O <=> CH3OCH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OCH2 + CH3O <=> CH3OCH3 + CH2O""",
)

entry(
    index = 431,
    label = "CH3OCH2 + CH2O <=> CH3OCH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5490, 'cm^3/(mol*s)'), n=2.8, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OCH2 + CH2O <=> CH3OCH3 + HCO""",
)

entry(
    index = 433,
    label = "CH3OCH2 <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (7.494e+23, 's^-1'),
                n = -4.5152,
                Ea = (25236.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.921e+28, 's^-1'),
                n = -5.7271,
                Ea = (27494.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.229e+29, 's^-1'),
                n = -5.6103,
                Ea = (28898.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.608e+27, 's^-1'),
                n = -4.7073,
                Ea = (29735.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.659e+29, 's^-1'),
                n = -4.9358,
                Ea = (31785.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH3OCH2 <=> CH3 + CH2O""",
)

entry(
    index = 436,
    label = "CH3OCH2 + O2 => CH2O + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 1, 2, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.01e+21, 'cm^3/(mol*s)'),
                n = -3.18,
                Ea = (3067, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.73e+23, 'cm^3/(mol*s)'),
                n = -3.55,
                Ea = (4050, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.04e+31, 'cm^3/(mol*s)'),
                n = -5.76,
                Ea = (11594, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.99e+31, 'cm^3/(mol*s)'),
                n = -5.87,
                Ea = (12710, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.39e+30, 'cm^3/(mol*s)'),
                n = -5.59,
                Ea = (14517, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.09e+30, 'cm^3/(mol*s)'),
                n = -5.3,
                Ea = (15051, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.58e+28, 'cm^3/(mol*s)'),
                n = -4.88,
                Ea = (15664, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.41e+27, 'cm^3/(mol*s)'),
                n = -4.55,
                Ea = (16107, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH3OCH2 + O2 => CH2O + CH2O + OH""",
)

entry(
    index = 456,
    label = "CH3O + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + HCO <=> CH3OH + CO""",
)

entry(
    index = 482,
    label = "C3H8 <=> CH3 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.29e+37, 's^-1'), n=-5.84, Ea=(97380, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.64e+74, 'cm^3/(mol*s)'),
            n = -15.74,
            Ea = (98714, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.31,
        T3 = (50, 'K'),
        T1 = (3000, 'K'),
        T2 = (9000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is C3H8 <=> CH3 + C2H5""",
)

entry(
    index = 483,
    label = "NC3H7 + H <=> C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NC3H7 + H <=> C3H8""",
)

entry(
    index = 484,
    label = "IC3H7 + H <=> C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is IC3H7 + H <=> C3H8""",
)

entry(
    index = 485,
    label = "C3H8 + IC3H7 <=> NC3H7 + C3H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(12900, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + IC3H7 <=> NC3H7 + C3H8""",
)

entry(
    index = 486,
    label = "C3H8 + O2 <=> IC3H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49640, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + O2 <=> IC3H7 + HO2""",
)

entry(
    index = 487,
    label = "C3H8 + H <=> IC3H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + H <=> IC3H7 + H2""",
)

entry(
    index = 488,
    label = "C3H8 + O <=> IC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(549000, 'cm^3/(mol*s)'), n=2.5, Ea=(3140, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + O <=> IC3H7 + OH""",
)

entry(
    index = 489,
    label = "C3H8 + OH <=> IC3H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H8 + OH <=> IC3H7 + H2O""",
)

entry(
    index = 490,
    label = "C3H8 + HO2 <=> IC3H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(63.2, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + HO2 <=> IC3H7 + H2O2""",
)

entry(
    index = 491,
    label = "C3H8 + CH3 <=> IC3H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(64000, 'cm^3/(mol*s)'), n=2.17, Ea=(7520, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + CH3 <=> IC3H7 + CH4""",
)

entry(
    index = 492,
    label = "C3H8 + C2H3 <=> IC3H7 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + C2H3 <=> IC3H7 + C2H4""",
)

entry(
    index = 493,
    label = "C3H8 + C2H5 <=> IC3H7 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + C2H5 <=> IC3H7 + C2H6""",
)

entry(
    index = 494,
    label = "C3H8 + C3H5-A <=> IC3H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(16200, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + C3H5-A <=> IC3H7 + C3H6""",
)

entry(
    index = 495,
    label = "C3H8 + CH3O <=> IC3H7 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + CH3O <=> IC3H7 + CH3OH""",
)

entry(
    index = 502,
    label = "C3H8 + O2 <=> NC3H7 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + O2 <=> NC3H7 + HO2""",
)

entry(
    index = 503,
    label = "C3H8 + H <=> NC3H7 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(349000, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + H <=> NC3H7 + H2""",
)

entry(
    index = 504,
    label = "C3H8 + O <=> NC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.71e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5505, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H8 + O <=> NC3H7 + OH""",
)

entry(
    index = 505,
    label = "C3H8 + OH <=> NC3H7 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.054e+10, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H8 + OH <=> NC3H7 + H2O""",
)

entry(
    index = 506,
    label = "C3H8 + HO2 <=> NC3H7 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + HO2 <=> NC3H7 + H2O2""",
)

entry(
    index = 507,
    label = "C3H8 + CH3 <=> NC3H7 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + CH3 <=> NC3H7 + CH4""",
)

entry(
    index = 508,
    label = "C3H8 + C2H3 <=> NC3H7 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + C2H3 <=> NC3H7 + C2H4""",
)

entry(
    index = 509,
    label = "C3H8 + C2H5 <=> NC3H7 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + C2H5 <=> NC3H7 + C2H6""",
)

entry(
    index = 510,
    label = "C3H8 + C3H5-A <=> NC3H7 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + C3H5-A <=> NC3H7 + C3H6""",
)

entry(
    index = 511,
    label = "C3H8 + CH3O <=> NC3H7 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H8 + CH3O <=> NC3H7 + CH3OH""",
)

entry(
    index = 518,
    label = "IC3H7 + H <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is IC3H7 + H <=> C2H5 + CH3""",
)

entry(
    index = 519,
    label = "IC3H7 + OH <=> C3H6 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is IC3H7 + OH <=> C3H6 + H2O""",
)

entry(
    index = 531,
    label = "NC3H7 + O2 <=> C3H6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e-19, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NC3H7 + O2 <=> C3H6 + HO2""",
)

entry(
    index = 623,
    label = "C2H3 + CH3 <=> C3H6",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.27e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9769.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1341, 'K'),
        T1 = (60000, 'K'),
        T2 = (10140, 'K'),
        efficiencies = {},
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + CH3 <=> C3H6""",
)

entry(
    index = 632,
    label = "C2H3 + CH3 <=> C3H5-A + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.12e+29, 'cm^3/(mol*s)'),
                        n = -4.95,
                        Ea = (8000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.86e+30, 'cm^3/(mol*s)'),
                        n = -5.03,
                        Ea = (11300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.3e+29, 'cm^3/(mol*s)'),
                        n = -4.57,
                        Ea = (14400, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.32e+30, 'cm^3/(mol*s)'),
                        n = -4.54,
                        Ea = (19300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.16e+28, 'cm^3/(mol*s)'),
                        n = -4.03,
                        Ea = (23800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (5.73e+15, 'cm^3/(mol*s)'),
                        n = -0.77,
                        Ea = (1195.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.06e+13, 'cm^3/(mol*s)'),
                        n = -0.074,
                        Ea = (1428.7, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.48e+10, 'cm^3/(mol*s)'),
                        n = 0.6,
                        Ea = (1421.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.1e+06, 'cm^3/(mol*s)'),
                        n = 1.71,
                        Ea = (1056.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (0.137, 'cm^3/(mol*s)'),
                        n = 3.91,
                        Ea = (-353.55, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + CH3 <=> C3H5-A + H""",
)

entry(
    index = 633,
    label = "C3H6 <=> C2H3 + CH3",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.88e+78, 's^-1'), n=-18.7, Ea=(130000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.73e+76, 's^-1'), n=-17.9, Ea=(132000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.8e+75, 's^-1'), n=-17.2, Ea=(134000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.12e+71, 's^-1'), n=-15.8, Ea=(136000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.15e+64, 's^-1'), n=-13.4, Ea=(135000, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1.69e+59, 's^-1'), n=-13.6, Ea=(113290, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2e+60, 's^-1'), n=-13.7, Ea=(114890, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.7e+54, 's^-1'), n=-11.8, Ea=(113840, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.06e+47, 's^-1'), n=-9.27, Ea=(111510, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.29e+38, 's^-1'), n=-6.7, Ea=(108740, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 <=> C2H3 + CH3""",
)

entry(
    index = 634,
    label = "C3H6 <=> C3H5-A + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(9.16e+74, 's^-1'), n=-17.6, Ea=(120000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.73e+70, 's^-1'), n=-16, Ea=(120000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.08e+71, 's^-1'), n=-15.9, Ea=(124860, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.4e+65, 's^-1'), n=-14.2, Ea=(125000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(8.05e+56, 's^-1'), n=-11.5, Ea=(122000, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(2.98e+54, 's^-1'), n=-12.3, Ea=(101200, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.37e+43, 's^-1'), n=-8.87, Ea=(96365, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6.28e+42, 's^-1'), n=-8.51, Ea=(98004, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.73e+35, 's^-1'), n=-6.26, Ea=(95644, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.34e+28, 's^-1'), n=-4.06, Ea=(93114, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 <=> C3H5-A + H""",
)

entry(
    index = 641,
    label = "C3H5-T + H <=> C3H6",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (4.96e+60, 'cm^3/(mol*s)'),
                        n = -15.2,
                        Ea = (18000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.2e+62, 'cm^3/(mol*s)'),
                        n = -15.1,
                        Ea = (20100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.31e+60, 'cm^3/(mol*s)'),
                        n = -14,
                        Ea = (21900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.69e+54, 'cm^3/(mol*s)'),
                        n = -12,
                        Ea = (22100, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.15e+50, 'cm^3/(mol*s)'),
                        n = -10.4,
                        Ea = (23300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.49e+48, 'cm^3/(mol*s)'),
                        n = -12,
                        Ea = (7203.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.76e+46, 'cm^3/(mol*s)'),
                        n = -11.1,
                        Ea = (7629.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.09e+40, 'cm^3/(mol*s)'),
                        n = -8.66,
                        Ea = (6447.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.38e+31, 'cm^3/(mol*s)'),
                        n = -5.73,
                        Ea = (4506, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.69e+25, 'cm^3/(mol*s)'),
                        n = -3.83,
                        Ea = (3250.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-T + H <=> C3H6""",
)

entry(
    index = 642,
    label = "C3H5-T + H <=> C3H5-A + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.11e+17, 'cm^3/(mol*s)'),
                        n = -1.08,
                        Ea = (1290, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.05e+29, 'cm^3/(mol*s)'),
                        n = -4.91,
                        Ea = (8540, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.98e+30, 'cm^3/(mol*s)'),
                        n = -4.79,
                        Ea = (12000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.22e+28, 'cm^3/(mol*s)'),
                        n = -4.14,
                        Ea = (15400, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.28e+29, 'cm^3/(mol*s)'),
                        n = -4.12,
                        Ea = (20900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (6410, 'cm^3/(mol*s)'),
                        n = 2.61,
                        Ea = (-3778.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.19e+14, 'cm^3/(mol*s)'),
                        n = -0.3,
                        Ea = (1090.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (8.17e+11, 'cm^3/(mol*s)'),
                        n = 0.49,
                        Ea = (1184.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.79e+09, 'cm^3/(mol*s)'),
                        n = 1.09,
                        Ea = (1187.5, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(6750, 'cm^3/(mol*s)'), n=2.7, Ea=(373.8, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-T + H <=> C3H5-A + H""",
)

entry(
    index = 643,
    label = "C3H5-T + H <=> C2H3 + CH3",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (3.31e+16, 'cm^3/(mol*s)'),
                        n = -0.69,
                        Ea = (5200, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.04e+16, 'cm^3/(mol*s)'),
                        n = -0.81,
                        Ea = (4800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.01e+24, 'cm^3/(mol*s)'),
                        n = -2.86,
                        Ea = (10900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.75e+26, 'cm^3/(mol*s)'),
                        n = -3.31,
                        Ea = (15800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.15e+32, 'cm^3/(mol*s)'),
                        n = -4.83,
                        Ea = (26000, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.04e+13, 'cm^3/(mol*s)'),
                        n = -0.14,
                        Ea = (1150, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.17e+10, 'cm^3/(mol*s)'),
                        n = 0.67,
                        Ea = (673.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.97e+08, 'cm^3/(mol*s)'),
                        n = 1.36,
                        Ea = (1596.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.41e+07, 'cm^3/(mol*s)'),
                        n = 1.57,
                        Ea = (2108.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.7e+12, 'cm^3/(mol*s)'),
                        n = 0.32,
                        Ea = (6791.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-T + H <=> C2H3 + CH3""",
)

entry(
    index = 644,
    label = "C3H6 <=> C3H5-S + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.71e+69, 's^-1'), n=-16.09, Ea=(140000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 <=> C3H5-S + H""",
)

entry(
    index = 645,
    label = "C3H6 + H <=> C3H5-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (364400, 'cm^3/(mol*s)'),
        n = 2.455,
        Ea = (4361.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + H <=> C3H5-A + H2""",
)

entry(
    index = 646,
    label = "C3H6 + O2 <=> C3H5-A + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.96e+19, 'cm^3/(mol*s)'),
        n = -1.67,
        Ea = (46192.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + O2 <=> C3H5-A + HO2""",
)

entry(
    index = 647,
    label = "C3H6 + O <=> C3H5-A + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + O <=> C3H5-A + OH""",
)

entry(
    index = 648,
    label = "C3H6 + OH <=> C3H5-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.46e+06, 'cm^3/(mol*s)'),
        n = 2.072,
        Ea = (1050.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + OH <=> C3H5-A + H2O""",
)

entry(
    index = 649,
    label = "C3H6 + HO2 <=> C3H5-A + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0307, 'cm^3/(mol*s)'),
        n = 4.403,
        Ea = (13547.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + HO2 <=> C3H5-A + H2O2""",
)

entry(
    index = 650,
    label = "C3H6 + CH3 <=> C3H5-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 + CH3 <=> C3H5-A + CH4""",
)

entry(
    index = 651,
    label = "C3H6 + CH3O <=> C3H5-A + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 + CH3O <=> C3H5-A + CH3OH""",
)

entry(
    index = 653,
    label = "C3H6 + C2H5 <=> C3H5-A + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9800, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 + C2H5 <=> C3H5-A + C2H6""",
)

entry(
    index = 658,
    label = "C3H6 + H <=> C3H5-T + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (149.8, 'cm^3/(mol*s)'),
        n = 3.381,
        Ea = (8909.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + H <=> C3H5-T + H2""",
)

entry(
    index = 659,
    label = "C3H6 + O <=> C3H5-T + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7632, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + O <=> C3H5-T + OH""",
)

entry(
    index = 660,
    label = "C3H6 + OH <=> C3H5-T + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.979,
        Ea = (2235.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + OH <=> C3H5-T + H2O""",
)

entry(
    index = 661,
    label = "C3H6 + HO2 <=> C3H5-T + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15600, 'cm^3/(mol*s)'),
        n = 2.82,
        Ea = (24427.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + HO2 <=> C3H5-T + H2O2""",
)

entry(
    index = 662,
    label = "C3H6 + O2 <=> C3H5-T + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(58770, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 + O2 <=> C3H5-T + HO2""",
)

entry(
    index = 663,
    label = "C3H6 + CH3 <=> C3H5-T + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 + CH3 <=> C3H5-T + CH4""",
)

entry(
    index = 664,
    label = "C3H6 + H <=> C3H5-S + H2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (510.1, 'cm^3/(mol*s)'),
                n = 3.234,
                Ea = (12357, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (396.9, 'cm^3/(mol*s)'),
                n = 3.252,
                Ea = (12007, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(397, 'cm^3/(mol*s)'), n=3.252, Ea=(12007, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(510, 'cm^3/(mol*s)'), n=3.234, Ea=(12357, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + H <=> C3H5-S + H2""",
)

entry(
    index = 665,
    label = "C3H6 + O2 <=> C3H5-S + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(62270, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 + O2 <=> C3H5-S + HO2""",
)

entry(
    index = 666,
    label = "C3H6 + O <=> C3H5-S + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8959.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + O <=> C3H5-S + OH""",
)

entry(
    index = 667,
    label = "C3H6 + OH <=> C3H5-S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (186000, 'cm^3/(mol*s)'),
        n = 2.369,
        Ea = (2502, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + OH <=> C3H5-S + H2O""",
)

entry(
    index = 668,
    label = "C3H6 + HO2 <=> C3H5-S + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (957, 'cm^3/(mol*s)'),
        n = 3.059,
        Ea = (20798.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + HO2 <=> C3H5-S + H2O2""",
)

entry(
    index = 669,
    label = "C3H6 + CH3 <=> C3H5-S + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.348, 'cm^3/(mol*s)'), n=3.5, Ea=(12850, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 + CH3 <=> C3H5-S + CH4""",
)

entry(
    index = 670,
    label = "C3H6 + O <=> C2H5 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.45e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + O <=> C2H5 + HCO""",
)

entry(
    index = 673,
    label = "C3H6 + H <=> NC3H7",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (7.99e+81, 'cm^3/(mol*s)'),
                        n = -23.161,
                        Ea = (22239, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.24e+68, 'cm^3/(mol*s)'),
                        n = -18.427,
                        Ea = (19665, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.04e+49, 'cm^3/(mol*s)'),
                        n = -11.5,
                        Ea = (15359, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.2e+41, 'cm^3/(mol*s)'),
                        n = -8.892,
                        Ea = (14637, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.85e+26, 'cm^3/(mol*s)'),
                        n = -5.83,
                        Ea = (3865.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.82e+30, 'cm^3/(mol*s)'),
                        n = -6.49,
                        Ea = (5470.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.78e+28, 'cm^3/(mol*s)'),
                        n = -5.57,
                        Ea = (5625.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.46e+25, 'cm^3/(mol*s)'),
                        n = -4.28,
                        Ea = (5247.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.22e+27, 'cm^3/(mol*s)'),
                        n = -4.39,
                        Ea = (9345.8, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + H <=> NC3H7""",
)

entry(
    index = 674,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.54e+09, 'cm^3/(mol*s)'),
                        n = 1.35,
                        Ea = (2542, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.88e+10, 'cm^3/(mol*s)'),
                        n = 0.87,
                        Ea = (3599.6, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.67e+12, 'cm^3/(mol*s)'),
                        n = 0.47,
                        Ea = (5431.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.25e+22, 'cm^3/(mol*s)'),
                        n = -2.6,
                        Ea = (12898, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.32e+23, 'cm^3/(mol*s)'),
                        n = -2.42,
                        Ea = (16500, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (124000, 'cm^3/(mol*s)'),
                        n = 2.52,
                        Ea = (3679.1, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(2510, 'cm^3/(mol*s)'), n=2.91, Ea=(3980.9, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + H <=> C2H4 + CH3""",
)

entry(
    index = 675,
    label = "C3H6 + H <=> IC3H7",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.35e+44, 'cm^3/(mol*s)'),
                        n = -10.68,
                        Ea = (8196.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.11e+57, 'cm^3/(mol*s)'),
                        n = -14.23,
                        Ea = (15147, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.26e+61, 'cm^3/(mol*s)'),
                        n = -14.94,
                        Ea = (20161, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.3e+56, 'cm^3/(mol*s)'),
                        n = -13.12,
                        Ea = (20667, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.11e+50, 'cm^3/(mol*s)'),
                        n = -10.8,
                        Ea = (20202, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.17e+130, 'cm^3/(mol*s)'),
                        n = -32.58,
                        Ea = (136140, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.25e+29, 'cm^3/(mol*s)'),
                        n = -5.84,
                        Ea = (4241.9, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+30, 'cm^3/(mol*s)'),
                        n = -5.63,
                        Ea = (5613.4, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.11e+26, 'cm^3/(mol*s)'),
                        n = -4.44,
                        Ea = (5182.3, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.73e+23, 'cm^3/(mol*s)'),
                        n = -3.26,
                        Ea = (4597, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + H <=> IC3H7""",
)

entry(
    index = 676,
    label = "C2H4 + CH3 <=> NC3H7",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.67e+48, 'cm^3/(mol*s)'),
                        n = -12.54,
                        Ea = (18206, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+49, 'cm^3/(mol*s)'),
                        n = -12.04,
                        Ea = (20001, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.67e+47, 'cm^3/(mol*s)'),
                        n = -11.17,
                        Ea = (22366, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.81e+45, 'cm^3/(mol*s)'),
                        n = -10.03,
                        Ea = (23769, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.04e+40, 'cm^3/(mol*s)'),
                        n = -8.25,
                        Ea = (24214, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.0013, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.12e+43, 'cm^3/(mol*s)'),
                        n = -11.3,
                        Ea = (13080, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.28e+39, 'cm^3/(mol*s)'),
                        n = -9.88,
                        Ea = (13164, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.6e+33, 'cm^3/(mol*s)'),
                        n = -7.46,
                        Ea = (12416, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.85e+27, 'cm^3/(mol*s)'),
                        n = -5.38,
                        Ea = (11455, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.66e+21, 'cm^3/(mol*s)'),
                        n = -3.17,
                        Ea = (10241, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + CH3 <=> NC3H7""",
)

entry(
    index = 679,
    label = "C3H6 + HO2 <=> IC3H7 + O2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.9869, 9.87, 98.69], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.02e+07, 'cm^3/(mol*s)'),
                n = 1.16,
                Ea = (10273, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.31e+20, 'cm^3/(mol*s)'),
                n = -2.58,
                Ea = (19078, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.14e+28, 'cm^3/(mol*s)'),
                n = -4.92,
                Ea = (26212, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.87e+22, 'cm^3/(mol*s)'),
                n = -3.09,
                Ea = (26586, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + HO2 <=> IC3H7 + O2""",
)

entry(
    index = 681,
    label = "C3H5-A + H <=> C3H4-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1232, 'cm^3/(mol*s)'), n=3.035, Ea=(2582, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-A + H <=> C3H4-A + H2""",
)

entry(
    index = 682,
    label = "C3H5-A + OH <=> C3H4-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-A + OH <=> C3H4-A + H2O""",
)

entry(
    index = 683,
    label = "C3H5-A + CH3 <=> C3H4-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=-0.32, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-A + CH3 <=> C3H4-A + CH4""",
)

entry(
    index = 684,
    label = "C3H5-A + C2H5 <=> C3H4-A + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-A + C2H5 <=> C3H4-A + C2H6""",
)

entry(
    index = 685,
    label = "C3H5-A + C2H3 <=> C3H4-A + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-A + C2H3 <=> C3H4-A + C2H4""",
)

entry(
    index = 687,
    label = "C3H5-S + H <=> C3H4-A + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.333e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + H <=> C3H4-A + H2""",
)

entry(
    index = 688,
    label = "C3H5-S + CH3 <=> C3H4-A + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + CH3 <=> C3H4-A + CH4""",
)

entry(
    index = 689,
    label = "C3H5-S + H <=> C3H4-P + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + H <=> C3H4-P + H2""",
)

entry(
    index = 690,
    label = "C3H5-S + CH3 <=> C3H4-P + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + CH3 <=> C3H4-P + CH4""",
)

entry(
    index = 691,
    label = "C3H5-T + H <=> C3H4-P + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-T + H <=> C3H4-P + H2""",
)

entry(
    index = 692,
    label = "C3H5-T + CH3 <=> C3H4-P + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-T + CH3 <=> C3H4-P + CH4""",
)

entry(
    index = 693,
    label = "C3H5-A + C3H5-A <=> C3H4-A + C3H6",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 4, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.77e+40, 'cm^3/(mol*s)'),
                n = -9.3,
                Ea = (12470, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.97e+32, 'cm^3/(mol*s)'),
                n = -6.8,
                Ea = (9180, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.46e+28, 'cm^3/(mol*s)'),
                n = -5.5,
                Ea = (7410, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-A + C3H5-A <=> C3H4-A + C3H6""",
)

entry(
    index = 694,
    label = "C3H5-A + C2H5 <=> C2H4 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-A + C2H5 <=> C2H4 + C3H6""",
)

entry(
    index = 695,
    label = "C3H5-A + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-A + HCO <=> C3H6 + CO""",
)

entry(
    index = 696,
    label = "C3H5-S + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + HCO <=> C3H6 + CO""",
)

entry(
    index = 697,
    label = "C3H5-T + HCO <=> C3H6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-T + HCO <=> C3H6 + CO""",
)

entry(
    index = 698,
    label = "C3H5-S + O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + O <=> C2H4 + HCO""",
)

entry(
    index = 699,
    label = "C3H5-S + OH => C2H4 + HCO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + OH => C2H4 + HCO + H""",
)

entry(
    index = 700,
    label = "C3H5-S + HO2 => C2H4 + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + HO2 => C2H4 + HCO + OH""",
)

entry(
    index = 706,
    label = "C3H5-A + O2 <=> C3H4-A + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.99e+15, 'cm^3/(mol*s)'),
                n = -1.4,
                Ea = (22428, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.18e+21, 'cm^3/(mol*s)'),
                n = -2.85,
                Ea = (30755, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-A + O2 <=> C3H4-A + HO2""",
)

entry(
    index = 714,
    label = "C3H5-T + O2 <=> C3H4-A + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.59e+10, 'cm^3/(mol*s)'),
        n = -0.27,
        Ea = (-413.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-T + O2 <=> C3H4-A + HO2""",
)

entry(
    index = 733,
    label = "C2H3 + CH2O <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.11e+07, 'cm^3/(mol*s)'),
                n = 1.09,
                Ea = (1807.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+07, 'cm^3/(mol*s)'),
                n = 0.993,
                Ea = (1994.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+08, 'cm^3/(mol*s)'),
                n = 0.704,
                Ea = (2596.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.42e+10, 'cm^3/(mol*s)'),
                n = 0.209,
                Ea = (3934.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.45e+13, 'cm^3/(mol*s)'),
                n = -0.726,
                Ea = (6944.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.31e+14, 'cm^3/(mol*s)'),
                n = -0.866,
                Ea = (10965.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(16.5, 'cm^3/(mol*s)'), n=3.17, Ea=(9399.8, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + CH2O <=> C2H4 + HCO""",
)

entry(
    index = 780,
    label = "C2H + CH3 <=> C3H4-P",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H + CH3 <=> C3H4-P""",
)

entry(
    index = 781,
    label = "C3H4-A <=> C3H4-P",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.762e+39, 's^-1'), n=-7.8, Ea=(78446, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.786e+48, 's^-1'), n=-10, Ea=(88685, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-A <=> C3H4-P""",
)

entry(
    index = 805,
    label = "C3H4-A + H <=> C3H4-P + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.49e+10, 'cm^3/(mol*s)'),
                        n = 0.89,
                        Ea = (2503, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.48e+13, 'cm^3/(mol*s)'),
                        n = 0.26,
                        Ea = (4103, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.48e+15, 'cm^3/(mol*s)'),
                        n = -0.33,
                        Ea = (6436, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.35e+25, 'cm^3/(mol*s)'),
                        n = -3.23,
                        Ea = (13165, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.02e+24, 'cm^3/(mol*s)'),
                        n = -2.67,
                        Ea = (15552, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (1.79e+07, 'cm^3/(mol*s)'),
                        n = 1.98,
                        Ea = (4521, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(46300, 'cm^3/(mol*s)'), n=2.62, Ea=(4466, 'cal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-A + H <=> C3H4-P + H""",
)

entry(
    index = 806,
    label = "C3H4-A + H <=> C3H5-A",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.21e+61, 'cm^3/(mol*s)'),
                        n = -15.25,
                        Ea = (20076, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.24e+52, 'cm^3/(mol*s)'),
                        n = -12.02,
                        Ea = (17839, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.67e+51, 'cm^3/(mol*s)'),
                        n = -11.45,
                        Ea = (21340, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.75e+48, 'cm^3/(mol*s)'),
                        n = -10.27,
                        Ea = (22511, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.23e+43, 'cm^3/(mol*s)'),
                        n = -8.61,
                        Ea = (22522, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (2.8e+38, 'cm^3/(mol*s)'),
                        n = -8.67,
                        Ea = (8035, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.33e+36, 'cm^3/(mol*s)'),
                        n = -8.19,
                        Ea = (7462, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.32e+30, 'cm^3/(mol*s)'),
                        n = -5.78,
                        Ea = (6913, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.29e+26, 'cm^3/(mol*s)'),
                        n = -4.32,
                        Ea = (6163, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.38e+21, 'cm^3/(mol*s)'),
                        n = -2.71,
                        Ea = (5187, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-A + H <=> C3H5-A""",
)

entry(
    index = 807,
    label = "C3H4-A + H <=> C3H5-S",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+30, 'cm^3/(mol*s)'),
                n = -6.52,
                Ea = (15200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.4e+29, 'cm^3/(mol*s)'),
                n = -6.09,
                Ea = (16300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.6e+31, 'cm^3/(mol*s)'),
                n = -6.23,
                Ea = (18700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.2e+31, 'cm^3/(mol*s)'),
                n = -5.88,
                Ea = (21500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-A + H <=> C3H5-S""",
)

entry(
    index = 808,
    label = "C3H4-A + H <=> C3H5-T",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (6.44e+102, 'cm^3/(mol*s)'),
                        n = -27.51,
                        Ea = (51768, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.55e+53, 'cm^3/(mol*s)'),
                        n = -13.1,
                        Ea = (14472, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.9e+53, 'cm^3/(mol*s)'),
                        n = -12.59,
                        Ea = (16726, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.95e+51, 'cm^3/(mol*s)'),
                        n = -11.82,
                        Ea = (18286, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.21e+52, 'cm^3/(mol*s)'),
                        n = -11.64,
                        Ea = (22262, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.1e+54, 'cm^3/(mol*s)'),
                        n = -14.29,
                        Ea = (10809, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.88e+44, 'cm^3/(mol*s)'),
                        n = -11.21,
                        Ea = (8212, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.81e+40, 'cm^3/(mol*s)'),
                        n = -9.42,
                        Ea = (7850, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.6e+35, 'cm^3/(mol*s)'),
                        n = -7.57,
                        Ea = (7147, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.88e+29, 'cm^3/(mol*s)'),
                        n = -5.53,
                        Ea = (6581, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-A + H <=> C3H5-T""",
)

entry(
    index = 809,
    label = "C3H4-A + H <=> CH3 + C2H2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.23e+08, 'cm^3/(mol*s)'),
                        n = 1.53,
                        Ea = (4737, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.72e+09, 'cm^3/(mol*s)'),
                        n = 1.2,
                        Ea = (6834, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.26e+20, 'cm^3/(mol*s)'),
                        n = -1.83,
                        Ea = (15003, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.68e+16, 'cm^3/(mol*s)'),
                        n = -0.6,
                        Ea = (14754, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.37e+17, 'cm^3/(mol*s)'),
                        n = -0.79,
                        Ea = (17603, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(12300, 'cm^3/(mol*s)'), n=2.68, Ea=(6335, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.31e+08, 'cm^3/(mol*s)'),
                        n = 1.14,
                        Ea = (8886, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.28e+06, 'cm^3/(mol*s)'),
                        n = 1.71,
                        Ea = (9774, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-A + H <=> CH3 + C2H2""",
)

entry(
    index = 810,
    label = "C3H4-P + H <=> C3H5-T",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.85e+51, 'cm^3/(mol*s)'),
                        n = -13.04,
                        Ea = (12325, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.17e+52, 'cm^3/(mol*s)'),
                        n = -12.69,
                        Ea = (14226, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.87e+53, 'cm^3/(mol*s)'),
                        n = -12.51,
                        Ea = (16853, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.51e+51, 'cm^3/(mol*s)'),
                        n = -11.74,
                        Ea = (18331, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.51e+52, 'cm^3/(mol*s)'),
                        n = -11.58,
                        Ea = (22207, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.97e+46, 'cm^3/(mol*s)'),
                        n = -11.91,
                        Ea = (7456, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.59e+45, 'cm^3/(mol*s)'),
                        n = -11.23,
                        Ea = (8046, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.93e+39, 'cm^3/(mol*s)'),
                        n = -9.11,
                        Ea = (7458, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.8e+34, 'cm^3/(mol*s)'),
                        n = -7.29,
                        Ea = (6722, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.65e+29, 'cm^3/(mol*s)'),
                        n = -5.39,
                        Ea = (6150, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-P + H <=> C3H5-T""",
)

entry(
    index = 811,
    label = "C3H4-P + H <=> C3H5-S",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.38e+49, 'cm^3/(mol*s)'),
                        n = -12.75,
                        Ea = (14072, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.37e+51, 'cm^3/(mol*s)'),
                        n = -12.55,
                        Ea = (15428, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.88e+50, 'cm^3/(mol*s)'),
                        n = -11.9,
                        Ea = (16915, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.17e+49, 'cm^3/(mol*s)'),
                        n = -11.1,
                        Ea = (18746, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.49e+38, 'cm^3/(mol*s)'),
                        n = -10.11,
                        Ea = (7458, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.98e+43, 'cm^3/(mol*s)'),
                        n = -11.43,
                        Ea = (8736, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.75e+39, 'cm^3/(mol*s)'),
                        n = -9.51,
                        Ea = (8772, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.33e+40, 'cm^3/(mol*s)'),
                        n = -9.6,
                        Ea = (9401, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.44e+34, 'cm^3/(mol*s)'),
                        n = -7.36,
                        Ea = (8558, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-P + H <=> C3H5-S""",
)

entry(
    index = 812,
    label = "C3H4-P + H <=> CH3 + C2H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.44e+10, 'cm^3/(mol*s)'),
                n = 1.04,
                Ea = (3980, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.89e+10, 'cm^3/(mol*s)'),
                n = 0.989,
                Ea = (4114, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.46e+12, 'cm^3/(mol*s)'),
                n = 0.442,
                Ea = (5463, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.72e+14, 'cm^3/(mol*s)'),
                n = -0.01,
                Ea = (7134, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.9e+15, 'cm^3/(mol*s)'),
                n = -0.29,
                Ea = (8306, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-P + H <=> CH3 + C2H2""",
)

entry(
    index = 813,
    label = "C3H4-P + H <=> C3H5-A",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+60, 'cm^3/(mol*s)'),
                n = -14.56,
                Ea = (28100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.91e+60, 'cm^3/(mol*s)'),
                n = -14.37,
                Ea = (31644, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.04e+60, 'cm^3/(mol*s)'),
                n = -14.19,
                Ea = (32642, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.02e+59, 'cm^3/(mol*s)'),
                n = -13.89,
                Ea = (33953, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.2e+59, 'cm^3/(mol*s)'),
                n = -13.61,
                Ea = (34900, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6e+55, 'cm^3/(mol*s)'),
                n = -12.07,
                Ea = (37500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H4-P + H <=> C3H5-A""",
)

entry(
    index = 814,
    label = "C3H5-A <=> C3H5-T",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.9e+59, 's^-1'), n=-15.42, Ea=(75400, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.06e+56, 's^-1'), n=-14.08, Ea=(75868, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.8e+55, 's^-1'), n=-13.59, Ea=(75949, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.86e+53, 's^-1'), n=-12.81, Ea=(75883, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.4e+51, 's^-1'), n=-12.12, Ea=(75700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+43, 's^-1'), n=-9.27, Ea=(74000, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-A <=> C3H5-T""",
)

entry(
    index = 815,
    label = "C3H5-A <=> C3H5-S",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.3e+55, 's^-1'), n=-14.53, Ea=(73800, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5e+51, 's^-1'), n=-13.02, Ea=(73300, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.7e+48, 's^-1'), n=-11.73, Ea=(73700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.86e+44, 's^-1'), n=-9.84, Ea=(73400, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-A <=> C3H5-S""",
)

entry(
    index = 816,
    label = "C2H2 + CH3 <=> C3H5-T",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.8e+20, 'cm^3/(mol*s)'),
                n = -4.16,
                Ea = (18000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.99e+22, 'cm^3/(mol*s)'),
                n = -4.39,
                Ea = (18850, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(6e+23, 'cm^3/(mol*s)'), n=-4.6, Ea=(19571, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (7.31e+25, 'cm^3/(mol*s)'),
                n = -5.06,
                Ea = (21150, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.3e+27, 'cm^3/(mol*s)'),
                n = -5.55,
                Ea = (22900, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.8e+36, 'cm^3/(mol*s)'),
                n = -7.58,
                Ea = (31300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H2 + CH3 <=> C3H5-T""",
)

entry(
    index = 817,
    label = "C3H5-T <=> C3H5-S",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.6e+44, 's^-1'), n=-12.16, Ea=(52200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+48, 's^-1'), n=-12.71, Ea=(53900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.1e+52, 's^-1'), n=-13.37, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.8e+51, 's^-1'), n=-12.43, Ea=(59200, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-T <=> C3H5-S""",
)

entry(
    index = 818,
    label = "C2H2 + CH3 <=> C3H5-A",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.2e+53, 'cm^3/(mol*s)'),
                n = -13.32,
                Ea = (33200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.68e+53, 'cm^3/(mol*s)'),
                n = -12.82,
                Ea = (35730, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.64e+52, 'cm^3/(mol*s)'),
                n = -12.46,
                Ea = (36127, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.04e+51, 'cm^3/(mol*s)'),
                n = -11.89,
                Ea = (36476, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.4e+49, 'cm^3/(mol*s)'),
                n = -11.4,
                Ea = (36700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.8e+44, 'cm^3/(mol*s)'),
                n = -9.63,
                Ea = (37600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C2H2 + CH3 <=> C3H5-A""",
)

entry(
    index = 819,
    label = "CH3 + C2H2 <=> C3H5-S",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.78e+42, 'cm^3/(mol*s)'),
                        n = -10.4,
                        Ea = (13647, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.52e+44, 'cm^3/(mol*s)'),
                        n = -10.73,
                        Ea = (15256, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.19e+44, 'cm^3/(mol*s)'),
                        n = -10.19,
                        Ea = (18728, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.02e+43, 'cm^3/(mol*s)'),
                        n = -9.74,
                        Ea = (20561, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.42e+42, 'cm^3/(mol*s)'),
                        n = -8.91,
                        Ea = (22235, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.039, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e-10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (8.49e+35, 'cm^3/(mol*s)'),
                        n = -8.43,
                        Ea = (12356, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.04e+32, 'cm^3/(mol*s)'),
                        n = -7.01,
                        Ea = (12357, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.69e+27, 'cm^3/(mol*s)'),
                        n = -5.07,
                        Ea = (11690, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH3 + C2H2 <=> C3H5-S""",
)

entry(
    index = 821,
    label = "C3H4-P + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H4-P + O <=> C2H4 + CO""",
)

entry(
    index = 822,
    label = "C3H4-P + O <=> C2H3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(2010, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H4-P + O <=> C2H3 + HCO""",
)

entry(
    index = 823,
    label = "C3H4-A + O <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H4-A + O <=> C2H4 + CO""",
)

entry(
    index = 824,
    label = "C3H4-A + O <=> C2H2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.003, 'cm^3/(mol*s)'), n=4.61, Ea=(-4243, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H4-A + O <=> C2H2 + CH2O""",
)

entry(
    index = 834,
    label = "C3H4-P + HO2 => C2H4 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H4-P + HO2 => C2H4 + CO + OH""",
)

entry(
    index = 835,
    label = "C3H4-A + HO2 => C2H4 + CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H4-A + HO2 => C2H4 + CO + OH""",
)

entry(
    index = 1423,
    label = "C3H5-T + CH2O <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.11e+07, 'cm^3/(mol*s)'),
                n = 1.09,
                Ea = (1807.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+07, 'cm^3/(mol*s)'),
                n = 0.993,
                Ea = (1994.9, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+08, 'cm^3/(mol*s)'),
                n = 0.704,
                Ea = (2596.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.42e+10, 'cm^3/(mol*s)'),
                n = 0.209,
                Ea = (3934.2, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.45e+13, 'cm^3/(mol*s)'),
                n = -0.726,
                Ea = (6944.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.31e+14, 'cm^3/(mol*s)'),
                n = -0.866,
                Ea = (10965.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(16.5, 'cm^3/(mol*s)'), n=3.17, Ea=(9399.8, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-T + CH2O <=> C3H6 + HCO""",
)

entry(
    index = 1737,
    label = "C3H5-S + CH2O <=> C3H6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(16.5, 'cm^3/(mol*s)'), n=3.17, Ea=(9399.8, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + CH2O <=> C3H6 + HCO""",
)

entry(
    index = 3632,
    label = "H2O + H2O <=> H + OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.006e+26, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (120180, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is H2O + H2O <=> H + OH + H2O""",
)

entry(
    index = 3633,
    label = "HCO + HO2 <=> CO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HCO + HO2 <=> CO + H2O2""",
)

entry(
    index = 3638,
    label = "CH + O2 <=> CO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.9e+09, 'cm^3/(mol*s)'),
        n = 1.008,
        Ea = (-489.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH + O2 <=> CO2 + H""",
)

entry(
    index = 3639,
    label = "CH + O2 => CO + O + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (9.9e+09, 'cm^3/(mol*s)'),
        n = 1.008,
        Ea = (-489.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH + O2 => CO + O + H""",
)

entry(
    index = 3640,
    label = "CH2 => C + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.148e+14, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (55820, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is CH2 => C + H2""",
)

entry(
    index = 3641,
    label = "CH2 + O <=> CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.19e+13, 'cm^3/(mol*s)'), n=0, Ea=(536.5, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + O <=> CO + H2""",
)

entry(
    index = 3642,
    label = "CH2 + O2 => CO + OH + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.673e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1779.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2 + O2 => CO + OH + H""",
)

entry(
    index = 3643,
    label = "CH2 + O2 <=> CO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.968e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1908.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2 + O2 <=> CO2 + H2""",
)

entry(
    index = 3644,
    label = "CH2 + O2 <=> CH2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.328e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1501.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2 + O2 <=> CH2O + O""",
)

entry(
    index = 3645,
    label = "CH2 + O2 <=> CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.13e+11, 'cm^3/(mol*s)'), n=0, Ea=(1453, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + O2 <=> CO + H2O""",
)

entry(
    index = 3646,
    label = "CH2 + H2 <=> H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (440800, 'cm^3/(mol*s)'),
        n = 2.3,
        Ea = (7350.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2 + H2 <=> H + CH3""",
)

entry(
    index = 3647,
    label = "CH2 + HO2 <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + HO2 <=> OH + CH2O""",
)

entry(
    index = 3648,
    label = "CH2 + CH2O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.07407, 'cm^3/(mol*s)'),
        n = 4.21,
        Ea = (1623.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2 + CH2O <=> CH3 + HCO""",
)

entry(
    index = 3649,
    label = "CH2 + CH <=> H + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + CH <=> H + C2H2""",
)

entry(
    index = 3650,
    label = "CH2 + CH2 <=> C2H2 + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.094e+13, 'cm^3/(mol*s)'),
        n = 0.002,
        Ea = (8.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2 + CH2 <=> C2H2 + H + H""",
)

entry(
    index = 3651,
    label = "CH2 + CH2 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.773e+13, 'cm^3/(mol*s)'),
        n = 0.002,
        Ea = (8.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2 + CH2 <=> C2H2 + H2""",
)

entry(
    index = 3652,
    label = "CH2 + CO2 <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2 + CO2 <=> CH2O + CO""",
)

entry(
    index = 3664,
    label = "CH3 => CH + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.569e+15, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (81046, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3, 'CO': 3, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is CH3 => CH + H2""",
)

entry(
    index = 3665,
    label = "CH3 + O => CO + H2 + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.686e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3 + O => CO + H2 + H""",
)

entry(
    index = 3666,
    label = "CH3 + CH <=> H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3 + CH <=> H + C2H3""",
)

entry(
    index = 3669,
    label = "CH3O + O <=> OH + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + O <=> OH + CH2O""",
)

entry(
    index = 3670,
    label = "CH3O + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + OH <=> CH2O + H2O""",
)

entry(
    index = 3671,
    label = "CH3O + CO <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.57e+13, 'cm^3/(mol*s)'), n=0, Ea=(11804, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + CO <=> CH3 + CO2""",
)

entry(
    index = 3672,
    label = "CH3O + HCO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + HCO <=> CH2O + CH2O""",
)

entry(
    index = 3673,
    label = "CH3O + CH2 <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + CH2 <=> CH2O + CH3""",
)

entry(
    index = 3674,
    label = "CH2OH <=> CH3O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 5, 10, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.158e+18, 's^-1'), n=-4.592, Ea=(36016.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.81e+19, 's^-1'), n=-4.628, Ea=(35229.3, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.87e+21, 's^-1'), n=-4.771, Ea=(35111.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.797e+22, 's^-1'), n=-4.681, Ea=(35559.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.756e+22, 's^-1'), n=-4.499, Ea=(36133.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.449e+23, 's^-1'), n=-4.416, Ea=(36465.8, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.935e+23, 's^-1'), n=-4.199, Ea=(37365.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.423e+23, 's^-1'), n=-4.046, Ea=(37725.5, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH2OH <=> CH3O""",
)

entry(
    index = 3676,
    label = "CH2OH + H <=> CH3O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.46e+07, 'cm^3/(mol*s)'),
        n = 1.595,
        Ea = (7194.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH2OH + H <=> CH3O + H""",
)

entry(
    index = 3677,
    label = "CH2OH + CH2 <=> OH + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + CH2 <=> OH + C2H4""",
)

entry(
    index = 3678,
    label = "CH2OH + CH2 <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + CH2 <=> CH2O + CH3""",
)

entry(
    index = 3679,
    label = "CH2OH + CH3 <=> CH2O + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2OH + CH3 <=> CH2O + CH4""",
)

entry(
    index = 3680,
    label = "CH3OH <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.66e+12, 's^-1'), n=0.199, Ea=(89678.5, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.19e+25, 'cm^3/(mol*s)'),
            n = -2.75,
            Ea = (84971.1, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.014,
        T3 = (737.2, 'K'),
        T1 = (740.2, 'K'),
        T2 = (206500, 'K'),
        efficiencies = {'C': 2, 'CO': 3, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH <=> CH2O + H2""",
)

entry(
    index = 3682,
    label = "CH3OH <=> CH2OH + H",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.000132, 0.00132, 0.0132, 0.132, 1.32, 13.2, 132, 13200], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.11e+34, 's^-1'), n=-7.944, Ea=(111086, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.11e+37, 's^-1'), n=-8.323, Ea=(109174, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.733e+38, 's^-1'), n=-8.51, Ea=(107101, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.959e+41, 's^-1'), n=-8.969, Ea=(105979, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.086e+44, 's^-1'), n=-9.382, Ea=(107252, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.08e+45, 's^-1'), n=-9.263, Ea=(109268, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.717e+43, 's^-1'), n=-8.419, Ea=(110568, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.638e+29, 's^-1'), n=-3.838, Ea=(105075, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH <=> CH2OH + H""",
)

entry(
    index = 3683,
    label = "CH3OH <=> CH3O + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.000132, 0.00132, 0.0132, 0.132, 1.32, 13.2, 132, 13200], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.241e+28, 's^-1'), n=-7.012, Ea=(134030, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.218e+28, 's^-1'), n=-6.689, Ea=(130040, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.179e+30, 's^-1'), n=-6.772, Ea=(127195, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.517e+31, 's^-1'), n=-6.819, Ea=(121849, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.053e+34, 's^-1'), n=-7.292, Ea=(115732, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.06e+39, 's^-1'), n=-8.158, Ea=(114301, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.311e+42, 's^-1'), n=-8.531, Ea=(117206, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.484e+39, 's^-1'), n=-6.946, Ea=(123154, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH <=> CH3O + H""",
)

entry(
    index = 3684,
    label = "CH3OH + H <=> CH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (295700, 'cm^3/(mol*s)'),
        n = 2.485,
        Ea = (20627, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + H <=> CH3 + H2O""",
)

entry(
    index = 3685,
    label = "CH3OH + CH <=> CH2 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.522e+17, 'cm^3/(mol*s)'),
        n = -1.93,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + CH <=> CH2 + CH3O""",
)

entry(
    index = 3686,
    label = "CH3OH + CH <=> CH2 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.592e+18, 'cm^3/(mol*s)'),
        n = -1.93,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is CH3OH + CH <=> CH2 + CH2OH""",
)

entry(
    index = 3687,
    label = "CH3OH + CH2 <=> CH3 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.43, 'cm^3/(mol*s)'), n=3.1, Ea=(6935, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OH + CH2 <=> CH3 + CH3O""",
)

entry(
    index = 3688,
    label = "CH3OH + CH2 <=> CH3 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(31.92, 'cm^3/(mol*s)'), n=3.2, Ea=(7174, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OH + CH2 <=> CH3 + CH2OH""",
)

entry(
    index = 3692,
    label = "C2H + HCO <=> C2H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H + HCO <=> C2H2 + CO""",
)

entry(
    index = 3694,
    label = "C2H + CH4 <=> CH3 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.168e+10, 'cm^3/(mol*s)'),
        n = 0.94,
        Ea = (651.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H + CH4 <=> CH3 + C2H2""",
)

entry(
    index = 3695,
    label = "C2H + CH3OH <=> C2H2 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H + CH3OH <=> C2H2 + CH2OH""",
)

entry(
    index = 3696,
    label = "C2H + CH3OH <=> C2H2 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H + CH3OH <=> C2H2 + CH3O""",
)

entry(
    index = 3706,
    label = "C2H2 + O2 <=> C2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.204e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (74520, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H2 + O2 <=> C2H + HO2""",
)

entry(
    index = 3716,
    label = "C2H3 + O <=> OH + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03e+12, 'cm^3/(mol*s)'),
        n = 0.205,
        Ea = (-848.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H3 + O <=> OH + C2H2""",
)

entry(
    index = 3719,
    label = "C2H3 + HCO <=> C2H4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.033e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H3 + HCO <=> C2H4 + CO""",
)

entry(
    index = 3720,
    label = "C2H3 + CH2 <=> CH3 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H3 + CH2 <=> CH3 + C2H2""",
)

entry(
    index = 3722,
    label = "C2H + C2H3 <=> C2H2 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H + C2H3 <=> C2H2 + C2H2""",
)

entry(
    index = 3733,
    label = "C2H4 <=> C2H2 + H2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(88770, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.58e+51, 'cm^3/(mol*s)'),
            n = -9.31,
            Ea = (97800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7345,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2, 'CO': 3, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 <=> C2H2 + H2""",
)

entry(
    index = 3734,
    label = "C2H4 + O <=> CH2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (954700, 'cm^3/(mol*s)'),
        n = 2.121,
        Ea = (1233.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + O <=> CH2 + CH2O""",
)

entry(
    index = 3737,
    label = "C2H4 + O <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (127500, 'cm^3/(mol*s)'),
        n = 2.108,
        Ea = (449.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H4 + O <=> CH4 + CO""",
)

entry(
    index = 3739,
    label = "C2H4 + CH <=> C3H4-A + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+14, 'cm^3/(mol*s)'), n=-0.31, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H4 + CH <=> C3H4-A + H""",
)

entry(
    index = 3740,
    label = "C2H4 + CH2 <=> C3H5-A + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(5285, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H4 + CH2 <=> C3H5-A + H""",
)

entry(
    index = 3748,
    label = "C2H5 + O <=> CH3 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + O <=> CH3 + CH2O""",
)

entry(
    index = 3749,
    label = "C2H5 + O <=> OH + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + O <=> OH + C2H4""",
)

entry(
    index = 3750,
    label = "C2H5 + OH <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.409e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + OH <=> C2H4 + H2O""",
)

entry(
    index = 3751,
    label = "C2H5 + OH <=> CH3 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + OH <=> CH3 + CH2OH""",
)

entry(
    index = 3752,
    label = "C2H5 + HO2 <=> C2H4 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + HO2 <=> C2H4 + H2O2""",
)

entry(
    index = 3753,
    label = "C2H5 + CH <=> H + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + CH <=> H + C3H5-A""",
)

entry(
    index = 3754,
    label = "C2H5 + CH2 <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + CH2 <=> C2H4 + CH3""",
)

entry(
    index = 3756,
    label = "C2H5 + CH2OH <=> C2H4 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + CH2OH <=> C2H4 + CH3OH""",
)

entry(
    index = 3757,
    label = "C2H5 + CH2OH <=> C2H6 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + CH2OH <=> C2H6 + CH2O""",
)

entry(
    index = 3758,
    label = "C2H5 + CH3O <=> C2H6 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + CH3O <=> C2H6 + CH2O""",
)

entry(
    index = 3759,
    label = "C2H5 + C2H <=> C2H2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + C2H <=> C2H2 + C2H4""",
)

entry(
    index = 3760,
    label = "C2H5 + C2H3 <=> C3H5-A + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + C2H3 <=> C3H5-A + CH3""",
)

entry(
    index = 3766,
    label = "C2H6 + HCO <=> CH2O + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.72, Ea=(18235, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H6 + HCO <=> CH2O + C2H5""",
)

entry(
    index = 3767,
    label = "C2H6 + CH <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.185e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-262.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H6 + CH <=> C2H4 + CH3""",
)

entry(
    index = 3768,
    label = "C2H6 + CH2OH <=> CH3OH + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(199, 'cm^3/(mol*s)'), n=3, Ea=(13976, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H6 + CH2OH <=> CH3OH + C2H5""",
)

entry(
    index = 3769,
    label = "C2H6 + C2H <=> C2H2 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+11, 'cm^3/(mol*s)'),
        n = 0.54,
        Ea = (-358, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C2H6 + C2H <=> C2H2 + C2H5""",
)

entry(
    index = 3770,
    label = "C2H6 + C2H3 <=> C2H4 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(601, 'cm^3/(mol*s)'), n=3.3, Ea=(10502, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H6 + C2H3 <=> C2H4 + C2H5""",
)

entry(
    index = 3790,
    label = "C3H4-A + OH <=> CH2O + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-198.7, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H4-A + OH <=> CH2O + C2H3""",
)

entry(
    index = 3798,
    label = "C3H5-A + H <=> C3H6",
    degeneracy = 1,
    duplicate = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.33e+60, 'cm^6/(mol^2*s)'),
            n = -12,
            Ea = (5967.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.02,
        T3 = (1097, 'K'),
        T1 = (10967, 'K'),
        T2 = (6860, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-A + H <=> C3H6""",
)

entry(
    index = 3799,
    label = "C3H5-A + O => C2H4 + H + CO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-A + O => C2H4 + H + CO""",
)

entry(
    index = 3800,
    label = "C3H5-A + O2 => C2H2 + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (9.71e+20, 'cm^3/(mol*s)'),
        n = -2.7,
        Ea = (24980, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H5-A + O2 => C2H2 + CH2O + OH""",
)

entry(
    index = 3806,
    label = "C3H5-A + C2H3 <=> C3H6 + C2H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-A + C2H3 <=> C3H6 + C2H2""",
)

entry(
    index = 3808,
    label = "C3H5-S + H <=> C3H5-A + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + H <=> C3H5-A + H""",
)

entry(
    index = 3810,
    label = "C3H5-S + O <=> C2H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + O <=> C2H5 + CO""",
)

entry(
    index = 3811,
    label = "C3H5-S + OH <=> C3H4-P + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + OH <=> C3H4-P + H2O""",
)

entry(
    index = 3812,
    label = "C3H5-S + OH <=> C3H4-A + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H5-S + OH <=> C3H4-A + H2O""",
)

entry(
    index = 3825,
    label = "C3H6 + O <=> C2H4 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+06, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (-546, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is C3H6 + O <=> C2H4 + CH2O""",
)

entry(
    index = 3827,
    label = "C3H6 + CH2 <=> C3H5-A + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 + CH2 <=> C3H5-A + CH3""",
)

entry(
    index = 3828,
    label = "C3H6 + C2H <=> C2H2 + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(140, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C3H6 + C2H <=> C2H2 + C3H5-A""",
)

entry(
    index = 3898,
    label = "O3 <=> O2 + O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.37e+15, 's^-1'), n=-0.67, Ea=(25990, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.275e+28, 'cm^3/(mol*s)'),
            n = -4.37,
            Ea = (27297, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6417,
        T3 = (0.000391, 'K'),
        T1 = (8680.74, 'K'),
        T2 = (6060.75, 'K'),
        efficiencies = {'[O]': 6, 'N#N': 1.5, '[H][H]': 3, '[He]': 1.2, '[O][O]': 1.5, 'O=OO': 3.75, '[Ar]': 1},
    ),
    shortDesc = u"""The chemkin file reaction is O3 <=> O2 + O""",
)

entry(
    index = 3899,
    label = "O3 + O <=> O2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(4094, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O3 + O <=> O2 + O2""",
)

entry(
    index = 3900,
    label = "O3 + H <=> O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(934, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O3 + H <=> O2 + OH""",
)

entry(
    index = 3901,
    label = "O3 + H <=> O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O3 + H <=> O + HO2""",
)

entry(
    index = 3902,
    label = "O3 + OH <=> O2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.85e+11, 'cm^3/(mol*s)'), n=0, Ea=(831, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O3 + OH <=> O2 + HO2""",
)

entry(
    index = 3903,
    label = "O3 + H2O <=> O2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(66.2, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O3 + H2O <=> O2 + H2O2""",
)

entry(
    index = 3904,
    label = "O3 + HO2 <=> OH + O2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.62e+09, 'cm^3/(mol*s)'), n=0, Ea=(994, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O3 + HO2 <=> OH + O2 + O2""",
)

entry(
    index = 3905,
    label = "O3 + CO <=> O2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(602, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O3 + CO <=> O2 + CO2""",
)

entry(
    index = 3906,
    label = "O3 + HCO <=> O2 + H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O3 + HCO <=> O2 + H + CO2""",
)

entry(
    index = 3907,
    label = "O3 + CH3 <=> CH3O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.83e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is O3 + CH3 <=> CH3O + O2""",
)

entry(
    index = 3908,
    label = "N + N <=> N2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.53e+14, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-218.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[N]': 3, '[O]': 3, 'O=C=O': 3.5, 'N#N': 0, '[Ar]': 0.5},
    ),
    shortDesc = u"""The chemkin file reaction is N + N <=> N2""",
)

entry(
    index = 3909,
    label = "N + N + N2 <=> N2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+14, 'cm^6/(mol^2*s)'),
        n = 0,
        Ea = (-251.61, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is N + N + N2 <=> N2 + N2""",
)

entry(
    index = 3910,
    label = "N + O <=> NO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.96e+19, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[O][O]': 0, 'O=C=O': 2.9, 'N#N': 0, '[Ar]': 0.05},
    ),
    shortDesc = u"""The chemkin file reaction is N + O <=> NO""",
)

entry(
    index = 3911,
    label = "N + O + N2 <=> NO + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.28e+16, 'cm^6/(mol^2*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is N + O + N2 <=> NO + N2""",
)

entry(
    index = 3912,
    label = "N + O + O2 <=> NO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.28e+16, 'cm^6/(mol^2*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is N + O + O2 <=> NO + O2""",
)

entry(
    index = 3913,
    label = "N + HO2 <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1987.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is N + HO2 <=> NO + OH""",
)

entry(
    index = 3914,
    label = "N + NO <=> N2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.27e+12, 'cm^3/(mol*s)'), n=0.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is N + NO <=> N2 + O""",
)

entry(
    index = 3915,
    label = "N + O2 <=> NO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.4e+09, 'cm^3/(mol*s)'), n=1, Ea=(6280, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is N + O2 <=> NO + O""",
)

entry(
    index = 3916,
    label = "N + OH <=> NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is N + OH <=> NO + H""",
)

entry(
    index = 3917,
    label = "NO + C <=> CO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NO + C <=> CO + N""",
)

entry(
    index = 3918,
    label = "N + O3 <=> NO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+07, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is N + O3 <=> NO + O2""",
)

entry(
    index = 3919,
    label = "NO + O <=> NO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+15, 'cm^3/(mol*s)'), n=-0.75, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.72e+24, 'cm^6/(mol^2*s)'),
            n = -2.87,
            Ea = (1550, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.957,
        T3 = (1e-90, 'K'),
        T1 = (8332, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12, '[Ar]': 0},
    ),
    shortDesc = u"""The chemkin file reaction is NO + O <=> NO2""",
)

entry(
    index = 3920,
    label = "NO2 + O <=> O2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.05e+14, 'cm^3/(mol*s)'), n=-0.52, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NO2 + O <=> O2 + NO""",
)

entry(
    index = 3921,
    label = "NO2 + H <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.32e+14, 'cm^3/(mol*s)'), n=0, Ea=(362, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NO2 + H <=> NO + OH""",
)

entry(
    index = 3922,
    label = "HO2 + NO <=> NO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+12, 'cm^3/(mol*s)'), n=0, Ea=(-497, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HO2 + NO <=> NO2 + OH""",
)

entry(
    index = 3923,
    label = "NO2 + NO2 <=> NO + NO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.63e+12, 'cm^3/(mol*s)'), n=0, Ea=(26100, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NO2 + NO2 <=> NO + NO + O2""",
)

entry(
    index = 3924,
    label = "CO + NO2 <=> CO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(33800, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CO + NO2 <=> CO2 + NO""",
)

entry(
    index = 3925,
    label = "HCO + NO2 <=> H + CO2 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.39e+15, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (1930, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is HCO + NO2 <=> H + CO2 + NO""",
)

entry(
    index = 3926,
    label = "NO2 + CH3 <=> NO + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+15, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NO2 + CH3 <=> NO + CH3O""",
)

entry(
    index = 3945,
    label = "NO + OH <=> HONO",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (1.99e+12, 'cm^3/(mol*s)'),
            n = -0.05,
            Ea = (-721, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.08e+23, 'cm^6/(mol^2*s)'),
            n = -2.51,
            Ea = (-67.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[Ar]': 0.75},
    ),
    shortDesc = u"""The chemkin file reaction is NO + OH <=> HONO""",
)

entry(
    index = 3947,
    label = "HONO + O <=> OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(5960, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HONO + O <=> OH + NO2""",
)

entry(
    index = 3948,
    label = "HONO + OH <=> H2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-520, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HONO + OH <=> H2O + NO2""",
)

entry(
    index = 3949,
    label = "HCO + NO2 <=> CO + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.24e+23, 'cm^3/(mol*s)'),
        n = -3.29,
        Ea = (2350, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is HCO + NO2 <=> CO + HONO""",
)

entry(
    index = 3950,
    label = "NO2 + H2 <=> HONO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.33e+11, 'cm^3/(mol*s)'), n=0, Ea=(28800, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NO2 + H2 <=> HONO + H""",
)

entry(
    index = 3951,
    label = "HONO + H <=> H2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.1e+06, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (3845.24, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is HONO + H <=> H2O + NO""",
)

entry(
    index = 3953,
    label = "HONO + HONO <=> NO + NO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.349, 'cm^3/(mol*s)'),
        n = 3.64,
        Ea = (12139.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""The chemkin file reaction is HONO + HONO <=> NO + NO2 + H2O""",
)

entry(
    index = 3967,
    label = "NO + CH <=> N + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NO + CH <=> N + HCO""",
)

entry(
    index = 4069,
    label = "CH3O + NO2 <=> CH2O + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(2285, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + NO2 <=> CH2O + HONO""",
)

entry(
    index = 4092,
    label = "NO2 + HO2 <=> HONO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.446e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NO2 + HO2 <=> HONO + O2""",
)

entry(
    index = 4093,
    label = "NO2 + HCO <=> CO + NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.45e+12, 'cm^3/(mol*s)'), n=0, Ea=(-430, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is NO2 + HCO <=> CO + NO + OH""",
)

entry(
    index = 4094,
    label = "CH2O + NO2 <=> HCO + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(800, 'cm^3/(mol*s)'), n=2.77, Ea=(13730, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH2O + NO2 <=> HCO + HONO""",
)

entry(
    index = 4095,
    label = "CH3OCH3 + NO2 <=> CH3OCH2 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(17600, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3OCH3 + NO2 <=> CH3OCH2 + HONO""",
)

entry(
    index = 4097,
    label = "HONO + CH3 <=> NO2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.14e+17, 'cm^3/(mol*s)'), n=0, Ea=(19975, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is HONO + CH3 <=> NO2 + CH4""",
)

entry(
    index = 4100,
    label = "C2H5 + HONO <=> C2H6 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.87, Ea=(5504, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H5 + HONO <=> C2H6 + NO2""",
)

entry(
    index = 4101,
    label = "C2H3 + HONO <=> C2H4 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.87, Ea=(5504, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is C2H3 + HONO <=> C2H4 + NO2""",
)

entry(
    index = 4102,
    label = "CH3O + HONO <=> CH3OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.87, Ea=(5504, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""The chemkin file reaction is CH3O + HONO <=> CH3OH + NO2""",
)

