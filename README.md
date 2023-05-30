# hacku-challenge

Formulario

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python (versión 3.9)
- Virtualenv (opcional pero recomendado)

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
   git clone https://github.com/wam24/hacku-challenge.git
   ```

2. Ve al directorio del proyecto:

```bash
    cd hacku-challenge
```

3. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
  virtualenv venv 
  source venv/bin/activate
```

4. Instala las dependencias del proyecto:

```bash
  pip install -r requirements.txt

```
5. Ejecutar migraciones:
```bash
  python www/manage.py migrate

```

## Ejecución

Una vez que hayas realizado la instalación, puedes ejecutar el proyecto con el siguiente comando:

```bash
  python manage.py runserver
```

Cuando ingrese a la aplicación podrá observar el formulario