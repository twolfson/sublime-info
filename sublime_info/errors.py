# Define a custom exception for when Sublime cannot be located
class STNotFoundError(Exception):
    pass


class STNotResolvedError(STNotFoundError):
    pass


class STBadLocationError(STNotFoundError):
    pass
