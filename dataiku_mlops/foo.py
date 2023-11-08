from loguru import logger


def foo(arg1) -> str:
    """Summary line.

    Extended description of function.

    Args:
        arg1: Description of arg1

    Returns:
        str: Description of return value
    """

    logger.info("foo function called.")

    return "foo"
