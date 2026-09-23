import re
import unicodedata

TERMINOS_PROTEGIDOS = {
    r'saque de esquina|tiro de esquina|c[oó]rner': 'tiro_de_esquina',
    r'saque de banda': 'saque_de_banda',
    r'tarjeta amarilla|cartulina amarilla': 'tarjeta_amarilla',
    r'tarjeta roja|cartulina roja': 'tarjeta_roja',
    r'fuera de juego(?:s)?|fuera de lugar': 'fuera_de_juego',
    r'bal[oó]n parado': 'balon_parado',
}

PALABRAS_VACIAS = {
    'a', 'al', 'ante', 'bajo', 'con', 'contra', 'de', 'del', 'desde', 'durante', 'en', 'entre',
    'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'sobre', 'tras',
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'lo',
    'y', 'o', 'u', 'e', 'ni', 'que', 'pero', 'aunque', 'porque', 'si', 'como',
    'yo', 'tu', 'tú', 'él', 'ella', 'ello', 'nosotros', 'vosotros', 'ellos', 'ellas',
    'me', 'te', 'se', 'le', 'les', 'su', 'sus', 'mi', 'mis',
    'esto', 'eso', 'esa', 'ese', 'esta', 'este', 'esas', 'esos', 'estas', 'estos', 'aquello',
    'es', 'ha', 'han', 'va', 'hay', 'está', 'están', 'era', 'fue', 'ser', 'estar',
    'tiene', 'tienen', 'soy', 'somos', 'sido',
    'no', 'sí', 'más', 'muy', 'ya', 'también', 'ahora', 'ahí', 'aquí', 'así',
    'cómo', 'qué', 'cuál', 'cuándo', 'dónde', 'quién',
    'todo', 'toda', 'todos', 'todas', 'otra', 'otro', 'otros', 'otras',
    'cada', 'algo', 'alguna', 'alguno', 'algunos', 'algunas', 'mismo', 'misma',
}

MULETILLAS = {
    'eh', 'ehh', 'bueno', 'vamos', 'ver', 'vemos', 'mira', 'miren', 'oye',
    'digamos', 'verdad', 'evidentemente', 'prácticamente', 'sabemos',
    'creo', 'fíjate', 'ojo', 'decir', 'pues',
}

TOKEN_RE = re.compile(r"[a-záéíóúñüç]+(?:_[a-záéíóúñüç]+)*")


def normalizar_texto(texto):
    texto = unicodedata.normalize('NFC', str(texto)).lower()
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto


def proteger_terminos(texto, terminos=TERMINOS_PROTEGIDOS):
    for patron, token in terminos.items():
        texto = re.sub(patron, token, texto, flags=re.IGNORECASE)
    return texto


def tokenizar(texto):
    return TOKEN_RE.findall(texto)


def quitar_vacias(tokens, vacias=PALABRAS_VACIAS | MULETILLAS):
    return [t for t in tokens if t not in vacias and len(t) > 1]


def preprocesar_texto(texto):
    texto = normalizar_texto(texto)
    texto = proteger_terminos(texto)
    tokens = tokenizar(texto)
    return quitar_vacias(tokens)
