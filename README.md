# rafter v1.0
Designed by Zoe S. for hensaku line-1
### What is rafter?
rafter is a Python module that allows 'animations' (.raf files) to be played on robots with a preset Servo control.
### How do I use rafter?
Well, at the moment that's a little tricky, as we have yet to actually set up the Servo controls physically. If you would like to figure it out or use it somehow in your project, Instructions will be provided.
1. Download the project
2. In the root directory, run ```pip install -r requirements.txt``` (assuming you have Python and Pip installed)
3. Edit the *config.json5* file and make sure the information is correct
<!-- -->
It is recommended that you use rafter as a module, as it's not designed to be run as a script.
### Possible Limitations / Issues
- rafter's effective speed is limited to Serial link speed.
- Possible out of range issues with motors.
