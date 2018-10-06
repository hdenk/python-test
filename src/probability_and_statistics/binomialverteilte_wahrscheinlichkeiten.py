import matplotlib.pyplot as plt
import math

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

fig = plt.figure(figsize=(10,8))

# Dichtefunktion
ax_Dichte = fig.add_subplot(211)
ax_Dichte.plot(x_Koordinaten, y_DichteFkt)
#ax_Dichte.axis([1, maxIdx, 0, 0.2])
ax_Dichte.set_title("Dichtefunktion (p=" + "{:1.4f}".format(p) 
          + " ew=" + "{:1.4f}".format(erwartungsWert) + ")", loc="left")

# Verteilungsfunktion
ax_Verteilung = fig.add_subplot(212)
ax_Verteilung.plot(x_Koordinaten, y_VerteilungsFkt)
#ax_Verteilung.axis([1, maxIdx, 0, 1])
ax_Verteilung.set_title("Verteilungsfunktion (iw=" + "{:1.4f}".format(integralWert)
          + ")", loc="left")

plt.show()
