import sys
import numpy as np
import firstFitAlgorithm

def test_first_fit():
    """
    Funkcija testira da li se jednaki rezultati dobe serijskom i paralelnom izvedbom First Fit algoritma.

    Argumenti:
    /

    Vraca:
    Ukoliko je test uspjesan, potvrdu da je test uspjesan.
    """
    items = np.array([2.0, 4.0, 3.0, 4.0, 2.0, 5.0, 1.0, 4.0], np.float32)
    cap = 5.0

    bins = np.zeros((2, len(items)), dtype=np.float32)
    for x in range(0, len(items)):
        bins[0][x] = cap
    y = 0
    for item in items:
        x=0
        if item > cap:
            print "Element ", item, "je veci od kapaciteta spremnika koji je ", cap,". PREKID!"
            sys.exit()
        if bins[0][x] >= item:
            bins[1][x] += item
            bins[0][x] -= item
        else:
            while bins[0][x] < item:
                  x+=1
            bins[1][x] += item
            bins[0][x] -= item
        if x > y:
            y = x
    result_cpu = y + 1
    assert (firstFitAlgorithm.first_fit(items, cap) == result_cpu)
    print "Test uspjesno prolazi."

if __name__ == "__main__":
    test_first_fit()
