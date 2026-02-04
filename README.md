# GitHub Pages Redirect System

Sistema de redirección de links para emails usando GitHub Pages (github.io).

## Setup Inicial (5 minutos)

### 1. Crear Repositorio en GitHub

```bash
# Opción A: Desde web
1. Ir a https://github.com/new
2. Nombre: links (o tracking-links, email-links, etc.)
3. Público ✅
4. Initialize with README ❌ (lo haremos nosotros)
5. Create repository

# Opción B: Desde CLI
gh repo create links --public --source=. --remote=origin
```

### 2. Configurar Git Local

```bash
cd github-redirect
git init
git add .
git commit -m "Initial commit - redirect system"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/links.git
git push -u origin main
```

### 3. Activar GitHub Pages

```
1. Ir a Settings → Pages
2. Source: Deploy from a branch
3. Branch: main / (root)
4. Save
```

**URLs disponibles en 1-2 minutos:**
```
https://TU-USUARIO.github.io/links/bbva.html
https://TU-USUARIO.github.io/links/tarjeta.html
```

## Estructura de Archivos

```
github-redirect/
├── README.md              # Este archivo
├── index.html             # Página principal
├── bbva.html             # Redirect ejemplo: BBVA
├── tarjeta.html          # Redirect ejemplo: Tarjeta
├── unsubscribe.html      # Redirect ejemplo: Baja
└── generate_redirect.py  # Script para generar nuevos redirects
```

## Uso en Emails

### Antes (rechazado por Gmail):
```html
<a href="https://tinyurl.com/abc123">Click aquí</a>
```

### Ahora (aprobado):
```html
<a href="https://TU-USUARIO.github.io/links/bbva.html">Solicita tu tarjeta BBVA</a>
```

## Generar Nuevos Redirects

```bash
# Opción 1: Manual
cp bbva.html nuevo-link.html
# Editar URL destino en nuevo-link.html

# Opción 2: Con script
python generate_redirect.py --name "promo-feb" --url "https://afiliacion.com/promo"
git add promo-feb.html
git commit -m "Add promo-feb redirect"
git push
```

## Tracking y Analytics

Para agregar tracking, modifica la URL destino:

```html
<meta http-equiv="refresh" content="0;url=https://destino.com?utm_source=email&utm_medium=github&utm_campaign=bbva">
```

## Ventajas

✅ Dominio github.io tiene excelente reputación en Gmail  
✅ SSL incluido (HTTPS automático)  
✅ Gratis e ilimitado  
✅ Fácil de mantener (solo HTML estático)  
✅ Sin límite de redirects  
✅ Sin tarjeta de crédito requerida  

## Mantenimiento

```bash
# Actualizar URL destino
vim bbva.html  # Cambiar URL
git commit -am "Update BBVA link"
git push

# Agregar nuevo redirect
cp bbva.html nueva-oferta.html
vim nueva-oferta.html  # Cambiar URL
git add nueva-oferta.html
git commit -m "Add nueva-oferta redirect"
git push
```

## Mejores Prácticas

1. **Nombres descriptivos:** `tarjeta-bbva.html` mejor que `r1.html`
2. **Organizar por campaña:** `feb2026-bbva.html`
3. **Agregar parámetros UTM:** Para tracking en destino
4. **Usar delay=0:** Para redirección instantánea
5. **Texto alternativo:** Por si JavaScript está deshabilitado

## Troubleshooting

**404 Not Found después de push:**
- Esperar 1-2 minutos para propagación
- Verificar que GitHub Pages está activado
- URL correcta: `https://USUARIO.github.io/REPO/archivo.html`

**Redirect muy lento:**
- Normal: 0.5-1 segundo
- Si >3 segundos, verificar URL destino

**Gmail sigue bloqueando:**
- Verificar que URL destino no está en blacklist
- Evitar múltiples redirects encadenados
- Usar delay="0" en meta refresh
