import numpy as np

flow = np.array([-100,72.6,72.6,-33])
IRR = np.irr(flow)
print(IRR)