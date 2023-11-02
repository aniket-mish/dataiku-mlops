from loguru import logger


def foo() -> str:
    """Summary line.

    Extended description of function.

    Args:
        foo (str): Description of arg1

    Returns:
        str: Description of return value
    """

    logger.info("foo function called.")

    return "foo"
