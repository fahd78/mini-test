
from behave import given, when, then
import requests

@given('the server is running at "http://localhost:5001"')
def step_impl(context):
    context.base = "http://localhost:5001"

@when('I create an item with name "{name}" and qty {qty:d}')
def step_impl(context, name, qty):
    context.response = requests.post(
        f"{context.base}/items", json={'name': name, 'qty': qty}
    )

@then('the status code is {code:d}')
def step_impl(context, code):
    assert context.response.status_code == code

@then('the response contains an id')
def step_impl(context):
    assert 'id' in context.response.json()