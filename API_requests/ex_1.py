import json


def get_second_message(json_text):
    try:
        parsed_text = json.loads(json_text)
    except TypeError:
        return f"Error: json_text should be a string, but it is {type(json_text)}"

    if len(parsed_text["messages"]) > 1:
        second_message = parsed_text["messages"][1]
        return second_message
    else:
        return "Error: List index out of range"


json_text = '''{
  "messages": [
    {
      "message": "This is the first message",
      "timestamp": "2021-06-04 16:40:53"
    },
    {
      "message": "And this is a second message",
      "timestamp": "2021-06-04 16:41:01"
    }
  ]
}'''
print(get_second_message(json_text))
