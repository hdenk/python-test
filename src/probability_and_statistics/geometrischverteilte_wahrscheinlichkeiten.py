import matplotlib.pyplot as plt

# p/q Wahrscheinlichkeit fuer Treffer/Niete
p = 1.0 / 6.0 
q = 1.0 - p 

# Anzahl der berechneten Wahrscheinlichkeiten (x_Koordinate Maximum)
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

fig = plt.figure(figsize=(10,8))

# Dichtefunktion
ax_Dichte = fig.add_subplot(211)
ax_Dichte.plot(x_Koordinaten, y_DichteFkt)
# ax_Dichte.axis([1, maxIdx, 0, 0.2])
ax_Dichte.set_title("Dichtefunktion (p=" + "{:1.4f}".format(p) +
          " ew=" + "{:1.4f}".format(erwartungsWert) + ")", loc="left")

# Verteilungsfunktion
ax_Verteilung = fig.add_subplot(212)
ax_Verteilung.plot(x_Koordinaten, y_VerteilungsFkt)
# ax_Verteilung.axis([1, maxIdx, 0, 1])
ax_Verteilung.set_title("Verteilungsfunktion (iw=" + "{:1.4f}".format(integralWert)
          + ")", loc="left")

plt.show()
