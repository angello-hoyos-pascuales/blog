#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script para optimizar y actualizar completamente las portadas del blog

import re
import os

def optimize_blog_covers():
    """
    Optimiza y actualiza las portadas del blog con las mejores imágenes disponibles
    """
    index_file = "index.html"
    
    if not os.path.exists(index_file):
        print(f"❌ Error: No se encontró el archivo {index_file}")
        return
    
    # Leer el archivo
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Lista de imágenes disponibles (excluyendo las genéricas)
    available_images = []
    for file in os.listdir('assets/images'):
        if file.endswith(('.jpg', '.png', '.jpeg')) and not file in ['2.jpg', '4.jpg', '5.jpg', '6.jpg', 'Logo1.png']:
            available_images.append(file)
    
    print("🖼️  Imágenes específicas disponibles:")
    for i, img in enumerate(available_images, 1):
        print(f"{i}. {img}")
    
    # Mapeo mejorado para asegurar que cada artículo tenga la imagen más apropiada
    article_image_mapping = {
        "IA Generativa 2025": "IA Generativa 2025 ChatGPT-5, Claude 4 y Gemini Ultra.jpg",
        "React 19": "React 19 Server Components Revolution.png",
        "Next.js 15": "Next.js 15 App Router 2.0 - Framework Definitivo 2025.png",
        "TypeScript 5.3": "TypeScript 5.3 Decorators & Pattern Matching.jpg",
        "CSS Grid y Flexbox": "CSS Grid y Flexbox Guía Completa 2025.jpg",
        "JavaScript ES6+": "JavaScript ES6+ AsyncAwait y Módulos Modernos.jpg",
        "Responsive Design": "Mobile-First Design Estrategia Responsive 2025.jpg",
        "Node.js": "Node.js Backend API REST desde Cero.jpg"
    }
    
    updates_count = 0
    
    # Verificar y actualizar cada imagen si es necesario
    for title, image_name in article_image_mapping.items():
        # Verificar si la imagen existe
        if os.path.exists(f'assets/images/{image_name}'):
            # Buscar el patrón en el HTML
            pattern = rf'(<img\s+src="assets/images/[^"]+"\s+alt="{re.escape(title)}"[^>]*>)'
            
            def replace_if_needed(match):
                nonlocal updates_count
                full_tag = match.group(1)
                current_src = re.search(r'src="([^"]*)"', full_tag)
                if current_src:
                    current_image = current_src.group(1)
                    expected_src = f"assets/images/{image_name}"
                    
                    if current_image != expected_src:
                        new_tag = re.sub(r'src="[^"]*"', f'src="{expected_src}"', full_tag)
                        updates_count += 1
                        print(f"✓ Actualizado: {title}")
                        print(f"  {current_image} → {expected_src}")
                        return new_tag
                    else:
                        print(f"✅ Correcto: {title} → {image_name}")
                
                return full_tag
            
            content = re.sub(pattern, replace_if_needed, content)
        else:
            print(f"⚠️  Imagen faltante: {image_name}")
    
    # Actualizar artículos populares con las mejores imágenes
    popular_updates = [
        ("Popular 1", "React 19 Server Components Revolution.png"),
        ("Popular 2", "IA Generativa 2025 ChatGPT-5, Claude 4 y Gemini Ultra.jpg")
    ]
    
    for alt_text, image_name in popular_updates:
        pattern = rf'(<img\s+src="assets/images/[^"]+"\s+alt="{alt_text}"[^>]*>)'
        expected_src = f"assets/images/{image_name}"
        
        def update_popular(match):
            nonlocal updates_count
            full_tag = match.group(1)
            current_src = re.search(r'src="([^"]*)"', full_tag)
            if current_src and current_src.group(1) != expected_src:
                new_tag = re.sub(r'src="[^"]*"', f'src="{expected_src}"', full_tag)
                updates_count += 1
                print(f"✓ Actualizado: {alt_text} → {image_name}")
                return new_tag
            return full_tag
        
        content = re.sub(pattern, update_popular, content)
    
    # Escribir el archivo actualizado si hubo cambios
    if updates_count > 0:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n🎉 Proceso completado: {updates_count} actualizaciones aplicadas")
    else:
        print(f"\n✅ No se necesitaron cambios: Todas las portadas ya están optimizadas")
    
    # Verificación final
    print(f"\n🔍 Verificación final:")
    images_in_use = re.findall(r'assets/images/([^"]+\.(?:jpg|jpeg|png|gif))', content)
    blog_images = [img for img in set(images_in_use) if img != 'Logo1.png']
    
    for img in blog_images:
        exists = os.path.exists(f"assets/images/{img}")
        status = "✅" if exists else "❌"
        print(f"{status} {img}")
    
    return updates_count > 0

if __name__ == "__main__":
    optimize_blog_covers()