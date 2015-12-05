import unittest

from rmgpy.chemkin import loadChemkinFile

class ConcentrationPrinter:
    def __init__(self):
        self.species_names = []
        self.data = []

    def update(self, subject):
        self.data.append((subject.t , subject.coreSpeciesConcentrations))


def loadRMGPyJob(inputFile, chemkinFile, speciesDict):
    """
    Load the results of an RMG-Py job generated from the given `inputFile`.
    """
    import os.path
    from rmgpy.chemkin import getSpeciesIdentifier, loadChemkinFile
    from rmgpy.rmg.main import RMG
    from rmgpy.solver.base import TerminationTime, TerminationConversion

    # Load the specified RMG input file
    rmg = RMG()
    rmg.loadInput(inputFile)
    rmg.outputDirectory = os.path.abspath(os.path.dirname(inputFile))
    
    # Load the final Chemkin model generated by RMG
    speciesList, reactionList = loadChemkinFile(chemkinFile, speciesDict, readComments=False)

    # Map species in input file to corresponding species in Chemkin file
    speciesDict = {}


    #label of initial species must correspond to the label in the chemkin file WITHOUT parentheses.
    for spec0 in rmg.initialSpecies:
        for species in speciesList:
            if species.label == spec0.label:
                speciesDict[spec0] = species
                break
            
    # Replace species in input file with those in Chemkin file
    for reactionSystem in rmg.reactionSystems:
        reactionSystem.initialMoleFractions = dict([(speciesDict[spec], frac) for spec, frac in reactionSystem.initialMoleFractions.iteritems()])
        for t in reactionSystem.termination:
            if isinstance(t, TerminationConversion):
                t.species = speciesDict[t.species]
    
    # Set reaction model to match model loaded from Chemkin file
    rmg.reactionModel.core.species = speciesList
    rmg.reactionModel.core.reactions = reactionList

    return rmg


class ListenerTest(unittest.TestCase):

    def setUp(self):
        self.listener = ConcentrationPrinter()

        working_dir = 'rmgpy/solver/files/listener/'
        self.inputFile = working_dir + 'input.py'
        self.chemkinFile = working_dir + 'chemkin/chem.inp'
        self.spc_dict = working_dir + 'chemkin/species_dictionary.txt'


    def test_attach_detach(self):
        #create observable
        rmg = loadRMGPyJob(self.inputFile, self.chemkinFile, self.spc_dict)

        reactionSystem = rmg.reactionSystems[0]
        reactionSystem.attach(self.listener)

        self.assertNotEqual(reactionSystem._observers, [])
        
        reactionSystem.detach(self.listener)    

        self.assertEquals(reactionSystem._observers, [])

    def test_listen(self):
        #create observable
        rmg = loadRMGPyJob(self.inputFile, self.chemkinFile, self.spc_dict)

        reactionSystem = rmg.reactionSystems[0]
        reactionSystem.attach(self.listener)

        reactionModel = rmg.reactionModel

        self.assertEqual(self.listener.data, [])

        # run simulation:
        terminated, obj = reactionSystem.simulate(
            coreSpecies = reactionModel.core.species,
            coreReactions = reactionModel.core.reactions,
            edgeSpecies = reactionModel.edge.species,
            edgeReactions = reactionModel.edge.reactions,
            toleranceKeepInEdge = 0,
            toleranceMoveToCore = 1,
            toleranceInterruptSimulation = 1,
        ) 

        self.assertNotEqual(self.listener.data, [])

class ReactionSystemTest(unittest.TestCase):

    def setUp(self):
        
        working_dir = 'rmgpy/solver/files/listener/'
        self.inputFile = working_dir + 'input.py'
        self.chemkinFile = working_dir + 'chemkin/chem.inp'
        self.spc_dict = working_dir + 'chemkin/species_dictionary.txt'
        self.rmg = loadRMGPyJob(self.inputFile, self.chemkinFile, self.spc_dict)
        self.rxnSys = self.rmg.reactionSystems[0]

    def test_pickle(self):
        import pickle
        rxnSys = pickle.loads(pickle.dumps(self.rxnSys))
        
if __name__ == '__main__':
    unittest.main()