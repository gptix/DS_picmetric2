import pickle

@app.route('/summary', methods=['POST'])
"""Receive and process a request for classification of one image."""
def summary():
    url = request['url']
    
    try:
        message = handle_one_url(url)

    except Exception as e:
        message = 'Error from predictor: " + e

    return (message)


@app.route('/batch_img_summary', methods=['POST'])
"""Receive and process a request for classification of a batch of images."""
def batch_img_summary():
    url_dict = request['url_dict']
    urls = pull_out_urls(url_dict)
    
    try:
        responses = []
        for u in urls:
            responses.append(handle_one_url(u))
        message = responses
    
    except:
         message = 'Error from predictor: " + e

    return (message)


def handle_one_URL(url):
    answer_from_predictor = process_one_image(url)
    return convert_answer_to_json(answer_from_predictor)


def process_one_image(url)
"""Provide a URL to the classifier, and expect pickled response."""
# foo
return foo(url)


def convert_answer_to_json(answer):
"""Convert prediction from predictor response, which should be a
JSON object in pickled data format, to JSON. This is for delivery to 
the caller to one of our endpoints."""
return pickle.loads(answer)