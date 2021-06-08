import importlib
import os
import sys

from .fake_context import FakeContext


class LambdaModule:
    def __init__(self) -> None:
        pass

    def context():
        """
        Return a fake Lambda context object
        To use this within a test module, do:
            from fixtures import context
            context = pytest.fixture(context)
        """
        return FakeContext()

    def lambda_module(request):
        # Inject environment variables
        backup_environ = {}
        for key, value in request.param.get("environ", {}).items():
            if key in os.environ:
                backup_environ[key] = os.environ[key]
            os.environ[key] = value

        # Add path for Lambda function
        sys.path.insert(
            0, os.path.dirname(os.path.abspath(request.param["module_name"]))
        )

        # Save the list of previously loaded modules
        prev_modules = list(sys.modules.keys())

        # Return the function module
        module = importlib.import_module(request.param["module_name"])
        yield module

        # Delete newly loaded modules
        new_keys = list(sys.modules.keys())
        for key in new_keys:
            if key not in prev_modules:
                del sys.modules[key]

        # Delete function module
        del module

        # Remove the Lambda function from path
        sys.path.pop(0)

        # Restore environment variables
        for key in request.param.get("environ", {}).keys():
            if key in backup_environ:
                os.environ[key] = backup_environ[key]
            else:
                del os.environ[key]
