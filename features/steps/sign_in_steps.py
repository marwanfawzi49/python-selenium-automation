from behave import given, when, then

@given("Open Target homepage")
def open_home(context):
    context.app.main_page.open_main()

@when("Click Account from header")
def click_account(context):
    context.app.header.click_account()

@when("From right-side menu, click Sign In")
def click_sign_in_menu(context):
    context.app.right_menu.verify_sign_in_heading()     # <- check for "Sign in" text
    context.app.right_menu.click_sign_in_from_menu()    # <- then click button


@then("Verify Sign In form is opened")
def verify_sign_in_opened(context):
    context.app.sign_in_page.verify_sign_in_form_opened()
