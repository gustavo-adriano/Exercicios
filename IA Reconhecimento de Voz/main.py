import speech_recognition as sr
def obter_audio(microfone):
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    return audio

def tranformar_audio(microfone,audio):
    try :
        frase = microfone.recognize_google(audio, language='pt-BR')
        return frase
    except sr.UnknownValueError:
        print("Não entendi a frase.")

def escutar_microfone():
    microfone = sr.Recognizer()
    audio = obter_audio(microfone)
    texto = tranformar_audio(microfone, audio)
    return texto
if __name__ == '__main__':
    texto = escutar_microfone()
    print("A Frase dita foi: " + texto)
