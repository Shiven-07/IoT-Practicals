# Node-RED practical: source gaps and expected behavior

The supplied book provides the aim and a short setup outline, but no importable flow.

## Required behavior

1. A dashboard switch stores the user's requested LED state.
2. A physical button press overrides the output to ON for five seconds.
3. When the timer expires, restore the most recently requested dashboard state, including a change made during the override.
4. Define and test repeated button presses: restarting the five-second timer is one possible design choice, not specified by the PDF.

The source names BCM18 for the LED but does not specify a button GPIO, pull-up/pull-down arrangement or debounce settings. Get the lab's wiring and flow, or implement these explicitly before deploying. Its camera-connection sentence is unrelated to this exercise.

## What to obtain from the lab

- A flow export (.json) and the dashboard/node package versions it requires.
- Complete button wiring and the matching GPIO input configuration.
- Confirmation of active-high/active-low input logic.
- Output screenshots from a real test.

The source refers to the legacy node-red-dashboard package. Do not assume a flow for it will import unchanged into a different dashboard package.

See [Node-RED's Raspberry Pi guide](https://nodered.org/docs/getting-started/raspberrypi) for platform setup. The original procedure is preserved in [source.pdf](source.pdf).
