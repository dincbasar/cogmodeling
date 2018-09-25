# actr-project
For 85-412 Final Project

1) Firstly, ACT-R must be running when ./setup.sh is called

To run setup script on MacOS:

2) ./setup.sh

This will install the necessary packages and run the model

2a) To run manually, call "python3 draw.py", which will initiate a perfect
      model for display purposes
2b) Training code is available in the project.py module

3) in the "tk" window that just opened, draw a letter by dragging your mouse

4) click "save"

5) click "run model" to run the CNN image recognition model, this will display
    both the recognized letter and the confidence level

6) click "send to ACT-R" to run the ACT-R model with the recognized letter,
      this will open two displays. one will be the window where the act-r
      model will get the input letter, and the other will be where it makes
      the actual drawing

7) this process can be repeated for as long as you wish, click "clear" in the
      tk window and repeat from step 3

Note: This is a perfect model for display purposes, to see how it learns, it is
        possible to set the "display" value to False in the draw.py module
        line 79, but it will take hundreds of trials to reach a perfect model,
        and thus is not advised
