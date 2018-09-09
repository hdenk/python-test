import numpy as np
import matplotlib.pyplot as plt
import random

# Berechnung von Wahrscheinlichkeiten der Normal-Verteilung durch Mittelwert-
# Bildung via Wuerfel
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html

anzahlWuerfe = 60
anzahlVersuche = 1000
mu = 3.5  # Mittelwert des Wuerfelns
sigmaW = 1.7078  # Standardabweichung des Wuerfelns
sigma = sigmaW / anzahlWuerfe**(1/2)  # Der Standardfehler des arithm. Mittels

verteilung = [0] * anzahlVersuche

for v in range(0, anzahlVersuche):
    augenSumme = 0

    for w in range(0, anzahlWuerfe):
        augenZahl = random.randint(1, 6)
        augenSumme += augenZahl

    mittelWert = augenSumme / anzahlWuerfe
    verteilung[v] = mittelWert

num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(verteilung, num_bins, density=1)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Mittelwerte')
ax.set_ylabel('Haeufigkeiten')
ax.set_title("Verteilung")

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
