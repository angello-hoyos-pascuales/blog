#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script para actualizar las portadas en noticias.html

import re
import os

def update_noticias_covers():
    """
    Actualiza las portadas en la página de noticias con imágenes específicas
    """
    noticias_file = "pages/noticias.html"
    
    if not os.path.exists(noticias_file):
        print(f"❌ Error: No se encontró el archivo {noticias_file}")
        return
    
    # Leer el archivo
    with open(noticias_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mapeo de artículos basado en el contenido y títulos
    article_mappings = [
        # Artículo Principal - Las Nuevas Tendencias en Desarrollo Web 2025
        {
            "old_src": "../assets/images/4.jpg",
            "new_src": "../assets/images/Las Nuevas Tendencias en Desarrollo Web 2025.jpg",
            "alt": "Noticia Principal",
            "title": "Las Nuevas Tendencias en Desarrollo Web 2025"
        },
        # CSS Grid vs Flexbox
        {
            "old_src": "../assets/images/5.jpg", 
            "new_src": "../assets/images/CSS Grid y Flexbox Guía Completa 2025.jpg",
            "alt": "CSS Grid",
            "title": "CSS Grid vs Flexbox"
        },
        # JavaScript ES2024
        {
            "old_src": "../assets/images/4.jpg",
            "new_src": "../assets/images/JavaScript ES6+ AsyncAwait y Módulos Modernos.jpg", 
            "alt": "JavaScript",
            "title": "Nuevas características de ES2024"
        },
        # Performance - usando Next.js como imagen de performance
        {
            "old_src": "../assets/images/5.jpg",
            "new_src": "../assets/images/Next.js 15 App Router 2.0 - Framework Definitivo 2025.png",
            "alt": "Performance", 
            "title": "Optimización de rendimiento web"
        },
        # UX Design - usando TypeScript como imagen técnica
        {
            "old_src": "../assets/images/4.jpg",
            "new_src": "../assets/images/TypeScript 5.3 Decorators & Pattern Matching.jpg",
            "alt": "UX Design",
            "title": "Principios de diseño UX para 2025"
        },
        # Mobile First
        {
            "old_src": "../assets/images/5.jpg",
            "new_src": "../assets/images/Mobile-First Design Estrategia Responsive 2025.jpg",
            "alt": "Mobile First",
            "title": "Desarrollo Mobile-First en 2025"
        },
        # AI y Web  
        {
            "old_src": "../assets/images/4.jpg",
            "new_src": "../assets/images/IA Generativa 2025 ChatGPT-5, Claude 4 y Gemini Ultra.jpg",
            "alt": "AI y Web",
            "title": "IA en el desarrollo web"
        }
    ]
    
    updates_count = 0
    
    # Procesar cada artículo
    for mapping in article_mappings:
        old_src = mapping["old_src"]
        new_src = mapping["new_src"] 
        alt_text = mapping["alt"]
        title = mapping["title"]
        
        # Verificar si el archivo de imagen existe
        image_path = new_src.replace("../assets/images/", "assets/images/")
        if os.path.exists(image_path):
            # Buscar y reemplazar la imagen específica por contexto
            # Usar una búsqueda más específica basada en el alt text
            pattern = rf'<img\s+src="{re.escape(old_src)}"\s+alt="{re.escape(alt_text)}"([^>]*)>'
            replacement = f'<img src="{new_src}" alt="{alt_text}"\\1>'
            
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content, count=1)
                updates_count += 1
                print(f"✓ Actualizado: {title}")
                print(f"  {old_src} → {new_src}")
            else:
                print(f"⚠️  No encontrado: {alt_text}")
        else:
            print(f"❌ Imagen no existe: {image_path}")
    
    # Actualizar imágenes populares en sidebar
    popular_mappings = [
        ("Popular 1", "../assets/images/React 19 Server Components Revolution.png"),
        ("Popular 2", "../assets/images/IA Generativa 2025 ChatGPT-5, Claude 4 y Gemini Ultra.jpg"),
        ("Popular 3", "../assets/images/TypeScript 5.3 Decorators & Pattern Matching.jpg")
    ]
    
    for alt_text, new_image in popular_mappings:
        pattern = rf'<img\s+src="../assets/images/[^"]+"\s+alt="{re.escape(alt_text)}"([^>]*)>'
        replacement = f'<img src="{new_image}" alt="{alt_text}"\\1>'
        
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1) 
            updates_count += 1
            print(f"✓ Actualizado: {alt_text} → {new_image.split('/')[-1]}")
    
    # Escribir el archivo actualizado
    with open(noticias_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n🎉 Proceso completado: {updates_count} imágenes actualizadas en noticias.html")
    
    # Verificación final
    print(f"\n🔍 Verificación final:")
    remaining_generic = len(re.findall(r'\.\./assets/images/[45]\.jpg', content))
    print(f"   📋 Imágenes genéricas restantes: {remaining_generic}")
    
    if remaining_generic == 0:
        print("   ✅ ¡Perfecto! Todas las imágenes genéricas fueron reemplazadas")
    else:
        print("   ⚠️  Aún quedan algunas imágenes genéricas por actualizar")
    
    return updates_count > 0

if __name__ == "__main__":
    update_noticias_covers()