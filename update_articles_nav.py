import os
import re

# Directorio de artículos
articles_dir = r"c:\Users\angeh\Desktop\primera pagina\pages\articles"

# Nueva navegación con Tailwind CSS
new_nav = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TITLE_PLACEHOLDER</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#3b82f6',
                        secondary: '#8b5cf6',
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-gray-50">
    <!-- Navegación -->
    <nav class="bg-white shadow-lg fixed w-full top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Logo -->
                <div class="flex items-center space-x-3">
                    <a href="../../index.html">
                        <img src="../../imagenes/Logo1.png" alt="Logo" class="h-12 w-12 rounded-full">
                    </a>
                    <a href="../../index.html">
                        <span class="text-2xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">Mi Blog</span>
                    </a>
                </div>
                
                <!-- Menú Desktop -->
                <div class="hidden md:flex items-center space-x-8">
                    <a href="../../index.html" class="text-gray-700 hover:text-primary transition-colors duration-300 font-medium">Inicio</a>
                    <a href="../nosotros.html" class="text-gray-700 hover:text-primary transition-colors duration-300 font-medium">Sobre Mí</a>
                    <a href="../servicios.html" class="text-gray-700 hover:text-primary transition-colors duration-300 font-medium">Proyectos</a>
                    <a href="../noticias.html" class="text-gray-700 hover:text-primary transition-colors duration-300 font-medium">Blog</a>
                    <a href="../contacto.html" class="bg-gradient-to-r from-primary to-secondary text-white px-6 py-2 rounded-full hover:shadow-lg transition-all duration-300">Contacto</a>
                </div>
                
                <!-- Botón menú móvil -->
                <button class="md:hidden text-gray-700" onclick="toggleMenu()">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
            
            <!-- Menú móvil -->
            <div id="mobile-menu" class="hidden md:hidden pb-4">
                <a href="../../index.html" class="block py-2 text-gray-700 hover:text-primary transition-colors duration-300">Inicio</a>
                <a href="../nosotros.html" class="block py-2 text-gray-700 hover:text-primary transition-colors duration-300">Sobre Mí</a>
                <a href="../servicios.html" class="block py-2 text-gray-700 hover:text-primary transition-colors duration-300">Proyectos</a>
                <a href="../noticias.html" class="block py-2 text-gray-700 hover:text-primary transition-colors duration-300">Blog</a>
                <a href="../contacto.html" class="block py-2 text-gray-700 hover:text-primary transition-colors duration-300">Contacto</a>
            </div>
        </div>
    </nav>

    <!-- Espaciador para el nav fijo -->
    <div class="h-20"></div>
'''

# Función para actualizar cada archivo
def update_article(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraer el título
        title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        title = title_match.group(1) if title_match else "Artículo - Mi Blog"
        
        # Encontrar dónde termina el header y empieza el main
        main_match = re.search(r'<main[^>]*>', content, re.DOTALL)
        
        if main_match:
            # Extraer todo desde <main> hasta el final
            main_and_rest = content[main_match.start():]
            
            # Crear el nuevo contenido
            new_content = new_nav.replace('TITLE_PLACEHOLDER', title) + '\n' + main_and_rest
            
            # Guardar el archivo actualizado
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Actualizado: {os.path.basename(filepath)}")
            return True
        else:
            print(f"✗ No se encontró <main> en: {os.path.basename(filepath)}")
            return False
            
    except Exception as e:
        print(f"✗ Error en {os.path.basename(filepath)}: {str(e)}")
        return False

# Procesar todos los archivos HTML en el directorio de artículos
print("Actualizando navegación de artículos con Tailwind CSS...\n")

success_count = 0
total_count = 0

for filename in os.listdir(articles_dir):
    if filename.endswith('.html') and not filename.endswith('.bak'):
        filepath = os.path.join(articles_dir, filename)
        total_count += 1
        if update_article(filepath):
            success_count += 1

print(f"\n{'='*50}")
print(f"Proceso completado: {success_count}/{total_count} artículos actualizados")
print(f"{'='*50}")
