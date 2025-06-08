# Made By can-maker,cab-maker,CoderBoy231 ...
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


# Theme and color settings for a sleek look
sg.theme_background_color('black')
sg.theme_button_color(('black', '#d3d3d3'))
sg.theme_element_background_color('#F5F5DC')
sg.theme_text_element_background_color('black')

button_style = {'size': (12, 1), 'button_color': (
    'black', '#d3d3d3'), 'border_width': 0, 'pad': (5, 5)}

layout = [
    [sg.Frame('', [
        [sg.Button('Text Analyse', key='-text_analyze-', **button_style),
         sg.Button('WordCounter', key='-wordcount-', **button_style),
         sg.Button('New Unique', key='-newunique-', **button_style)],
    ], background_color='#d3d3d3', element_justification='center', pad=(0, 10), expand_x=True)],

    [sg.Column([
        [sg.Text("Enter text here:", background_color='black',
                 font=('Helvetica', 12, 'bold'))],
        [sg.Multiline(key='-INPUT-', size=(40, 15), background_color='white',
                      font=('Helvetica', 12))],
    ], element_justification='center', expand_y=True),

        sg.VSeparator(),

        sg.Column([
            [sg.Text('Word Counter:', background_color='black', font=('Helvetica', 12, 'bold')),
             sg.Text('', key='-WORD_COUNTER-', font=('Helvetica', 12), background_color='black', text_color="black")],
            [sg.Text('Text Analyse:', background_color='black', font=('Helvetica', 12, 'bold')),
             sg.Text('', key='-LABEL2-', font=('Helvetica', 12), background_color='black', text_color="black")],
            [sg.Text('New Unique:', background_color='black', font=('Helvetica', 12, 'bold')),
             sg.Text('', key='-NewUni-', font=('Helvetica', 12), background_color='black', text_color="black")],

        ], element_justification='left', pad=(0, 10), expand_y=True)]
]

window = sg.Window('Quillbot Noob Edition', layout,
                   size=(839, 450), finalize=True)


while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-wordcount-':
        input_text = values['-INPUT-']
        if not input_text.strip():
            window['-WORD_COUNTER-'].update('No input received',
                                            text_color='white')
        else:
            counter = word_counter(input_text)
            window['-WORD_COUNTER-'].update(
                f'The Word Count Is {counter}', text_color='white')

    if event == '-text_analyze-':
        input_text = values['-INPUT-']

        if not input_text.strip():
            window['-LABEL2-'].update('The input was blank, try again.',
                                      text_color='white')
        else:
            sent_count, char_count = text_analyze(input_text)

            # Display results
            if sent_count == 1 and char_count == 1:
                window['-LABEL2-'].update(
                    f"There is {sent_count} sentence and {char_count} letter.", text_color='white')
            elif sent_count == 1:
                window['-LABEL2-'].update(
                    f"There is {sent_count} sentence and {char_count} letters.", text_color='white')
            elif sent_count > 1 and char_count == 1:
                window['-LABEL2-'].update(
                    f"There are {sent_count} sentences and {char_count} letter.", text_color='white')
            else:
                window['-LABEL2-'].update(
                    f"There are {sent_count} sentences and {char_count} letters.", text_color='white')

end_time = time.time()
print("Execution time {:.6f} seconds".format(end_time - start_time))
