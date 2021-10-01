# %% codecell
from julia.api import Julia
jl = Julia(compiled_modules=False)
# %% codecell
%load_ext julia.magic
# %% codecell
%%julia
println("Test")
# %% codecell
%load_ext rpy2.ipython
# %% codecell
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'cups_of_coffee': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'productivity': [2, 5, 6, 8, 9, 8, 0, 1, 0, -1]
})
df.transpose()
# %% codecell
%%R -i df
library(ggplot2)
ggplot(df, aes(x=reorder(cups_of_coffee,productivity), y=productivity)) + geom_col() + coord_flip()
# %% codecell

# %% codecell

# %% codecell

# %% codecell
