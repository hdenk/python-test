import matplotlib.pyplot as plt
import math

# Berechnung von Wahrscheinlichkeiten der binomialen Verteilung also
# zB. n mal Wuerfeln und zaehlen, wie oft Gerade Augenzahl o. eine Sechs kommt.

p = 1.0 / 2.0
q = 1.0 - p
maxIdx = 32

x_Koordinaten = range(0, maxIdx)
y_DichteFkt = [0] * maxIdx
y_VerteilungsFkt = [0] * maxIdx
erwartungsWert = 0
integralWert = 0


def nOverM(n, m):
    return math.factorial(n) / (math.factorial(m) * math.factorial(n - m))


for i, x in enumerate(x_Koordinaten):
    y = nOverM(maxIdx, x) * (p**x) * (q**(maxIdx-x))
    y_DichteFkt[i] = y
    erwartungsWert = erwartungsWert + (x * y)
    integralWert = integralWert + y
    y_VerteilungsFkt[i] = integralWert

plt.figure(1)

# Dichtefunktion
plt.subplot(211)
plt.plot(x_Koordinaten, y_DichteFkt)
# plt.axis([1, maxIdx, 0, 0.2])
plt.title("Dichtefunktion (p=" + "{:1.4f}".format(p) +
          " ew=" + "{:1.4f}".format(erwartungsWert) + ")", loc="left")

# Verteilungsfunktion
plt.subplot(212)
plt.title("Verteilungsfunktion (iw=" + "{:1.4f}".format(integralWert)
          + ")", loc="left")
# plt.axis([1, maxIdx, 0, 1])
plt.plot(x_Koordinaten, y_VerteilungsFkt)

plt.show()
