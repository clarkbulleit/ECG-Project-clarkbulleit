
class Error(Exception):
    """Base class for other exceptions"""
    pass


class NoBeatsDetected(Error):
    """Raised when no peaks have been detected"""
    pass


def calc_mean_hr(num_beats, duration, beats=[1, 2, 3], user_average=1):
    """
    :param num_beats: Int of number of detected beats
    :param duration: Float of duration of ECG strip
    :return: Mean hr in beats per minute as int, rounds the
    float to nearest integer
    Raises an error if the num_beats input = 0
    Raises TypeError if non-numeric
    """
    import logging
    logging.basicConfig(filename="Main_Log.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    new_num_beats = 0

    if num_beats == 0:
        raise NoBeatsDetected

    if duration <= user_average*60:
        mean_hr_bpm = round((num_beats/duration)*60)

    else:
        for x in beats:
            if x < user_average*60:
                new_num_beats = new_num_beats + 1
        mean_hr_bpm = round((new_num_beats/user_average))

    if mean_hr_bpm < 30:
        logging.warning("Warning: The heart rate is below normal range")

    elif mean_hr_bpm > 200:
        logging.warning("Warning: The hear rate exceeds normal values")

    return mean_hr_bpm
