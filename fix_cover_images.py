#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script para corregir las imágenes que no están cargando en index.html

import re
import os

def fix_cover_images():
    """
    Corrige las imágenes de portada en index.html usando los nombres reales de los archivos
    """
    index_file = "index.html"
    
    if not os.path.exists(index_file):
        print(f"❌ Error: No se encontró el archivo {index_file}")
        return
    
    # Leer el archivo
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mapeo correcto basado en los archivos reales existentes
    corrections = {
        # Nombres incorrectos → Nombres correctos (archivos que existen)
        "IA Generativa 2025 Deep Learning Revolution.jpg": "IA Generativa 2025 ChatGPT-5, Claude 4 y Gemini Ultra.jpg",
        "Next.js 15 Performance & App Router.png": "Next.js 15 App Router 2.0 - Framework Definitivo 2025.png",
        "CSS Grid y Flexbox Responsive Mastery.jpg": "CSS Grid y Flexbox Guía Completa 2025.jpg",
        "JavaScript ES6+ Modern Development.jpg": "JavaScript ES6+ AsyncAwait y Módulos Modernos.jpg",
        "Responsive Design Mobile First.jpg": "Mobile-First Design Estrategia Responsive 2025.jpg",
        "Node.js Full Stack Development.jpg": "Node.js Backend API REST desde Cero.jpg"
    }
    
    updates_count = 0
    
    # Aplicar correcciones
    for incorrect_name, correct_name in corrections.items():
        if incorrect_name in content:
            content = content.replace(f'assets/images/{incorrect_name}', f'assets/images/{correct_name}')
            updates_count += 1
            print(f"✓ Corregido: {incorrect_name}")
            print(f"  → {correct_name}")
    
    # Escribir el archivo corregido
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n🎉 Proceso completado: {updates_count}/6 imágenes corregidas en index.html")
    
    # Verificar qué imágenes están ahora en uso
    print("\n📋 Verificando imágenes en uso:")
    images_in_use = re.findall(r'assets/images/([^"]+\.(?:jpg|jpeg|png|gif))', content)
    unique_images = list(set(images_in_use))
    
    for img in unique_images:
        if img != "Logo1.png":  # Excluir el logo
            exists = os.path.exists(f"assets/images/{img}")
            status = "✅" if exists else "❌"
            print(f"{status} {img}")
    
    return updates_count > 0

if __name__ == "__main__":
    fix_cover_images()