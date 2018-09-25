import actr, string, dict, correctDict

actr.load_act_r_model("ACT-R:tutorial;actr-project;project-model.lisp")

# globals

global window, window_reading, clickList, isStart, windowX, windowY, k, chunk_defs, chunk_names

clickList = []

isStart = False

windowX = 550
windowY = 550

k = 6                       # adjust size of drawing

chunk_defs = None
chunk_names = None

# will return true if the click is to signal start -> not active any more
def startClick():
    return numclicks%2 == 1

# makes the drawing on the act-r screen
def drawLine(start, end):
    global window
    actr.add_line_to_exp_window(window, start, end, 'black')

# mouse click handler, adds the relevant coordinates to the clicklist and
# makes the drawing if its the end click of a stroke
def process_click(model, location, finger):
    global isStart, clickList, clickList, k

    if (not model):
        return

    if not isStart:
        (x1, y1) = (k * location[0], k * location[1])
        clickList.append((x1,y1))
    else:
        (x2, y2) = (k * location[0], k * location[1])
        (x1, y1) = clickList.pop(-1)
        drawLine([x1, y1], [x2, y2])
        clickList.append((x1, y1, x2, y2))

    isStart = not isStart

# defines all of the relevant chunks in act-r
def define_chunks(defs = False):
    global chunk_names, chunk_defs;

    if (chunk_names == None):
        chunk_defs = dict.make_chunk_defs();

    if (not defs):
        chunk_names = dict.make_chunk_names(chunk_defs);

    return chunk_defs if defs else chunk_names

# presents one training example to the model, no waiting afterwards
def train_once(letter):
    global chunk_names;

    for chunk in chunk_names[letter]:
        actr.set_buffer_chunk('imaginal', chunk[0])
        actr.clear_buffer('imaginal')

    return

# presents n many training examples to the model, no waiting afterwards
def train_n(n, letter):
    global chunk_names

    for i in range(n):
        train_once(letter)

    return

# presents trial to the model
# given_letter is what the model is supposed to reproduce, this is passed by the
#           integration code between CNN and act-r
# train_epochs is the data collection parameter mentioned in the final report
#           specifying how many times the model will get trained if it makes mistake
# new_window and open_window are used by various functions to diplay a window or not
# delay_time is another parameter that was mentioned in the final report
#           it is how much the model waits after being trained
# display is set to true if the model is being ran for display purposes only
#           and not being trained. in this case, it will not make a mistake
def present_trial(given_letter = None, train_epochs = 1,
            new_window = True, open_window = True, delay_time = 10, display = False):

    global window, window_reading, clickList, chunk_names, chunk_defs

    if (given_letter == None):
        letterList = actr.permute_list(list(string.ascii_uppercase))
        chosen_letter = letterList[0]
    else:
        chosen_letter = given_letter

    if display:
        train_n(10, chosen_letter)

    clickList = []

    actr.clear_exp_window(window_reading)
    actr.clear_exp_window(window)

    actr.add_text_to_exp_window(window_reading, chosen_letter, 125, 150)

    actr.add_command('process-click',process_click)
    actr.monitor_command('click-mouse','process-click')

    actr.run(1000, open_window)        # for actr time or real time

    correct = correct_drawing(chosen_letter, clickList)

    if (correct):
        train_once(chosen_letter)
        actr.run_full_time(delay_time)

    else:
        train_n(train_epochs, chosen_letter)
        actr.run_full_time(delay_time)

    actr.remove_command_monitor('click-mouse', 'process-click')
    actr.remove_command('process-click')

    return (clickList, correct)

# presents all letters in the alphabet as a trial to the model
def present_alphabet():

    for letter in list(string.ascii_uppercase):
        present_trial(letter)

# checks if the drawing done by the model was correct
def correct_drawing(chosen_letter, clickList):

    for stroke in correct_dict[chosen_letter]:
        if stroke not in clickList:
            return False

    return True

# the function used to collect the data we studied in the final report
def collect_data(n = 5000, given_train_epochs = 5, given_delay_time = 20):

    correctCount = 0
    delta = 0

    correctness_list = []

    for i in range(n):
        letter = actr.permute_list(list(string.ascii_uppercase))[0]

        (clickList, correct) = present_trial(letter,
            train_epochs = given_train_epochs, delay_time = given_delay_time);

        correctCount += correct
        delta += correct

        if (i % (n / 20) == 0):
            correctness_list.append(delta/(n/20))
            delta = 0

    print(n, given_train_epochs, given_delay_time)

    print(correctness_list)

    print (correctCount / n)

# runs alphabet based trials on the model
def run_trials(train_epochs = 1, new_window = False, open_window = False):
    global goalLetter

    alphabet = list(string.ascii_uppercase)

    for letter in alphabet:

        present_trial(letter, new_window = False, open_window = False);

# runs a perfectly accurate model once to collect the criteria for the
#            correct_drawing function to use when comparing
def correctness_trials(train_epochs = 1, new_window = True,
                    open_window = False, outCorrectPath = "outCorrect.txt"):

    global chunk_names, window

    alphabet = list(string.ascii_uppercase)

    outCorrect = open(outCorrectPath, "wt")

    for letter in alphabet:

        (stroke_list, correct) = present_trial(letter, new_window, open_window)
        outCorrect.write(letter + ": ")
        outCorrect.write(str(stroke_list));
        outCorrect.write("\n")

    outCorrect.close()

    return

# initiates all the necessary variables
def init_all(open_window = False):
    global window, window_reading, chunk_defs, chunk_names, correct_dict

    actr.reset()

    window = actr.open_exp_window("Letter Writing", open_window,
                                    windowX, windowY, 200, 300)
    window_reading = actr.open_exp_window("Letter Goal", open_window,
                                    windowX, windowY, 800, 300)
    actr.install_device(window_reading)
    actr.install_device(window)
    chunk_defs = define_chunks(defs = True)
    chunk_names = define_chunks(defs = False)
    correct_dict = correctDict.make_correct_dict()

# calls the initiation function when the code is being called for the first time
if (chunk_defs == None):
    init_all()
