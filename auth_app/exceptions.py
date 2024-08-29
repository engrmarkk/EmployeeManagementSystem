# auth_app/utils.py
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError


def custom_exception_handler(exc, context):
    # Get the standard error response from DRF
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, ValidationError):
            # Collect error messages and format them
            errors = []
            for field, messages in response.data.items():
                if isinstance(messages, list):
                    for message in messages:
                        errors.append(f"{message}")

            # Format the response with a single key
            response.data = {
                'message': errors[0]
            }
            response.status_code = response.status_code

    return response
