from gtts import gTTS

texto = "Saludos chicos y recuerden protegerse y tratar, en lo posible de no salir de aquí."
lenguaje = 'es'

audio = gTTS(text = texto, lang = lenguaje, slow = False)
audio.save('audio.mp3')

print("Proceso Terminado")
