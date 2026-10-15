# Alumno 8: perímetro de un rectángulo

U2 · Actividad 3 · Implementación de CI con GitHub Actions.

## Función asignada

`perimetro_rectangulo(largo, ancho)` calcula `2 * (largo + ancho)`.
Por ejemplo, un rectángulo de largo 5 y ancho 3 tiene perímetro 16.
Las dos medidas deben expresarse en la misma unidad.

Se aceptan enteros y decimales finitos no negativos. Cero se admite como
caso límite de un rectángulo degenerado. Se rechazan texto, booleanos y
otros tipos con `TypeError`, y negativos, infinito y NaN con `ValueError`.
Un desbordamiento decimal produce `OverflowError`.

## Estructura

```text
perimetro-rectangulo/
├── perimetro_rectangulo.py
├── requirements.txt
├── README.md
├── .gitignore
├── tests/
│   └── test_perimetro_rectangulo.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Ejecución local

Desde la carpeta del proyecto, con Python 3.10 o posterior:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v
```

Ejemplo de uso:

```python
from perimetro_rectangulo import perimetro_rectangulo

print(perimetro_rectangulo(5, 3))  # 16
```

## Crear el repositorio desde cero

1. En GitHub, selecciona **New repository** y usa `perimetro-rectangulo-alumno8`.
2. Crea el repositorio vacío: no agregues README, licencia ni .gitignore.
3. Abre una terminal en esta carpeta y ejecuta los siguientes comandos.
   Sustituye `TU_USUARIO` por tu usuario real de GitHub.

```powershell
git init -b main
git add .
git commit -m "Implementar perimetro, pruebas y CI"
git remote add origin https://github.com/TU_USUARIO/perimetro-rectangulo-alumno8.git
git push -u origin main
```

Si Git solicita identidad, configura tu propio nombre y correo con
`git config user.name "Tu nombre"` y `git config user.email "Tu correo"`.
La autenticación con GitHub se realiza con tu cuenta, sin poner contraseñas
ni tokens dentro de los archivos del proyecto.

## Demostración obligatoria: verde → rojo → verde

Cada etapa requiere su propio commit y push. Espera a que termine el workflow
antes de pasar a la siguiente para conservar las tres ejecuciones como evidencia.

### 1. Pipeline verde inicial

Después del primer push, abre **Actions → CI - Pruebas del perimetro**.
Espera a que termine correctamente y guarda una captura con el nombre del
commit, el estado y los pasos de la ejecución.

### 2. Pipeline rojo intencional

En `tests/test_perimetro_rectangulo.py`, cambia únicamente la aserción
de `test_caso_correcto`:

```python
assert perimetro_rectangulo(5, 3) == 20
```

El resultado correcto es 16, por lo que esta expectativa incorrecta hará
fallar la prueba. No modifiques la función.

```powershell
git add tests/test_perimetro_rectangulo.py
git commit -m "Demostrar CI rojo con una expectativa incorrecta"
git push origin main
```

Espera a que Actions termine en rojo. Abre el paso **Ejecutar pytest** y
captura el fallo `assert 16 == 20` junto con la identificación del commit.

### 3. Pipeline verde final

Restaura la aserción correcta:

```python
assert perimetro_rectangulo(5, 3) == 16
```

```powershell
git add tests/test_perimetro_rectangulo.py
git commit -m "Corregir la expectativa y recuperar CI verde"
git push origin main
```

Espera a que Actions termine correctamente y guarda la tercera captura.
La versión final del repositorio debe tener todas las pruebas aprobadas.

## Qué entregar

- Enlace al repositorio nuevo.
- Enlaces o capturas de las tres ejecuciones: verde inicial, rojo intencional
  y verde final, con sus commits visibles.
- Explicación breve: el commit dispara el workflow; Actions obtiene el código,
  prepara Python 3.10, instala `requirements.txt` y ejecuta pytest. Una prueba
  fallida detiene la validación; al corregirla, la integración vuelve a pasar.

Las pruebas locales no sustituyen las evidencias de GitHub Actions.

## Referencias

- [GitHub: construir y probar Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
- [actions/setup-python](https://github.com/actions/setup-python)
- [actions/checkout](https://github.com/actions/checkout)
