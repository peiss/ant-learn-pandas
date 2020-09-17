import pandas as pd
import os

dfs = []

# read all excel 's sheet append to dfs
for fname in os.listdir("./"):
    if fname.endswith(".xls") and fname != "final.xls":
        df = pd.read_excel(
            fname,
            header=None,
            sheet_name=None
        )
        dfs.extend(df.values())

# concat
result = pd.concat(dfs)

# output excel
result.to_excel("./final.xls", index=False)