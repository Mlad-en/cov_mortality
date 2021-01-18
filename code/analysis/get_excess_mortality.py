import pandas as pd


def calc_bg_excess_mortality(file: str, week_start: int = 1, week_end: int = 100) -> str:
    '''
    :param file: Provide file path to file that will be read. Ensure file has Weeks listed out in numeric format (1,2,3...).

    File should contain the following columns: Week (int), excess_death (numeric: int/float)
    :param week_start: Optional Param - Provide a start week for calculation. If not provided it will be assumed 1.
    :param week_end: Optional Param - Provide an end week for calculation. If not provided it will be assumed 100.
    :return: Returns the excess mortality for a given period.
    If no start and end weeks are given, then it will return excess death for the whole available period.
    '''
    df = pd.read_csv(file)
    df = df[(df['Week'] >= week_start) & (df['Week'] <= week_end)]

    return sum(df['excess_death'])