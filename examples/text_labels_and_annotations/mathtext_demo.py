"""
Demo using fontdict to control style of text and labels.
"""
import numpy as np
import matplotlib as mpl
import matplotlib.mathtext as mathtext
import matplotlib.pyplot as plt

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 14,
        }

x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

tex = r'${\displaystyle \frac{1}{2}} {\frac{3}{2}} ' + \
         r'{\scriptscriptstyle \frac{4}{5}} \cos(2 \pi t)' + \
         r'{\scriptstyle e^{{\textstyle x}x}}$'

plt.close('all')
plt.plot(x, y, 'k')
plt.title('Damped exponential decay', fontdict=font)
plt.text(1.5, 0.65, r"Mathtex: " + tex, fontdict=font)
plt.text(1.5, 0.35, r"\LaTeX: " + tex, fontdict=font, usetex=True)
plt.xlabel('time (s)', fontdict=font)
plt.ylabel('voltage (mV)', fontdict=font)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
