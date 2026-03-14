
import pandas as pd
import re

def load_waveform(file_path):
    with open(file_path,'r',errors='ignore') as f:
        lines=f.readlines()

    data=[]
    for line in lines:
        parts=re.split(r'\s+',line.strip())
        nums=[]
        for p in parts:
            try:
                nums.append(float(p))
            except:
                pass
        if len(nums)>=2:
            for i in range(0,len(nums)-1,2):
                data.append((nums[i],nums[i+1]))

    return pd.DataFrame(data,columns=["time","amplitude"])
