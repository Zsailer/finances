import pandas as pd
import numpy as np

federal_tax_brackets = pd.DataFrame({
    'rate': [0, 0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
    'single': [0, 9700, 39475, 84200, 160726, 204101, 510300, np.inf],
    'married-jointly': [0, 19400, 78950, 168400, 321450, 408200, 612350, np.inf],
    'head-of-household': [0, 13850, 52850, 84200, 160700, 204100, 510300, np.inf]
})

federal_standard_deduction = pd.DataFrame({
    'head-of-household': [18000],
    'married-jointly': [24000],
    'single': [12000]
})


state_tax_brackets = pd.DataFrame({
    'rate': [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123],
    'single': [8544, 20255, 31969, 44377, 56085, 286492, 343788, 572980, np.inf],
    'married-jointly': [8544*2, 20255*2, 31969*2, 44377*2, 56085*2, 286492*2, 343788*2, 572980*2, np.inf],
    'head-of-household': [8544*2, 20255*2, 31969*2, 44377*2, 56085*2, 286492*2, 343788*2, 572980*2, np.inf]
})