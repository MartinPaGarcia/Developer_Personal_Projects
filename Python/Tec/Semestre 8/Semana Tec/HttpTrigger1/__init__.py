import logging
import openai
import azure.functions as func

# sample request
# {"model":"text-davinci-003", "prompt":"dame un slogan para una empresa de inteligencia artificial", "max_tokens":200, "temperature":0}
secret_key = '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'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give OpenAI my secret key to authenticate
    openai.api_key = secret_key

    # get variables from HTTP request body
    req_body = req.get_json()

    # call OpenAI API
    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body['temperature']
    )

    # format the response
    output_text = output['choices'][0]['text']

    # echo the response
    return func.HttpResponse(output_text,
                             status_code=200)
