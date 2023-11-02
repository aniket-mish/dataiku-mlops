from loguru import logger

class Foo:
    
    def __init__(self, name: str):
        self.name = name

    def foo(self) -> str:
        """Summary line.

        Extended description of function.

        Args:
            foo (str): Description of arg1

        Returns:
            str: Description of return value
        """

        logger.info(f"foo welcome you {self.name}")

        return "foo"