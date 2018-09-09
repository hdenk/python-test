import matplotlib.pyplot as plt

# Berechnung von Wahrscheinlichkeiten der geometrischen Verteilung also
# zB. so lange Wuerfeln bis eine Sechs kommt, dabei Anzahl der Wuerfe zaehlen

p = 1.0 / 6.0
q = 1.0 - p
maxIdx = 256

x_Koordinaten = range(1, maxIdx+1)
y_DichteFkt = [0] * maxIdx
y_VerteilungsFkt = [0] * maxIdx
erwartungsWert = 0
integralWert = 0

for i, x in enumerate(x_Koordinaten):
    y = p * (q**(x-1))
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
