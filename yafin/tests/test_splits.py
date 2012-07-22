from unittest import TestCase
import os.path

import yafin.cactions as cact

def curpath():
    pth, _ = os.path.split(os.path.abspath(__file__))
    return pth

class TestYahooSplits(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)

    def runTest(self):
        pass

    def setUp(self):
        pass

    def splits_error(self, bad):
        try:
            cact.get_splits(bad)
        except cact.SymbolNotFound as err:
            assert err.symbol == bad
        except:
            assert False, "Raised wrong error. Should be SymbolNotFound"
        else:
            assert False, "Error should have been raised"

    def test_splits_error(self):
        """
            Make sure to handle errors properly
        """
        self.splits_error('BCME')
        self.splits_error('TC+T')
        self.splits_error('ASDFSD@!#')

if __name__ == '__main__':                                                                                          
    import nose                                                                      
    nose.runmodule(argv=[__file__,'-vvs','-x','--pdb', '--pdb-failure'],exit=False)   
