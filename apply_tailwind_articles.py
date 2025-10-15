import os
import re
from pathlib import Path

# Template header con Tailwind
header_template = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Mi Blog</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        primary: '#3b82f6',
                        secondary: '#8b5cf6'
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-gray-50">
    <div class="min-h-screen">
        <!-- Navigation -->
        <nav class="fixed top-0 w-full bg-white/95 backdrop-blur-sm shadow-md z-50">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-20">
                    <div class="flex-shrink-0">
                        <a href="../../index.html" class="flex items-center gap-2">
                            <img src="../../assets/images/Logo1.png" alt="Logo" class="h-12 w-auto">
                            <span class="text-2xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">Mi Blog</span>
                        </a>
                    </div>
                    
                    <div class="hidden md:flex items-center gap-8">
                        <a href="../../index.html" class="text-gray-700 hover:text-primary transition-colors font-medium">Inicio</a>
                        <a href="../nosotros.html" class="text-gray-700 hover:text-primary transition-colors font-medium">Sobre Mí</a>
                        <a href="../servicios.html" class="text-gray-700 hover:text-primary transition-colors font-medium">Proyectos</a>
                        <a href="../noticias.html" class="text-gray-700 hover:text-primary transition-colors font-medium">Blog</a>
                        <a href="../contacto.html" class="text-gray-700 hover:text-primary transition-colors font-medium">Contacto</a>
                    </div>
                    
                    <button onclick="toggleMenu()" class="md:hidden p-2 rounded-lg hover:bg-gray-100 transition-colors">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
                
                <div id="mobile-menu" class="hidden md:hidden pb-4">
                    <a href="../../index.html" class="block py-2 text-gray-700 hover:text-primary transition-colors">Inicio</a>
                    <a href="../nosotros.html" class="block py-2 text-gray-700 hover:text-primary transition-colors">Sobre Mí</a>
                    <a href="../servicios.html" class="block py-2 text-gray-700 hover:text-primary transition-colors">Proyectos</a>
                    <a href="../noticias.html" class="block py-2 text-gray-700 hover:text-primary transition-colors">Blog</a>
                    <a href="../contacto.html" class="block py-2 text-gray-700 hover:text-primary transition-colors">Contacto</a>
                </div>
            </div>
        </nav>

        <!-- Article Content -->
        <article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-32 pb-16">
            <div class="bg-white rounded-2xl shadow-lg p-8 md:p-12">
'''

footer_template = '''
            </div>
            
            <!-- Back Button -->
            <div class="mt-8 text-center">
                <a href="../../index.html" class="inline-flex items-center gap-2 text-primary hover:text-secondary transition-colors font-semibold">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
                    </svg>
                    Volver al Blog
                </a>
            </div>
        </article>

        <!-- Footer -->
        <footer class="bg-gradient-to-r from-gray-900 via-gray-800 to-gray-900 text-white py-8 mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex flex-col md:flex-row items-center justify-between gap-4">
                    <p class="text-sm text-gray-300">
                        © 2025 <span class="text-primary font-semibold">Mi Blog de Programación</span>. Todos los derechos reservados.
                    </p>
                    <p class="text-sm text-gray-400">
                        Desarrollado con ❤️ por <span class="text-white font-semibold">angello</span>
                    </p>
                </div>
            </div>
        </footer>
    </div>
    
    <script>
        function toggleMenu() {{
            const mobileMenu = document.getElementById('mobile-menu');
            mobileMenu.classList.toggle('hidden');
        }}
    </script>
</body>
</html>
'''

# Directorio de artículos
articles_dir = Path('pages/articles')

# Procesar cada archivo HTML
for html_file in articles_dir.glob('articulo-*.html'):
    print(f"Procesando {html_file.name}...")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer título
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else html_file.stem.replace('-', ' ').title()
    title = title.replace(' - Mi Blog', '').strip()
    
    # Extraer contenido del body (todo después de header y antes de footer/script)
    # Buscar el contenido principal entre <main> o <article> tags
    body_content = content
    
    # Limpiar el contenido existente
    body_content = re.sub(r'<!DOCTYPE html>.*?<body[^>]*>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<header[^>]*>.*?</header>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<footer[^>]*>.*?</footer>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<script[^>]*>.*?</script>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'</body>.*?</html>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<div class="padre">|</div>\s*$', '', body_content)
    
    # Construir el nuevo HTML
    new_html = header_template.format(title=title) + body_content + footer_template
    
    # Escribir el archivo actualizado
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"✓ {html_file.name} actualizado con Tailwind CSS")

print("\n✅ Todos los artículos han sido actualizados con Tailwind CSS")
