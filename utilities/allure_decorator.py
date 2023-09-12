import inspect
import allure


def allure_auto_step(cls):
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if name != "__init__":
            setattr(cls, name, allure.step(method))
    return cls
