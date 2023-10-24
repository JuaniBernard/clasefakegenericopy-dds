# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en /clasefakegenericopy-dds
WORKDIR /clasefakegenericopy-dds

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt /clasefakegenericopy-dds/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de la aplicación al contenedor
COPY . /app/

# Expone el puerto en el que se ejecutará tu aplicación FastAPI
EXPOSE 8000

# Ejecuta tu aplicación con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]