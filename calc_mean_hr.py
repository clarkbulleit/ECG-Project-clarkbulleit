
class Error(Exception):
    """Base class for other exceptions"""
    pass


class NoBeatsDetected(Error):
    """Raised when no peaks have been detected"""
    pass


def calc_mean_hr(num_beats, duration):
    """
    :param num_beats: Int of number of detected beats
    :param duration: Float of duration of ECG strip
    :return: Mean hr in beats per minute as int, rounds the
    float to nearest integer
    Raises an error if the num_beats input = 0
    Raises TypeError if non-numeric
    """

    if num_beats == 0:
        raise NoBeatsDetected

    mean_hr_bpm = round((num_beats/duration)*60)

    return mean_hr_bpm
