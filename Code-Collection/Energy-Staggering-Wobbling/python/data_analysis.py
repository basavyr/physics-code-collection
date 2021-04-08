#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as plt
import finder
import importer
import plotter
import staggering

isotopes = {
    'Pd': [112, 114],
    'Ru': [108, 110, 112]}


path = './plots/'

# generate naming for the data files used for importing spins and energies
data_file = lambda mass, isotope: f'{mass}{isotope}.dat'

# generate the files for staggering plots
plot_file = lambda mass, isotope: f'Stagger-{mass}{isotope}.pdf'


def Data_Analysis(Isotope, Mass):
    A = list(isotopes[Isotope])
    a = [x for x in A if x == Mass]
    if(len(a) == 0):
        print(
            f'The isotope A={Mass}|{Isotope} does not have an experimental data set within the current database')
        return -1
    INPUT_FILE = data_file(Mass, Isotope)
    PLOT_FILE = plot_file(Mass, Isotope)

    EXPERIMENTAL_DATA = importer.Import_Data(INPUT_FILE)

    DATA_SIZE = len(EXPERIMENTAL_DATA)
    print(f'{DATA_SIZE} bands were imported into the stack')

    STAGGER_DATA = []

    for id in range(0, DATA_SIZE, 2):
        odd_band = EXPERIMENTAL_DATA[id]
        even_band = EXPERIMENTAL_DATA[id + 1]
        current_stagger = staggering.Compute_Stagger(even_band, odd_band)
        STAGGER_DATA.append(current_stagger)
    # print(STAGGER_DATA)
    plotter.Plot_Stagger_Bands(STAGGER_DATA, path + PLOT_FILE,str(Mass)+str(Isotope))


Data_Analysis('Ru', 108)
