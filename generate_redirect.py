#!/usr/bin/env python3
"""
Generador de páginas de redirección para GitHub Pages
Uso: python generate_redirect.py --name "promo-feb" --url "https://destino.com/oferta"
"""
import argparse
import os
from pathlib import Path

TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0;url={destination_url}">
    <meta name="robots" content="noindex, nofollow">
    <title>Redirigiendo...</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: #f4f4f4;
        }}
        .loader {{
            text-align: center;
        }}
        .spinner {{
            border: 4px solid #f3f3f3;
            border-top: 4px solid #0366d6;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
    </style>
</head>
<body>
    <div class="loader">
        <div class="spinner"></div>
        <p>Redirigiendo...</p>
        <p style="font-size: 12px; color: #666;">Si no eres redirigido automáticamente, 
           <a href="{destination_url}">haz clic aquí</a>
        </p>
    </div>
    
    <script>
        // Redirect inmediato por JavaScript (backup del meta refresh)
        window.location.href = '{destination_url}';
    </script>
</body>
</html>
"""

def generate_redirect(name, url, output_dir='.'):
    """Genera un archivo HTML de redirección"""
    
    # Sanitizar nombre de archivo
    filename = name.lower().replace(' ', '-').replace('_', '-')
    if not filename.endswith('.html'):
        filename += '.html'
    
    filepath = Path(output_dir) / filename
    
    # Generar contenido
    content = TEMPLATE.format(destination_url=url)
    
    # Escribir archivo
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Redirect creado: {filepath}")
    print(f"📍 URL destino: {url}")
    print(f"\n🔗 Para usar en email:")
    print(f"   https://TU-USUARIO.github.io/links/{filename}")
    print(f"\n📝 Próximos pasos:")
    print(f"   git add {filename}")
    print(f"   git commit -m 'Add {filename} redirect'")
    print(f"   git push")
    
    return filepath

def main():
    parser = argparse.ArgumentParser(
        description='Genera archivos HTML de redirección para GitHub Pages'
    )
    parser.add_argument('--name', '-n', required=True,
                        help='Nombre del redirect (ej: promo-feb, bbva-tarjeta)')
    parser.add_argument('--url', '-u', required=True,
                        help='URL de destino (ej: https://afiliacion.com/oferta)')
    parser.add_argument('--output', '-o', default='.',
                        help='Directorio de salida (default: directorio actual)')
    
    args = parser.parse_args()
    
    # Validar URL
    if not args.url.startswith(('http://', 'https://')):
        print("❌ Error: La URL debe comenzar con http:// o https://")
        return 1
    
    # Generar redirect
    generate_redirect(args.name, args.url, args.output)
    
    return 0

if __name__ == '__main__':
    exit(main())
