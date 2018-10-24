
def create_dict(mean_hr_bpm, voltage_extremes, duration, num_beats, beats):
    metrics = {}
    metrics["mean_hr_bpm"] = mean_hr_bpm
    metrics["voltage_extremes"] = voltage_extremes
    metrics["duration"] = duration
    metrics["num_beats"] = num_beats
    metrics["beats"] = beats

    return metrics