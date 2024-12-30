class BaseMoneymanagerException(BaseException):
    """Base exception for all exception classes on MoneyManager app.

    This is the parent exception class that all other custom exceptions
    in the MoneyManager application should inherit from. It allows for
    catching all application-specific exceptions with a single except clause.
    """


class InvalidInput(BaseMoneymanagerException):
    """Exception raised when user input doesn't meet expected format or constraints."""


class UserCancel(BaseMoneymanagerException):
    """Exception raised when user explicitly cancels an operation."""


class UserExit(BaseMoneymanagerException):
    """Exception raised when user chooses to exit the application."""


class UnexpectedException(BaseMoneymanagerException):
    """Exceptions that is unexpected to happen."""
