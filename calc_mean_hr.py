

def calc_mean_hr(num_beats, duration, beats=[1, 2, 3], user_average=1):
    """ Calculates mean heart rate based on user input

    If the user input window is less than the time duration
    of the strip, the time duration is used for the calculation.
    If it is larger, the function finds the number of beats within
    the specified window, and uses it to find the mean HR

    Args:
        :param num_beats: Int of number of detected beats
        :param duration: Float of duration of ECG strip
        :param beats: Numpy array time locations of peaks
        :param user_average: Int for user input for time window in
        minutes

    Return:
        mean_hr_bpm: Mean hr in beats per minute as int,
        rounds the float to nearest integer

    Raises:
        TypeError: If input num_beats or duration are non-
        numeric

    """
    new_num_beats = 0

    if duration <= user_average*60:
        mean_hr_bpm = round((num_beats/duration)*60)

    else:
        for x in beats:
            if x < user_average*60:
                new_num_beats = new_num_beats + 1
        mean_hr_bpm = round((new_num_beats/user_average))

    return mean_hr_bpm
