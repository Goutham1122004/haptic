from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Morse Code Dictionary
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                   '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                   ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
                   '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
                   }

reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        translation_type = request.form.get('translation_type')
        input_text = request.form.get('input_text').strip()

        if translation_type == 'text_to_morse':
            result = text_to_morse_code(input_text)
        elif translation_type == 'morse_to_text':
            result = morse_code_to_text(input_text)
        else:
            result = "Invalid Translation Type"

        return render_template('index.html', result=result, input_text=input_text)

    return render_template('index.html')

def text_to_morse_code(text):
    text = text.upper()
    if not text:
        flash("Please enter some text.", "warning")
        return ""
    
    morse_code = ""
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            morse_code += char
    return morse_code.strip()

def morse_code_to_text(morse_code):
    morse_code = morse_code.split(" ")
    if not morse_code:
        flash("Please enter some Morse code.", "warning")
        return ""
    
    text = ""
    for code in morse_code:
        if code in reverse_morse_code_dict:
            text += reverse_morse_code_dict[code]
        else:
            text += code
    return text

if __name__ == '__main__':
    app.run(debug=True)
