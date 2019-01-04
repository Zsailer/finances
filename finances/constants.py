import pandas as pd

brackets = pd.DataFrame({
    'rate': [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
    'single': [0, 9525, 38700, 82500, 157500, 200000, 500000],
    'married-jointly': [0, 19050, 77400, 165000, 315000, 400000, 600000],
    'head-of-household': [0, 13600, 51800, 82500, 157500, 200000, 500000]
})

standard_deduction = pd.DataFrame({
    'head-of-household': [18000],
    'married-jointly': [24000],
    'single': [12000]
})
