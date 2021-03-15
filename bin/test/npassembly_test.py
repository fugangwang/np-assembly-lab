import testbook
import os
from datetime import datetime

DEFAULT_NPCHARGE = -1000
DEFAULT_LIGAND = 50
DEFAULT_SALT = 0.175

@testbook.testbook('npassemblylab-frontend.ipynb', execute=True)
def test_runPreprocessor(tb):
    t0 = datetime.now()
    func = tb.ref("runPreprocessor")
    func(DEFAULT_NPCHARGE, DEFAULT_LIGAND, DEFAULT_SALT)
    logf = "preprocessor.log"
    lammpsf = "in.lammps"
    assert os.path.exists(logf) == 1
    assert os.path.exists(lammpsf) == 1
    t1 = os.path.getmtime("logf")
    t2 = os.path.getmtime(lammpsf)
    assert (t1>t0 and t2>t0)
    os.remove(logf)
    os.remove(lammpsf)
