# PaLM API Text demo

This demo is a Python Flask web app that uses the Google PaLM API for generative AI.

## To Run
1. Clone the repo
2. Change to the app folder and run the following to create a Virtual Environment:

```
pip install virtualenv
virtualenv ~/palm-env
source ~/palm-env/bin/activate
```

3. Use Pip to install the prequisites

```
pip install -r requirements.txt
```

4. To test the pogram run:

```
python main.py
```

## You can customize the program using the config.yaml file.

Here is an example. Changing the context will change the bahavior of the model. You can make the model pretend to be anything you want (a bartender, mechanic, whatever). The example below makes the model emulate a Barista. 

Change the YAML file and restart the program

```
app:
 title: "CoffeeBot"
 subtitle: "Your friendly online BaristAI"

palm:
  botname: "CoffeeBot"
  context: "Your name is CoffeeBot. You are a barista and expert on all things related to coffee and tea."
  temperature: 0.8
  max_output_tokens: 1024
  top_p: 0.8
  top_k: 40
```

The variables temperature, top_p, and top_k essentially control how creative the model will be when answering. Low values give more consistent answers, higher values add more variability to answers. 

temperature is in the range 0.0 to 1.0
top_p is in the range 0.0 to 1.0
top_k is in the range 1 to 40

max_output_tokens does just what the name implies. It is in the range 1 to 1024.