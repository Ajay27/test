class AssertionError(Exception):
  pass


class PageNotLoadedError(Exception):
  pass


class LoginFailedError(Exception):
  pass


class ElementNotFoundError(Exception):
  pass


class ValidationError(Exception):
    def init(self, msg=None):
        self.message = msg


class ItemNotFoundError(Exception):
    """It is used when search result is empty"""
    pass