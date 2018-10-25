

def create_dict(mean_hr_bpm, voltage_extremes, duration, num_beats,
                beats):
    """ Creates dictionary from 5 inputs with specified keys

    :param mean_hr_bpm: integer for mean heart rate
    :param voltage_extremes: tuple for min and max voltages
    :param duration: duration of ECG time strip
    :param num_beats: integer of number of beats
    :param beats: numpy list of time locations of peaks
    :return: the complied dictionary of all the terms
    under the correct keys
    """
    metrics = {}
    metrics["mean_hr_bpm"] = mean_hr_bpm
    metrics["voltage_extremes"] = voltage_extremes
    metrics["duration"] = duration
    metrics["num_beats"] = num_beats
    metrics["beats"] = beats

    return metrics
