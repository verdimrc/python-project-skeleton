"""SageMaker inference script is imported as a module."""
from bad_modname import friendly_name as bad_friendly_name
from smep02.util import name


def bad_model_fn():
    return f"{name} - {bad_friendly_name}: inference"


def good_model_fn():
    return f"{name}: inference"
