# Made By Jishnu , Arsh , Purab ...
# Colour code: Beige: #F5F5DC

import time
import PySimpleGUI as sg

start_time = time.time()

# Function to count words
def word_counter(text):
    words = text.split()
    word_count = len(words)
    return word_count

# Function to analyze text for word, sentence, and character counts
def text_analyze(text):
    words = text.split()
    word_dict = {}
    e = []

    # Build a dictionary of unique words
    for word in words:
        if word not in e:
            e.append(word)
    word_dict = dict(enumerate(e))

    # Count sentences based on '.', '!', and '?' marks
    sent_count = 0
    for word in word_dict.values():
        if '.' in word or '?' in word or '!' in word:
            sent_count += 1

    # Count characters (excluding spaces)
    char_count = sum(len(word) for word in word_dict.values())

    return sent_count, char_count

# GUI layout and theme
sg.theme_background_color('#F5F5DC')

layout = [
    [sg.Column([
        [sg.Button('Text Analyse', key='-text_analyze-', size=(10, 1)),
         sg.Button('WordCounter', key='-wordcount-', size=(10, 1)),
         sg.Button('New Unique', key='-newunique-', size=(10, 1))]],
        background_color='gray',
        pad=(0, 0),
        size=(839, 40)
    )],
    [
        sg.Column([
            [sg.Text("Enter text here:")],
            [sg.InputText(key='-INPUT-', size=(25, 1))],
        ], element_justification='left', expand_y=True),

        sg.VSeparator(),

        sg.Column([
            [sg.Text('', key='-WORD_COUNTER-', font='Any 12')],
            [sg.Text('', key='-LABEL2-', font='Any 12')]
        ], element_justification='center', expand_y=True),
    ]
]

window = sg.Window('Simple GUI', layout, size=(839, 375), finalize=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-wordcount-':
        input_text = values['-INPUT-']
        if not input_text.strip():
            window['-WORD_COUNTER-'].update('No input received')
        else:
            counter = word_counter(input_text)
            window['-WORD_COUNTER-'].update(f'The Word Count Is {counter}')

    if event == '-text_analyze-':
        input_text = values['-INPUT-']
        
        if not input_text.strip():
            window['-WORD_COUNTER-'].update('The input was blank, try again.')
        else:
            sent_count, char_count = text_analyze(input_text)

            # Display results
            if sent_count == 1 and char_count == 1:
                window['-LABEL2-'].update(f"There is {sent_count} sentence and {char_count} letter.")
            elif sent_count == 1:
                window['-LABEL2-'].update(f"There is {sent_count} sentence and {char_count} letters.")
            elif sent_count > 1 and char_count == 1:
                window['-LABEL2-'].update(f"There are {sent_count} sentences and {char_count} letter.")
            else:
                window['-LABEL2-'].update(f"There are {sent_count} sentences and {char_count} letters.")

end_time = time.time()
print("Execution time {:.6f} seconds".format(end_time - start_time))
