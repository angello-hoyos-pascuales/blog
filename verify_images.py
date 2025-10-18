#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script para verificación final de imágenes

import os
import re

def verify_images():
    """
    Verifica que todas las imágenes referenciadas en index.html existen
    """
    # Leer index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Encontrar todas las imágenes referenciadas
    images = re.findall(r'assets/images/([^"]+\.(?:jpg|jpeg|png|gif))', content)
    unique_images = list(set(images))

    print('🔍 Verificación de imágenes en index.html:')
    print('=' * 50)

    missing_count = 0
    existing_count = 0

    for img in unique_images:
        if img != 'Logo1.png':  # Excluir el logo
            exists = os.path.exists(f'assets/images/{img}')
            status = '✅ EXISTE' if exists else '❌ FALTA'
            print(f'{status}: {img}')
            
            if exists:
                existing_count += 1
            else:
                missing_count += 1

    print(f'\n📊 Resumen:')
    print(f'   ✅ Imágenes existentes: {existing_count}')
    print(f'   ❌ Imágenes faltantes: {missing_count}')
    print(f'   📋 Total verificadas: {existing_count + missing_count}')
    
    if missing_count == 0:
        print('\n🎉 ¡Perfecto! Todas las imágenes están disponibles')
    else:
        print('\n⚠️  Hay imágenes que necesitan ser corregidas')

if __name__ == "__main__":
    verify_images()