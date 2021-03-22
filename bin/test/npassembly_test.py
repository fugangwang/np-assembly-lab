import testbook
import os
from datetime import datetime
import subprocess

DEFAULT_NPCHARGE = -1000
DEFAULT_LIGAND = 50
DEFAULT_SALT = 0.175

@testbook.testbook('npassemblylab-frontend.ipynb', execute=True)
def test_runPreprocessor(tb):
    t0 = datetime.now()
    func = tb.ref("runPreprocessor")
    func(DEFAULT_NPCHARGE, DEFAULT_LIGAND, DEFAULT_SALT)
    logf = "./preprocessor.log"
    lammpsf = "./in.lammps"
    assert os.path.exists(logf) == 1
    assert os.path.exists(lammpsf) == 1
    t1 = datetime.fromtimestamp(os.path.getmtime(logf))
    t2 = datetime.fromtimestamp(os.path.getmtime(lammpsf))
    assert (t1>t0 and t2>t0)
    os.remove(logf)
    os.remove(lammpsf)

def test_backend():
    subprocess.getstatusoutput("make run-preprocessor")
    retcode, retstr = subprocess.getstatusoutput("make run-local-serial")
    assert (retcode == 0)
    #mk1 = "Total # of neighbors"
    #mk2 = "Ave neighs/atom"
    #assert ((mk1 in runret) and (mk2 in runret))
