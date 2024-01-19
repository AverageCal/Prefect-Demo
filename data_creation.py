import numpy as np
import pandas as pd

pk_id = [n for n in range(30,40)]
alpha = ['t','l','o','q','m','n','q','v','s','w']
decimals = [round(np.random.normal(n),2) for n in range(10)]
large_ints = [n for n in range(23000,33000,1000)]

data2 = pd.DataFrame(
    {
        'id':pk_id,
        'letters':alpha,
        'floats':decimals,
        'ints':large_ints
    }
)

data2.to_csv('third_data.csv',index=False)
