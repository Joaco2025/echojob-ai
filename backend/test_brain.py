import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: Falta la GEMINI_API_KEY en el .env")
    exit()

print(f"🔑 Usando API Key directa...")

try:
    # Configuración simplificada (Sin regiones, sin JSONs raros)
    genai.configure(api_key=api_key)
    
    # Usamos Gemini Flash
    model = genai.GenerativeModel('gemini-1.5-flash')

    print("🧠 Enviando mensaje...")
    response = model.generate_content("Hola, confirma que estás vivo con una frase corta.")
    
    print("\n" + "="*40)
    print("RESPUESTA DE GEMINI:")
    print(response.text)
    print("="*40 + "\n")
    print("✅ ¡ESTAMOS DENTRO!")

except Exception as e:
    print(f"\n🔥 Error: {e}")