import math
import sys
import pycuda.autoinit
import pycuda.driver as drv
import numpy as np
from pycuda.compiler import SourceModule

def first_fit(items,cap):
    """
    Funkcija racuna koliko je spremnika odredenog kapaciteta potrebno za smjestanje odredenih elemenata koristeci First Fit algoritam.

    Argumenti:
    items -- elementi koje je potrebno smjestiti u spremnike
    cap -- kapacitet spremnika

    Vraca:
    Broj spremnika koji je potreban za spremanje elemenata.
    """
    length = len(items)
    bins = np.zeros(2 * length, dtype=np.float32)
    for x in range(0, len(items)):
        bins[0 * length + x] = cap

    mod = SourceModule(open("firstFitAlgorithm.cu").read())
    binPacking = mod.get_function("binPacking")
    binPacking(drv.InOut(bins), drv.In(items), np.float32(cap), np.int32(length), block=(16,1,1), grid=(1,1))

    used = 0
    for x in range(0, len(items)):
        if bins[x] != cap:
            used+=1
    return used
