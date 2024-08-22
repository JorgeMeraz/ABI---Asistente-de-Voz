import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import geocoder
import requests
from bs4 import BeautifulSoup
import webbrowser
import time

# Nombre del asistente
nombre_asistente = "ABI"

# Inicializar el reconocedor de voz y el motor de texto a voz
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustar para el ruido de fondo
        audio = recognizer.listen(source)

    try:
        # Reconocer el habla usando el servicio de reconocimiento de voz de Google
        query = recognizer.recognize_google(audio, language="es-419")  # Español latinoamericano
        print("Dijiste:", query)
        return query
    except sr.UnknownValueError:
        print("Lo siento, no entendí eso.")
        return ""
    except sr.RequestError as e:
        print(f"No se pudieron solicitar los resultados del servicio de reconocimiento de voz de Google; {e}")
        return ""

def speak(text):
    tts = gTTS(text=text, lang='es')
    tts.save("output.mp3")
    os.system("start output.mp3")
    # Esperar hasta que termine de hablar
    time.sleep(len(text) // 10)

def process_query(query):
    if "Hola" in query:
        return f"¡Hola! Soy {nombre_asistente}. ¿En qué puedo ayudarte?"
    elif "adiós" in query:
        return "¡Adiós!"
    elif "abrir" in query:
        words = query.split()
        app_name = ' '.join(words[words.index("abrir") + 1:])
        open_application(app_name)
        return f"Abriendo {app_name}..."
    elif "Cuál es tu nombre" in query:
        return f"Mi nombre es {nombre_asistente}. ¿Cómo puedo ayudarte?"
    elif "Cuál es mi nombre" in query:
        return "Tu nombre es Jorge"
    elif "Fer es de mongolia" in query:
        return "No, Fer es de Honduras"
    elif "Cuál es la capital de Francia" in query:
        return "La capital de Francia es París."
    elif "Cuál es la capital de Honduras" in query:
        return "La capital de Honduras es Tegucigalpa."
    elif "Quién es el mejor jugador del mundo" in query:
        return "El mejor jugador del mundo es Lionel Messi."
    elif "cómo está el clima" in query:
        get_weather()
        return ""
    elif "dónde estoy" in query or "qué lugar es este" in query:
        get_location()
        return "Buscando tu ubicación..."
    elif "qué hora es" in query:
        now = datetime.datetime.now()
        hora = now.strftime("%H:%M")
        return f"La hora actual es {hora}"
    elif "juega el barcelona" in query:
        return get_barcelona_match()
    elif "Cuántos goles lleva Messi" in query:
        return get_messi_goals()
    elif "Pon música" in query or "reproduce" in query:
        speak("¿Qué canción quieres reproducir?")
        song_query = listen()
        play_youtube_song(song_query)
        return "Reproduciendo música..."
    else:
        return "Lo siento, no entendí eso. ¿Puedes repetirlo?"

def open_application(app_name):
    if "explorador" in app_name:  # Abrir el explorador de archivos
        os.system("start explorer.exe")
    elif "calculadora" in app_name:  # Abrir la calculadora
        os.system("start calc.exe")
    elif "camara" in app_name:  # Abrir la cámara
        os.system("start microsoft.windows.camera:")
    elif "Word" in app_name:  # Abrir Microsoft Word
        os.system("start winword")
    elif "excel" in app_name:  # Abrir Microsoft Excel
        os.system("start excel")
    elif "powerpoint" in app_name:  # Abrir Microsoft PowerPoint
        os.system("start powerpnt")
    elif "bloc de notas" in app_name:  # Abrir Bloc de notas
        os.system("start notepad")
    else:
        speak(f"No puedo abrir {app_name}.")

def get_location():
    g = geocoder.ip('me')
    location = g.city
    if location:
        speak(f"Te encuentras en {location}.")
    else:
        speak("No se pudo obtener la ubicación.")

def get_weather():
    url = 'https://www.google.com/search?q=clima'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        weather_info = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text
        speak(f"El clima actual es {weather_info}.")
    else:
        speak("No se pudo obtener la información del clima.")

def get_barcelona_match():
    today = datetime.date.today()
    url = 'https://www.fcbarcelona.com/es/futbol/primer-equipo/calendario'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        matches = soup.find_all('div', class_='match')
        for match in matches:
            match_date = match.find('time').text.strip()
            match_date = datetime.datetime.strptime(match_date, '%d/%m/%Y').date()
            if match_date == today:
                opponent = match.find('div', class_='team').text.strip()
                return f"Hoy juega el FC Barcelona contra {opponent}."
        return "Hoy el FC Barcelona no tiene partido."
    else:
        return "No se pudo obtener la información del FC Barcelona."

def play_youtube_song(song_name):
    query = song_name.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def get_messi_goals():
    url = 'https://messi.com'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        goals = soup.find_all('div', class_='c-number__content')
        total_goals = goals[1].text.strip()
        return f"Lionel Messi ha marcado {total_goals} goles en total."
    else:
        return "No se pudo obtener la información de los goles de Messi."

def main():
    while True:
        print("Di algo (o di 'salir' para terminar):")
        query = listen()
        if query.lower() == "salir":
            break
        response_text = process_query(query)
        print("Respuesta:", response_text)
        speak(response_text)

if __name__ == "__main__":
    main()
