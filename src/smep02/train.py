"""SageMaker entrypoint is invoked as cmd line."""

from bad_modname import friendly_name as bad_friendly_name
from smep02.util import name


def bad_main():
    return f"{name} - {bad_friendly_name}: train"


def good_main():
    return f"{name}: train"


if __name__ == "__main__":
    print("Train script from cli: good_main:", good_main())
    print("Train script from cli: bad_main", good_main())
