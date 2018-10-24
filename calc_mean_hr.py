
def calc_mean_hr(num_beats, duration):
    """
    :param num_beats: int
    :param duration: float
    :return: mean hr in beats per minute as int
    """

    mean_hr_bpm = round((num_beats/duration)*60)

    return mean_hr_bpm
