import os
import re

articles_dir = r"c:\Users\angeh\Desktop\primera pagina\pages\articles"

# Contenido para los artículos restantes
remaining_articles = {
    "articulo-nextjs-15-2025.html": """
    <main class="bg-gray-50 py-12">
        <div class="max-w-4xl mx-auto px-4">
            <article class="bg-white rounded-2xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-green-600 to-teal-600 p-8 text-white">
                    <div class="flex items-center space-x-2 text-sm mb-4">
                        <a href="../../index.html" class="hover:underline">Inicio</a>
                        <span>›</span>
                        <a href="../noticias.html" class="hover:underline">Blog</a>
                        <span>›</span>
                        <span>Next.js 15</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold mb-4">Next.js 15: Guía Completa del Framework</h1>
                    <div class="flex items-center space-x-4 text-sm">
                        <span>📅 15 de Octubre, 2025</span>
                        <span>⏱️ 18 min lectura</span>
                    </div>
                </div>

                <div class="relative h-96 overflow-hidden">
                    <img src="../../imagenes/4.jpg" alt="Next.js 15" class="w-full h-full object-cover">
                </div>

                <div class="p-8 md:p-12">
                    <div class="bg-green-50 border-l-4 border-green-600 p-6 rounded-r-lg mb-8">
                        <p class="text-lg leading-relaxed text-gray-700">
                            <strong>Next.js 15</strong> revoluciona el desarrollo React con Turbopack, App Router 2.0 
                            y optimizaciones automáticas que mejoran el rendimiento hasta 4x comparado con versiones anteriores.
                        </p>
                    </div>

                    <div class="bg-gray-50 p-6 rounded-xl mb-8">
                        <h2 class="text-2xl font-bold mb-4">📋 Contenido</h2>
                        <ul class="space-y-2">
                            <li><a href="#turbopack" class="text-green-600 hover:underline">1. Turbopack: El Nuevo Bundler</a></li>
                            <li><a href="#app-router" class="text-green-600 hover:underline">2. App Router 2.0</a></li>
                            <li><a href="#server-actions" class="text-green-600 hover:underline">3. Server Actions</a></li>
                            <li><a href="#optimizaciones" class="text-green-600 hover:underline">4. Optimizaciones Automáticas</a></li>
                            <li><a href="#proyecto" class="text-green-600 hover:underline">5. Crear tu Primer Proyecto</a></li>
                        </ul>
                    </div>

                    <section id="turbopack" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🚀 Turbopack: Compilación Ultra Rápida</h2>
                        <p class="text-lg mb-6 text-gray-700">
                            Turbopack, escrito en Rust, es 700x más rápido que Webpack y 10x más rápido que Vite en proyectos grandes.
                        </p>

                        <div class="grid md:grid-cols-3 gap-6 mb-8">
                            <div class="bg-blue-50 p-6 rounded-xl text-center">
                                <div class="text-4xl font-bold text-blue-600 mb-2">700x</div>
                                <p class="text-gray-700">Más rápido que Webpack</p>
                            </div>
                            <div class="bg-purple-50 p-6 rounded-xl text-center">
                                <div class="text-4xl font-bold text-purple-600 mb-2">10x</div>
                                <p class="text-gray-700">Más rápido que Vite</p>
                            </div>
                            <div class="bg-green-50 p-6 rounded-xl text-center">
                                <div class="text-4xl font-bold text-green-600 mb-2">&lt;50ms</div>
                                <p class="text-gray-700">Hot Module Reload</p>
                            </div>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">⚙️ Configuración</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl overflow-x-auto mb-6">
                            <pre class="text-sm"><code>// next.config.js
module.exports = {
  // Turbopack activado por defecto en Next.js 15
  experimental: {
    turbo: {
      rules: {
        '*.svg': {
          loaders: ['@svgr/webpack'],
          as: '*.js'
        }
      }
    }
  }
}</code></pre>
                        </div>
                    </section>

                    <section id="app-router" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📁 App Router 2.0: Estructura Moderna</h2>
                        <p class="text-lg mb-6 text-gray-700">
                            App Router introduce un nuevo sistema de rutas basado en carpetas con soporte nativo para layouts,
                            loading states y error boundaries.
                        </p>

                        <h3 class="text-2xl font-bold mb-4">🏗️ Estructura de Carpetas</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>app/
├── layout.tsx          # Layout raíz
├── page.tsx           # Página de inicio
├── loading.tsx        # Loading UI
├── error.tsx          # Error handling
├── not-found.tsx      # 404 page
└── blog/
    ├── layout.tsx     # Layout del blog
    ├── page.tsx       # Lista de posts
    └── [slug]/
        └── page.tsx   # Post individual</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">📄 Ejemplo de Layout</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// app/layout.tsx
export default function RootLayout({
  children
}: {
  children: React.ReactNode
}) {
  return (
    &lt;html lang="es"&gt;
      &lt;body&gt;
        &lt;nav&gt;Mi Navegación&lt;/nav&gt;
        &lt;main&gt;{children}&lt;/main&gt;
        &lt;footer&gt;Mi Footer&lt;/footer&gt;
      &lt;/body&gt;
    &lt;/html&gt;
  )
}</code></pre>
                        </div>
                    </section>

                    <section id="server-actions" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🔄 Server Actions: Mutaciones Simples</h2>
                        <p class="text-lg mb-6 text-gray-700">
                            Server Actions permiten ejecutar código del servidor directamente desde componentes del cliente 
                            sin necesidad de crear APIs REST.
                        </p>

                        <h3 class="text-2xl font-bold mb-4">Ejemplo Completo</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// app/actions.ts
'use server'

import { db } from '@/lib/database'
import { revalidatePath } from 'next/cache'

export async function createPost(formData: FormData) {
  const title = formData.get('title') as string
  const content = formData.get('content') as string

  await db.post.create({
    data: { title, content, published: true }
  })

  revalidatePath('/blog')
  return { success: true }
}

// app/blog/nuevo/page.tsx
'use client'
import { createPost } from '@/app/actions'

export default function NuevoPost() {
  return (
    &lt;form action={createPost}&gt;
      &lt;input name="title" placeholder="Título" required /&gt;
      &lt;textarea name="content" placeholder="Contenido" required /&gt;
      &lt;button type="submit"&gt;Publicar&lt;/button&gt;
    &lt;/form&gt;
  )
}</code></pre>
                        </div>
                    </section>

                    <section id="optimizaciones" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">⚡ Optimizaciones Automáticas</h2>
                        
                        <div class="space-y-6">
                            <div class="bg-blue-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-blue-900">🖼️ Optimización de Imágenes</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>import Image from 'next/image'

&lt;Image
  src="/foto.jpg"
  alt="Foto"
  width={800}
  height={600}
  priority // Para imágenes above the fold
/&gt;</code></pre>
                                </div>
                            </div>

                            <div class="bg-purple-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-purple-900">🔤 Optimización de Fuentes</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({ children }) {
  return (
    &lt;html className={inter.className}&gt;
      &lt;body&gt;{children}&lt;/body&gt;
    &lt;/html&gt;
  )
}</code></pre>
                                </div>
                            </div>

                            <div class="bg-green-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-green-900">📦 Code Splitting Automático</h3>
                                <p class="text-gray-700">Next.js divide el código automáticamente por ruta, cargando solo lo necesario.</p>
                            </div>
                        </div>
                    </section>

                    <section id="proyecto" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🛠️ Crear tu Primer Proyecto</h2>
                        
                        <div class="space-y-6">
                            <div class="bg-gray-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3">Paso 1: Crear el Proyecto</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>npx create-next-app@latest mi-app
cd mi-app
npm run dev</code></pre>
                                </div>
                            </div>

                            <div class="bg-gray-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3">Paso 2: Configurar Base de Datos</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>npm install prisma @prisma/client
npx prisma init
npx prisma migrate dev</code></pre>
                                </div>
                            </div>

                            <div class="bg-gray-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3">Paso 3: Deploy en Vercel</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>npm install -g vercel
vercel</code></pre>
                                </div>
                            </div>
                        </div>
                    </section>

                    <div class="bg-gradient-to-r from-green-600 to-teal-600 p-8 rounded-xl text-white mt-12">
                        <h2 class="text-2xl font-bold mb-4">🎯 Conclusión</h2>
                        <p class="text-lg leading-relaxed">
                            Next.js 15 es el framework más completo para React. Con Turbopack, App Router y optimizaciones 
                            automáticas, crear aplicaciones web profesionales nunca fue tan fácil y rápido.
                        </p>
                    </div>

                    <div class="flex justify-between items-center mt-12 pt-8 border-t">
                        <a href="articulo-nodejs-principiantes.html" class="text-green-600 hover:underline">← Node.js</a>
                        <a href="../noticias.html" class="text-gray-600 hover:text-green-600">Ver todos</a>
                        <a href="articulo-react-19-2025.html" class="text-green-600 hover:underline">React 19 →</a>
                    </div>
                </div>
            </article>
        </div>
    </main>

    <footer class="bg-gray-900 text-white py-12 mt-20">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <p class="text-gray-400">© 2025 Mi Blog. Todos los derechos reservados.</p>
        </div>
    </footer>

    <script>
        function toggleMenu() {
            document.getElementById('mobile-menu').classList.toggle('hidden');
        }
    </script>
</body>
</html>
""",

    "articulo-javascript-es6.html": """
    <main class="bg-gray-50 py-12">
        <div class="max-w-4xl mx-auto px-4">
            <article class="bg-white rounded-2xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-yellow-500 to-orange-500 p-8 text-white">
                    <div class="flex items-center space-x-2 text-sm mb-4">
                        <a href="../../index.html" class="hover:underline">Inicio</a>
                        <span>›</span>
                        <a href="../noticias.html" class="hover:underline">Blog</a>
                        <span>›</span>
                        <span>JavaScript ES6+</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold mb-4">JavaScript Moderno: Guía Completa ES6+</h1>
                    <div class="flex items-center space-x-4 text-sm">
                        <span>📅 15 de Octubre, 2025</span>
                        <span>⏱️ 20 min lectura</span>
                    </div>
                </div>

                <div class="relative h-96 overflow-hidden">
                    <img src="../../imagenes/5.jpg" alt="JavaScript ES6+" class="w-full h-full object-cover">
                </div>

                <div class="p-8 md:p-12">
                    <div class="bg-yellow-50 border-l-4 border-yellow-500 p-6 rounded-r-lg mb-8">
                        <p class="text-lg leading-relaxed text-gray-700">
                            Domina las características modernas de JavaScript: arrow functions, destructuring, async/await, 
                            módulos ES6 y más. Esta guía completa te convertirá en un experto de JavaScript moderno.
                        </p>
                    </div>

                    <div class="bg-gray-50 p-6 rounded-xl mb-8">
                        <h2 class="text-2xl font-bold mb-4">📋 Contenido</h2>
                        <ul class="space-y-2">
                            <li><a href="#let-const" class="text-yellow-600 hover:underline">1. let, const y Scope</a></li>
                            <li><a href="#arrow" class="text-yellow-600 hover:underline">2. Arrow Functions</a></li>
                            <li><a href="#destructuring" class="text-yellow-600 hover:underline">3. Destructuring</a></li>
                            <li><a href="#async" class="text-yellow-600 hover:underline">4. Async/Await</a></li>
                            <li><a href="#modules" class="text-yellow-600 hover:underline">5. Módulos ES6</a></li>
                        </ul>
                    </div>

                    <section id="let-const" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📦 let, const y Block Scope</h2>
                        
                        <div class="grid md:grid-cols-2 gap-6 mb-6">
                            <div>
                                <h3 class="text-xl font-bold mb-3 text-red-600">❌ var (Evitar)</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-xl">
                                    <pre class="text-sm"><code>var nombre = 'Ana'
var nombre = 'Juan' // OK pero confuso
console.log(nombre) // 'Juan'

if (true) {
  var edad = 25
}
console.log(edad) // 25 (se filtra!)</code></pre>
                                </div>
                            </div>
                            <div>
                                <h3 class="text-xl font-bold mb-3 text-green-600">✅ let/const</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-xl">
                                    <pre class="text-sm"><code>const nombre = 'Ana'
// nombre = 'Juan' // ❌ Error

let edad = 25
edad = 26 // ✅ OK

if (true) {
  let ciudad = 'Madrid'
}
// console.log(ciudad) // ❌ Error</code></pre>
                                </div>
                            </div>
                        </div>

                        <div class="bg-blue-50 p-6 rounded-xl">
                            <h4 class="font-bold text-blue-900 mb-2">💡 Regla de Oro</h4>
                            <p class="text-blue-800">Usa <code class="bg-blue-200 px-2 py-1 rounded">const</code> por defecto. Solo usa <code class="bg-blue-200 px-2 py-1 rounded">let</code> si necesitas reasignar.</p>
                        </div>
                    </section>

                    <section id="arrow" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">➡️ Arrow Functions</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Las arrow functions son más concisas y mantienen el contexto de <code>this</code>.
                        </p>

                        <h3 class="text-2xl font-bold mb-4">Sintaxis</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// Función tradicional
function suma(a, b) {
  return a + b
}

// Arrow function
const suma = (a, b) => a + b

// Con un parámetro, sin paréntesis
const doble = x => x * 2

// Con cuerpo de bloque
const saludar = nombre => {
  const mensaje = \`Hola, \${nombre}!\`
  return mensaje
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Contexto de this</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>class Usuario {
  constructor(nombre) {
    this.nombre = nombre
  }

  // ❌ Función tradicional pierde this
  saludarMal() {
    setTimeout(function() {
      console.log(this.nombre) // undefined
    }, 1000)
  }

  // ✅ Arrow function mantiene this
  saludarBien() {
    setTimeout(() => {
      console.log(this.nombre) // Funciona!
    }, 1000)
  }
}</code></pre>
                        </div>
                    </section>

                    <section id="destructuring" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📦 Destructuring: Extraer Valores</h2>
                        
                        <h3 class="text-2xl font-bold mb-4">Objetos</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>const usuario = {
  nombre: 'Ana',
  edad: 28,
  ciudad: 'Madrid',
  profesion: 'Developer'
}

// Extrae propiedades
const { nombre, edad } = usuario
console.log(nombre) // 'Ana'

// Con renombrado
const { nombre: nombreUsuario } = usuario
console.log(nombreUsuario) // 'Ana'

// Con valores por defecto
const { pais = 'España' } = usuario
console.log(pais) // 'España'</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Arrays</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>const colores = ['rojo', 'verde', 'azul']

const [primero, segundo] = colores
console.log(primero) // 'rojo'

// Saltar elementos
const [, , tercero] = colores
console.log(tercero) // 'azul'

// Rest operator
const [cabeza, ...resto] = colores
console.log(resto) // ['verde', 'azul']</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">En Funciones</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// Parámetros destructurados
function mostrarUsuario({ nombre, edad }) {
  console.log(\`\${nombre} tiene \${edad} años\`)
}

mostrarUsuario(usuario) // 'Ana tiene 28 años'

// Con valores por defecto
function crear({ titulo, activo = true }) {
  return { titulo, activo }
}

crear({ titulo: 'Post' }) // { titulo: 'Post', activo: true }</code></pre>
                        </div>
                    </section>

                    <section id="async" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">⚡ Async/Await: Asincronía Simple</h2>
                        
                        <div class="grid md:grid-cols-2 gap-6 mb-6">
                            <div>
                                <h3 class="text-xl font-bold mb-3 text-red-600">❌ Callbacks (Antiguo)</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-xl">
                                    <pre class="text-xs"><code>fetch('/api/user')
  .then(res => res.json())
  .then(user => {
    fetch(\`/api/posts/\${user.id}\`)
      .then(res => res.json())
      .then(posts => {
        console.log(posts)
      })
  })</code></pre>
                                </div>
                            </div>
                            <div>
                                <h3 class="text-xl font-bold mb-3 text-green-600">✅ Async/Await</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-xl">
                                    <pre class="text-xs"><code>async function getPosts() {
  const userRes = await fetch('/api/user')
  const user = await userRes.json()
  
  const postsRes = await fetch(\`/api/posts/\${user.id}\`)
  const posts = await postsRes.json()
  
  return posts
}</code></pre>
                                </div>
                            </div>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Manejo de Errores</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>async function cargarDatos() {
  try {
    const response = await fetch('/api/datos')
    
    if (!response.ok) {
      throw new Error('Error en la petición')
    }
    
    const datos = await response.json()
    return datos
  } catch (error) {
    console.error('Error:', error.message)
    return null
  }
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Peticiones Paralelas</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// ❌ Secuencial (lento)
const user = await fetch('/api/user').then(r => r.json())
const posts = await fetch('/api/posts').then(r => r.json())

// ✅ Paralelo (rápido)
const [user, posts] = await Promise.all([
  fetch('/api/user').then(r => r.json()),
  fetch('/api/posts').then(r => r.json())
])</code></pre>
                        </div>
                    </section>

                    <section id="modules" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📦 Módulos ES6</h2>
                        
                        <h3 class="text-2xl font-bold mb-4">Export</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// utils.js

// Named exports
export const PI = 3.14159
export function suma(a, b) {
  return a + b
}

// Default export
export default class Calculadora {
  sumar(a, b) {
    return a + b
  }
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Import</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// app.js

// Import default
import Calculadora from './utils.js'

// Import named
import { PI, suma } from './utils.js'

// Import todo
import * as utils from './utils.js'

// Import con renombrado
import { suma as sumar } from './utils.js'</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Dynamic Imports</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// Carga bajo demanda
button.addEventListener('click', async () => {
  const module = await import('./graficas.js')
  module.mostrarGrafica(datos)
})</code></pre>
                        </div>
                    </section>

                    <div class="bg-gradient-to-r from-yellow-500 to-orange-500 p-8 rounded-xl text-white mt-12">
                        <h2 class="text-2xl font-bold mb-4">🎯 Conclusión</h2>
                        <p class="text-lg leading-relaxed">
                            Dominar ES6+ es esencial para cualquier desarrollador JavaScript moderno. Estas características 
                            hacen tu código más limpio, legible y mantenible. ¡Comienza a usarlas hoy!
                        </p>
                    </div>

                    <div class="flex justify-between items-center mt-12 pt-8 border-t">
                        <a href="articulo-css-moderno.html" class="text-yellow-600 hover:underline">← CSS Moderno</a>
                        <a href="../noticias.html" class="text-gray-600 hover:text-yellow-600">Ver todos</a>
                        <a href="articulo-nodejs-principiantes.html" class="text-yellow-600 hover:underline">Node.js →</a>
                    </div>
                </div>
            </article>
        </div>
    </main>

    <footer class="bg-gray-900 text-white py-12 mt-20">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <p class="text-gray-400">© 2025 Mi Blog. Todos los derechos reservados.</p>
        </div>
    </footer>

    <script>
        function toggleMenu() {
            document.getElementById('mobile-menu').classList.toggle('hidden');
        }
    </script>
</body>
</html>
"""
}

def update_article_content(filename, content):
    filepath = os.path.join(articles_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            current_content = f.read()
        
        nav_end = current_content.find('<!-- Espaciador para el nav fijo -->')
        
        if nav_end != -1:
            content_start = current_content.find('</div>', nav_end)
            
            if content_start != -1:
                nav_section = current_content[:content_start + 6]
                new_full_content = nav_section + '\\n' + content
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_full_content)
                
                print(f"✓ Actualizado: {filename}")
                return True
        
        print(f"✗ No se pudo encontrar la estructura en: {filename}")
        return False
        
    except Exception as e:
        print(f"✗ Error en {filename}: {str(e)}")
        return False

print("Actualizando artículos con contenido documentado...\\n")

for filename, content in remaining_articles.items():
    update_article_content(filename, content)

print("\\n✅ Completado!")
