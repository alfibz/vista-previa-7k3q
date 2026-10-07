# Adripsykcare – web estática

Sitio de www.adripsykcare.com / www.adripsykcare.se, como sitio estático propio, sin marcos (frameset).

- `build.py` – contiene todos los textos y genera el sitio en `docs/` (`python3 build.py`).
- `docs/` – el sitio publicado (GitHub Pages → rama `main`, carpeta `/docs`).
- Para cambiar un texto: editar `build.py`, ejecutar `python3 build.py`, hacer commit y push.

## Puesta en marcha con dominio propio (cuando se valide)

0. En `build.py` poner `PREVIEW = False` (quita el bloqueo a buscadores) y regenerar.

1. GitHub → Settings → Pages → Custom domain: `www.adripsykcare.com` → activar *Enforce HTTPS*.
2. En Loopia, quitar el reenvío enmascarado de ambos dominios y poner los DNS:
   - `www` → CNAME `<usuario>.github.io`
   - `@` (raíz) → registros A: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - adripsykcare.se: reenvío 301 normal (sin enmascarar) a https://www.adripsykcare.com
3. Dar de alta el sitio en Google Search Console y enviar `sitemap.xml`.
