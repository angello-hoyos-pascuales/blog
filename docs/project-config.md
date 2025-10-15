# Project Configuration

## Estructura Final del Proyecto

```
primera-pagina/
├── assets/
│   ├── images/          # Todas las imágenes del sitio
│   ├── fonts/           # Fuentes personalizadas
│   └── icons/           # Iconos del proyecto
├── styles/              # CSS modular
│   ├── main.css        # Archivo principal que importa todos
│   ├── base.css        # Variables, reset, utilidades
│   ├── navigation.css  # Header, nav, menú
│   ├── blog.css        # Tarjetas, grid, blog principal  
│   ├── articles.css    # Páginas de artículos individuales
│   └── responsive.css  # Media queries y responsive
├── pages/               # Páginas del sitio
│   ├── articles/       # Artículos del blog
│   ├── nosotros.html
│   ├── servicios.html
│   ├── noticias.html
│   └── contacto.html
├── docs/                # Documentación
│   └── style-guide.css # Guía de estilos y componentes
├── scripts/             # JavaScript y utilidades
│   └── server.js       # Servidor de desarrollo
├── index.html          # Página principal
└── README.md           # Documentación principal
```

## URLs y Rutas

### Páginas Principales
- `/` - Homepage/Blog principal
- `/pages/nosotros.html` - Sobre mí  
- `/pages/servicios.html` - Proyectos/Portfolio
- `/pages/noticias.html` - Blog/Noticias
- `/pages/contacto.html` - Contacto

### Artículos
- `/pages/articles/articulo-ia-generativa-2025.html`
- `/pages/articles/articulo-react-19-2025.html`
- `/pages/articles/articulo-nextjs-15-2025.html`
- `/pages/articles/articulo-typescript-53-2025.html`
- `/pages/articles/[otros-articulos].html`

### Recursos
- `/assets/images/` - Imágenes
- `/styles/main.css` - CSS principal
- `/docs/style-guide.css` - Guía de estilos

## Comandos Útiles

### Servidor de Desarrollo
```bash
# Python 3
python -m http.server 8080

# Node.js (si tienes http-server instalado)
npx http-server -p 8080

# PHP
php -S localhost:8080
```

### Build y Deploy
- No requiere build - HTML/CSS/JS vanilla
- Subir directamente a hosting estático
- Compatible con GitHub Pages, Netlify, Vercel

## Configuración de IDE

### VS Code Extensions Recomendadas
- HTML CSS Support
- Auto Rename Tag  
- Prettier
- Live Server
- CSS Peek

### Configuración de Prettier
```json
{
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "semi": true,
  "singleQuote": true,
  "quoteProps": "as-needed",
  "trailingComma": "es5"
}
```