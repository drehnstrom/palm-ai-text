from flask import Flask, render_template, request
import os
import yaml
import vertexai
from vertexai.language_models import TextGenerationModel

app = Flask(__name__)

def get_config_value(config, section, key, default=None):
    """
    Retrieve a configuration value from a section with an optional default value.
    """
    try:
        return config[section][key]
    except:
        return default
        
with open('config.yaml') as f:
    config = yaml.safe_load(f)

TITLE = get_config_value(config, 'app', 'title', 'Ask Google')
SUBTITLE = get_config_value(config, 'app', 'subtitle', 'Your friendly Bot')
CONTEXT = get_config_value(config, 'palm', 'context', 'You are a bot who can answer all sorts of questions')
BOTNAME = get_config_value(config, 'palm', 'botname', 'Google')
TEMPERATURE = get_config_value(config, 'palm', 'temperature', 0.8)
MAX_OUTPUT_TOKENS = get_config_value(config, 'palm', 'max_output_tokens', 256)
TOP_P = get_config_value(config, 'palm', 'top_p', 0.8)
TOP_K = get_config_value(config, 'palm', 'top_k', 40)



@app.route("/", methods = ['POST', 'GET'])
def main():
    if request.method == 'POST':
        input = request.form['input']
        response = get_response(input)
    else: 
        input = ""
        response = get_response("Who are you and what can you do?")

    model = {"title": TITLE, "subtitle": SUBTITLE, "botname": BOTNAME, "message": response, "input": input}
    return render_template('index.html', model=model)


def get_response(input):
    vertexai.init(project="vertext-ai-dar", location="us-central1")
    parameters = {
        "temperature": TEMPERATURE,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "top_p": TOP_P,
        "top_k": TOP_K
    }

    model = TextGenerationModel.from_pretrained("text-bison@001")
    request = """{0}.
    
    input: {1}
    output:
    """
    response = model.predict(
        request.format(CONTEXT, input),
        **parameters
    )
    return response
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    
