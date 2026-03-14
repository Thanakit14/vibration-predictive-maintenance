
import numpy as np
import pandas as pd

def extract_features(signal):

    rms=np.sqrt(np.mean(signal**2))
    peak=np.max(abs(signal))
    p2p=np.max(signal)-np.min(signal)

    kurtosis=pd.Series(signal).kurtosis()
    skewness=pd.Series(signal).skew()

    crest=peak/rms if rms!=0 else 0

    return {
        "RMS":rms,
        "Peak":peak,
        "Peak_to_Peak":p2p,
        "Kurtosis":kurtosis,
        "Skewness":skewness,
        "Crest_Factor":crest
    }
