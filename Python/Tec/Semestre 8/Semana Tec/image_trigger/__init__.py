import logging
import openai
import azure.functions as func

# sample request
# {"prompt":"Cohete espacial girando por saturo", "n":1, "size":"1024x1024"}
secret_key = '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'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give OpenAI my secret key to authenticate
    openai.api_key = secret_key

    # get variables from HTTP request body
    req_body = req.get_json()

    # call OpenAI ImageAPI
    output = openai.Image.create(
        prompt = req_body['prompt'],
        n = req_body['n'],
        size = req_body['size'],
    )

    # format the response
    output_text = output['data'][0]['url']

    # echo the response
    return func.HttpResponse(output_text,
                             status_code=200)

