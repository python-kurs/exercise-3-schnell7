# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script
#%%
def count_type(lines):
    res = []
    for i in set(lines):
        c = 0
        for k in lines:
            if i == k:
                c=c+1
        res.append(c)
    return(res)
#%%