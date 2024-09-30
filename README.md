# KeyStrokeLogger

This repository includes the code for a simple key stroke logger written in python. This is a small application that runs in the background, taking each key pressed by the user, conditionally adding/removing the pressed key from a logger stream and then writing the logs to a file when the return key is pressed.

These logs files can be used for further data processing such as to see if users have accidentally typed their password in some place which could pose security risks or other similar analysis.

### Usage

---

```bash
# Run the program, outputting logs to /tmp
python3 ./KeyStrokeLogger -output-folder /tmp
```
