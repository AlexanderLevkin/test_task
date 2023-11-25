import allure
import traceback
import os


# This method allows us to attach screenshots to allure reports
def attach_response_picture(screenshot, name):
    allure.attach(screenshot, name=name,
                  attachment_type=allure.attachment_type.PNG)


# This method allows us to attach text to allure reports
def attach_response_text(text, name):
    allure.attach(text, name=name,
                  attachment_type=allure.attachment_type.TEXT)


# If in our tst we get an error we handle it by this method
def handle_assertion_error(e):
    error_message = str(e)
    stack_trace = traceback.format_exc()
    directory = 'artifacts/fails/'
    os.makedirs(directory, exist_ok=True)
    # Write the error message and stack trace to a file
    with open('artifacts/fails/file.txt', 'w') as file:
        file.write(f"Error message: {error_message}\n\nStack trace:\n{stack_trace} + \n")
    # Attach the error message and stack trace to allure
    with allure.step("Handle assertion error"):
        attach_response_text(error_message, 'Error message')
    raise AssertionError(error_message)