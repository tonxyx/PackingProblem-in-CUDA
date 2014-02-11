import numpy as np
import firstFitAlgorithm

items = np.loadtxt("elementi.txt", dtype=np.float32)
cap = 5

result_gpu = firstFitAlgorithm.first_fit(items, cap)

print "First-fit algoritam za elemente ", items, "sa kapacitetom spremnika", cap, "koristio je", result_gpu, "spremika."
