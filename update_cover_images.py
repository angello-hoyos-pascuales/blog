#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script para actualizar las imágenes de portada en index.html

import re
import os

# Mapeo de títulos de artículos a nombres de archivos de imagen
image_mapping = {
    "IA Generativa 2025": "IA Generativa 2025 Deep Learning Revolution.jpg",
    "React 19": "React 19 Server Components Revolution.png",
    "Next.js 15": "Next.js 15 Performance & App Router.png",
    "TypeScript 5.3": "TypeScript 5.3 Decorators & Pattern Matching.jpg",
    "CSS Grid y Flexbox": "CSS Grid y Flexbox Responsive Mastery.jpg",
    "JavaScript ES6+": "JavaScript ES6+ Modern Development.jpg",
    "Responsive Design": "Responsive Design Mobile First.jpg",
    "Node.js": "Node.js Full Stack Development.jpg"
}

def update_index_images():
    """
    Actualiza las imágenes en index.html basándose en los títulos de los artículos
    """
    index_file = "index.html"
    
    if not os.path.exists(index_file):
        print(f"❌ Error: No se encontró el archivo {index_file}")
        return
    
    # Leer el archivo
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Contador de actualizaciones
    updates_count = 0
    
    # Actualizar cada imagen basándose en el alt text
    for title, image_name in image_mapping.items():
        # Buscar el patrón: <img src="assets/images/X.jpg" alt="TITULO"
        pattern = rf'(<img\s+src="assets/images/[^"]+"\s+alt="{re.escape(title)}"[^>]*>)'
        
        def replace_src(match):
            nonlocal updates_count
            # Extraer el tag completo
            full_tag = match.group(1)
            # Reemplazar solo el src manteniendo todo lo demás
            new_tag = re.sub(r'src="assets/images/[^"]*"', f'src="assets/images/{image_name}"', full_tag)
            updates_count += 1
            print(f"✓ Actualizado: {title} -> {image_name}")
            return new_tag
        
        content = re.sub(pattern, replace_src, content)
    
    # También actualizar las imágenes populares (opcional)
    # Usar las mismas imágenes para la sección de populares
    popular_images = ["React 19 Server Components Revolution.png", "IA Generativa 2025 Deep Learning Revolution.jpg"]
    
    # Actualizar Popular 1
    content = re.sub(
        r'(<img\s+src="assets/images/[^"]+"\s+alt="Popular 1"[^>]*>)',
        f'<img src="assets/images/{popular_images[0]}" alt="Popular 1" class="w-20 h-20 object-cover rounded-lg group-hover:scale-105 transition-transform">',
        content
    )
    
    # Actualizar Popular 2
    content = re.sub(
        r'(<img\s+src="assets/images/[^"]+"\s+alt="Popular 2"[^>]*>)',
        f'<img src="assets/images/{popular_images[1]}" alt="Popular 2" class="w-20 h-20 object-cover rounded-lg group-hover:scale-105 transition-transform">',
        content
    )
    
    updates_count += 2  # Por las dos imágenes populares
    print(f"✓ Actualizado: Artículos Populares -> {popular_images}")
    
    # Escribir el archivo actualizado
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n🎉 Proceso completado: {updates_count}/10 imágenes actualizadas en index.html")
    print("✅ Las imágenes de portada han sido actualizadas con las nuevas imágenes específicas")

if __name__ == "__main__":
    update_index_images()