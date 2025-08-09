# 🤖 Asistente de Investigación con LangChain y OpenAI

Este proyecto implementa un agente de IA que realiza investigaciones usando herramientas como Wikipedia y DuckDuckGo, estructurando las respuestas y permitiendo guardarlas en un archivo.  
El asistente está configurado para responder en español y puede buscar información tanto en la web como en Wikipedia (en español).

## 🚀 Características
- Uso de **LangChain** y **OpenAI GPT-4o-mini** para procesamiento de lenguaje.
- Integración con:
  - **Wikipedia** (idioma español).
  - **DuckDuckGo Search** para búsquedas web.
  - Guardado automático de resultados en archivo `.txt`.
- Salida estructurada con `Pydantic`.
- Fácil configuración mediante archivo `.env`.
- Estructura clara para pruebas (`test/`).

## 📂 Estructura del Proyecto
```
PROJECT_1/
│── src/
│   ├── main.py           # Script principal
│   ├── tools.py          # Definición de herramientas
│── test/
│   ├── test_main.py      # Pruebas para main.py
│   ├── test_tools.py     # Pruebas para tools.py
│── venv/                 # Entorno virtual (ignorado en Git)
│── .env                  # Variables de entorno (NO subir a GitHub)
│── sample.env            # Ejemplo de archivo .env
│── requirements.txt      # Dependencias del proyecto
│── README.md             # Este archivo
```

## ⚙️ Instalación y Ejecución

1. **Clonar el repositorio**:
```bash
git clone https://github.com/<TU_USUARIO>/<TU_REPO>.git
cd <TU_REPO>
```

2. **Crear y activar un entorno virtual**:
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```

3. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**:
Copia el archivo `sample.env` a `.env` y añade tu clave de OpenAI:
```
OPENAI_API_KEY=tu_api_key_aqui
```

5. **Ejecutar el asistente**:
```bash
python src/main.py
```

## 📝 Ejemplo de uso
```
¿Sobre qué tema te ayudo a investigar? Inteligencia Artificial
```
El agente buscará información y la guardará en `research_output.txt`.

## 📦 Dependencias principales
- `langchain`
- `langchain-openai`
- `langchain-community`
- `python-dotenv`
- `pydantic`

## ⚠️ Notas
- No subas tu `.env` a GitHub.
- El archivo `research_output.txt` irá acumulando resultados con fecha y hora.