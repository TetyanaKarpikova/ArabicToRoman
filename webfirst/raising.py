class InvalidRomanError(Exception):
    """Class for exception """

    def __init__(self, str_roman):
        Exception.__init__(self)
        self.str_wrong = str_roman
