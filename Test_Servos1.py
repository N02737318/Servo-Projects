import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)


GPIO.setmode(GPIO.BCM)

pin = { }

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('ledonoff.html', **templateData)