import os
import re

# Directorio de artículos
articles_dir = r"c:\Users\angeh\Desktop\primera pagina\pages\articles"

# Mapeo de artículos con sus imágenes correspondientes
image_mapping = {
    "articulo-react-19-2025.html": "React 19 Server Components Revolution.png",
    "articulo-typescript-53-2025.html": "TypeScript 5.3 Decorators & Pattern Matching.jpg",
    "articulo-nextjs-15-2025.html": "Next.js 15 App Router 2.0 - Framework Definitivo 2025.png",
    "articulo-javascript-es6.html": "JavaScript ES6+ AsyncAwait y Módulos Modernos.jpg",
    "articulo-nodejs-principiantes.html": "Node.js Backend API REST desde Cero.jpg",
    "articulo-css-moderno.html": "CSS Grid y Flexbox Guía Completa 2025.jpg",
    "articulo-mobile-first.html": "Mobile-First Design Estrategia Responsive 2025.jpg",
    "articulo-ia-generativa-2025.html": "IA Generativa 2025 ChatGPT-5, Claude 4 y Gemini Ultra.jpg"
}

def update_article_image(filename, new_image):
    filepath = os.path.join(articles_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar y reemplazar la imagen
        # Patrón para encontrar la imagen en el artículo
        old_pattern = r'<img src="../../imagenes/[^"]*"'
        new_img_tag = f'<img src="../../assets/images/{new_image}"'
        
        # Reemplazar
        updated_content = re.sub(old_pattern, new_img_tag, content)
        
        # Escribir el archivo actualizado
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✓ Actualizado: {filename} -> {new_image}")
        return True
        
    except Exception as e:
        print(f"✗ Error en {filename}: {str(e)}")
        return False

print("Actualizando imágenes de artículos...\\n")

success_count = 0
for filename, image in image_mapping.items():
    if update_article_image(filename, image):
        success_count += 1

print(f"\\n{'='*60}")
print(f"Proceso completado: {success_count}/{len(image_mapping)} artículos actualizados")
print(f"{'='*60}")

# Mostrar el mapeo final
print("\\n📁 Imágenes asignadas:")
for filename, image in image_mapping.items():
    article_name = filename.replace("articulo-", "").replace(".html", "").replace("-", " ").title()
    print(f"  {article_name}: {image}")