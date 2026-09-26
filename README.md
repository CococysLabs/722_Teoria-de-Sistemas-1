# 722_Teoria-de-Sistemas-1

Contenido, ejemplos y recursos del curso de Teoría de Sistemas 1.

## Guía de trabajo para tutores auxiliares

Bienvenido/a al equipo de tutores. Para mantener el material organizado, este repositorio restringe el acceso por carpeta mediante el archivo `CODEOWNERS` y los permisos asignados al equipo del curso.

### Políticas de permisos y edición

1. **Pertenencia al equipo:** formas parte de `Team_722_Teo1`, con permisos para subir cambios a la carpeta del ciclo vigente en la rama `main`.
2. **Restricción de rutas:** el archivo `.github/CODEOWNERS` protege los ciclos anteriores y el resto de carpetas del curso. Solo se permite modificar contenido dentro de la carpeta `Ejemplos/` del ciclo vigente.
3. **Descarga selectiva:** para evitar descargar carpetas pesadas de ciclos anteriores, usa siempre el flujo de sparse-checkout descrito a continuación.

## Flujo de trabajo paso a paso

1. Clona el repositorio sin descargar todo su contenido:

    ```bash
    git clone --no-checkout https://github.com/CococysLabs/722_Teoria-de-Sistemas-1.git
    cd 722_Teoria-de-Sistemas-1
    ```

2. Activa sparse-checkout en modo cono:

    ```bash
    git sparse-checkout init --cone
    ```

3. Indica la carpeta de ejemplos del ciclo vigente:

    ```bash
    git sparse-checkout set Ciclo-2026-Segundo-Semestre/Ejemplos
    ```

4. Descarga esa carpeta desde la rama `main`:

    ```bash
    git checkout main
    ```

5. Agrega tu código, guías o material didáctico dentro de:

    `Ciclo-2026-Segundo-Semestre/Ejemplos/`

6. Registra tus cambios con un commit descriptivo:

    ```bash
    git add .
    git commit -m "feat: agregar ejemplo de [DESCRIPCION] para el Segundo Semestre 2026"
    ```

7. Sube tus cambios a la rama `main`:

    ```bash
    git push origin main
    ```

    Nota: si el push modifica o elimina archivos fuera de `Ciclo-2026-Segundo-Semestre/Ejemplos/`, será rechazado por las reglas de propiedad definidas en `CODEOWNERS`.

## Estructura del repositorio

```text
722_Teoria-de-Sistemas-1/
├── .github/
│   └── CODEOWNERS                        (configuracion de permisos)
├── Ciclo-2024-Segundo-Semestre/           (protegido por CODEOWNERS)
├── Ciclo-2025-Primer-Semestre/            (protegido por CODEOWNERS)
└── Ciclo-2026-Segundo-Semestre/           (ciclo vigente)
    └── Ejemplos/                          (carpeta de trabajo del equipo del curso)
```

Nota: al cerrar el ciclo vigente, su carpeta se protegera agregandola a `CODEOWNERS`, siguiendo este mismo patron.

## Contacto

- Email: cococys@ingenieria.usac.edu.gt
- Organización: [CococysLabs](https://github.com/CococysLabs)
