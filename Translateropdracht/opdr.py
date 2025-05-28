#Opdracht translater
import os
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, "source_texts")
TARGET_DIR = os.path.join(BASE_DIR, "translated_texts")

LANGUAGE_TO = "nl"  # Bijvoorbeeld Nederlands

CHUNK_SIZE = 4500  # Veilig onder de limiet blijven

def chunk_text(text, size):
    return [text[i:i+size] for i in range(0, len(text), size)]

def translate_file(file_path, target_path, target_lang):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    chunks = chunk_text(text, CHUNK_SIZE)
    translated_chunks = []
    for chunk in chunks:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(chunk)
        translated_chunks.append(translated)

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(translated_chunks))

def translate_all_texts(source_dir, target_dir, lang):
    os.makedirs(target_dir, exist_ok=True)
    for filename in os.listdir(source_dir):
        if filename.endswith(".txt"):
            src_path = os.path.join(source_dir, filename)
            tgt_path = os.path.join(target_dir, filename)
            print(f"Translating: {filename}")
            translate_file(src_path, tgt_path, lang)

def list_and_select_file(directory):
    files = [f for f in os.listdir(directory) if f.endswith(".txt")]
    for idx, f in enumerate(files):
        print(f"{idx + 1}. {f}")
    choice = int(input("Kies een tekst om voor te lezen: ")) - 1
    return os.path.join(directory, files[choice])

def speak_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    tts = gTTS(text=text, lang='nl')
    temp_mp3 = "temp_audio.mp3"
    tts.save(temp_mp3)
    playsound(temp_mp3)
    os.remove(temp_mp3)

# === RUN SCRIPT ===
translate_all_texts(SOURCE_DIR, TARGET_DIR, LANGUAGE_TO)
selected_file = list_and_select_file(TARGET_DIR)
speak_file(selected_file)
