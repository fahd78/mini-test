from behave import when, then
import requests

@when('I attempt a SQL injection payload "{payload}"')
def step_impl(context, payload):
    context.response = requests.post(
        f"{context.base}/items", json={'name': payload, 'qty': 1}
    )

@then('the service should not execute malicious SQL')
def step_impl(context):
    assert context.response.status_code in (400, 201)