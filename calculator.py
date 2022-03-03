import json


def calculate(event, context):
    body = json.loads(event["body"])
    number1 = body["number1"]
    number2 = body["number2"]
    res = number1 + number2
    return {
        "statusCode": 200,
        "body": json.dumps("The sum of {0} and {1} is {2}".format(number1, number2, res))
    }
