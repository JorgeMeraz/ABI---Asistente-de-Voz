🤖 ABI - Asistente de Voz
ABI es un asistente de voz simple que puede responder a comandos de voz en español, como preguntar la hora, abrir aplicaciones en tu computadora, buscar información en la web, y más.

📄 Descripción del Proyecto
Este proyecto implementa un asistente de voz en Python que utiliza las siguientes bibliotecas:

SpeechRecognition: para el reconocimiento de voz.
gTTS (Google Text-to-Speech): para convertir texto a voz.
os: para ejecutar comandos del sistema.
datetime: para obtener la hora y fecha actual.
geocoder: para obtener la ubicación geográfica.
requests: para realizar peticiones HTTP.
BeautifulSoup: para analizar contenido HTML.
webbrowser: para abrir URLs en el navegador.
time: para manejar pausas en la ejecución.

💻 Requisitos
Antes de ejecutar el proyecto, asegúrate de tener Python instalado y las siguientes dependencias:
pip install
SpeechRecognition 
gTTS 
geocoder 
requests 
beautifulsoup4


🚀 Uso
Para ejecutar el asistente de voz, sigue estos pasos:

Clona el repositorio:

git clone https://github.com/tuusuario/ABI-asistente-voz.git
cd ABI-asistente-voz

Configura tu micrófono correctamente en tu sistema.
Ejecuta el script:
python abi.py


El asistente comenzará a escuchar tus comandos de voz. Puedes decir comandos como:

"Hola"
"Qué hora es"
"Cómo está el clima"
"Abrir explorador"
"Adiós" para terminar la sesión
ℹ️ Notas Adicionales
El asistente solo entiende comandos en español.
Para algunas funciones, como obtener el clima o la ubicación, se requiere una conexión a Internet.
Puedes personalizar los comandos o añadir más funcionalidades modificando el código en abi.py.


