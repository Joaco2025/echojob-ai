import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# 1. Cargar las llaves del archivo .env
load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("ELEVENLABS_VOICE_ID")

if not api_key:
    print("❌ ERROR: No encontré la API KEY en el archivo .env")
    exit()

print("✅ API Key encontrada. Intentando conectar con ElevenLabs...")

try:
    # 2. Conectar el cliente
    client = ElevenLabs(api_key=api_key)

    # 3. Generar audio
    # Usamos 'eleven_multilingual_v2' porque habla español e inglés increíble.
    audio = client.text_to_speech.convert(
        text="Hola MockMate. Estoy listo para la entrevista de trabajo.",
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128"
    )

    # 4. Guardar el archivo para probarlo
    # (Como es un generador, hay que consumir los bytes)
    save_file_path = "prueba_audio.mp3"
    with open(save_file_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    print(f"🎉 ¡ÉXITO! Audio guardado en: {save_file_path}")
    print("Ve a la carpeta backend y reprodúcelo.")

except Exception as e:
    print(f"🔥 Ocurrió un error: {e}")