
from behave import given, when, then
import requests

@given('the server is running at "http://localhost:5001"')
def step_impl(context):
    context.base = "http://localhost:5001"

@given('an item exists with name "{name}" and qty {qty:d}')
def step_impl(context, name, qty):
    response = requests.post(f"{context.base}/items", json={'name': name, 'qty': qty})
    response.raise_for_status()
    context.item_id = response.json()['id']

@when('I create an item with name "{name}" and qty {qty:d}')
def step_impl(context, name, qty):
    context.response = requests.post(
        f"{context.base}/items", json={'name': name, 'qty': qty}
    )

@when('I update item <id> to name "{name}" and qty {qty:d}')
def step_impl(context, name, qty):
    context.response = requests.put(
        f"{context.base}/items/{context.item_id}", json={'name': name, 'qty': qty}
    )

@when('I delete item <id>')
def step_impl(context):
    context.response = requests.delete(f"{context.base}/items/{context.item_id}")

@then('the status code is {code:d}')
def step_impl(context, code):
    assert context.response.status_code == code

@then('the response contains an id')
def step_impl(context):
    assert 'id' in context.response.json()

@then('the response JSON name is "{name}"')
def step_impl(context, name):
    assert context.response.json()['name'] == name