
def test_peak_detect():
    """
    Creates delta train of peaks at every half
    second in a 10 second time list
    :return: checks that the peak_detect function
    returns the correct peak locations in a list
    """
    from peak_detect import peak_detect
    import numpy as np

    delta_train = {}
    delta_train["time"] = [x*0.5 for x in range(0, 2*10+1)]
    delta_train["voltage"] = [1 if x % 2 else 0 for x in range(0, 21)]

    locs_peaks = peak_detect(delta_train)

    assert np.all(locs_peaks == np.array([.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]))
