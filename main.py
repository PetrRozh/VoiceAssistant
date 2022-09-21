import sys

import speech_recognition
import pyttsx3
import os
from googlesearch import search
import webbrowser


def record_and_recognize_audio(*args: tuple):

    with microphone:
        recognized_data = ""

        recognizer.adjust_for_microphone, duration=2)

        try:
            print("Слушаю...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("Проверь свой микрофон, пожалуйста.. ;)")
            return

        try:
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        return recognized_data


def quit(*args: tuple):

    sys.exit()


def search_for_term_on_google(*args: tuple):

    if not args[0]: return
    search_term = " ".join(args[0])

    # открытие ссылки на поисковик в браузере
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)
    search_results = []
    return

    print(search_results)


def open1file(*args: tuple):
    os.system('taskmgr.exe')


def open2file(*args: tuple):
    os.system('control')


def new_window_brow(*args: tuple):
    os.system('start chrome www.google.com')


def wifi(*args: tuple):
    os.system("netsh wlan disconnect")


def sub(*args):
    numbers = []
    for i in voice_input:
        if i.isnumeric() == True:
            numbers.append(int(i))
    ans = int(numbers[0]) - int(numbers[1])
    print(ans)


def execute_command_with_name(command_name: str, *args: list):

    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass


commands = {
    ("до свидания", "пока"): quit,
    ("найди"): search_for_term_on_google,
    ("диспетчер задач"): open1file,
    ("панель управления"): open2file,
    ("новая вкладка в браузере"): new_window_brow,
    ("выключи wi-fi"): wifi,
    ("вычти"): sub,
}

if __name__ == "__main__":

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    ttsEngine = pyttsx3.init()

    while True:

        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input)

        voice_input = voice_input.split(" ")
        command = voice_input[0]
        command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        execute_command_with_name(command, command_options)
