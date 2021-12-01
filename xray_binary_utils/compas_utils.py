import h5py
import os
import glob
import shutil
import matplotlib.pyplot as plt
import plotly.express as px


def run_compas(n_systems: int = 100):
    os.system(f'COMPAS -n {n_systems} --detailed-output --evolve-unbound-systems')
    
def remove_output():
    for f in glob.glob("COMPAS_Output*"):
        shutil.rmtree(f)

def open_output() -> h5py.File:
    return h5py.File('COMPAS_Output/COMPAS_Output.h5', 'r')

def open_detailed_output(n: int = 0) -> h5py.File:
    return h5py.File(f'COMPAS_Output/Detailed_Output/BSE_Detailed_Output_{n}.h5', 'r')
