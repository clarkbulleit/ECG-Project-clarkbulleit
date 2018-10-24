
def peak_detect(data, perh=.5, perl=0.015):
    """
    Detects peaks of ECG signals
    :param data: dictionary with lists under keys
    "time" and "voltage"
    :param perh: percentage of max height used for threshold, float
    :param perl: percentage of length used for min distance,float
    :return: list of the time locations of the detected peaks

    """
    import peakutils
    import numpy as np
    # import matplotlib.pyplot as plt

    v = data["voltage"]
    t = data["time"]
    cb = np.array(v)
    thres = perh*max(cb)
    min_dist = perl*len(t)

    inds = peakutils.indexes(cb, thres, min_dist)
    locs_peaks = []
    height_peaks = []

    for x in inds:
        locs_peaks.append(t[x])
        height_peaks.append(v[x])

    # plt.plot(t, v, locs_peaks, height_peaks, 'ro')
    # plt.show()
    return locs_peaks
