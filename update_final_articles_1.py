import os

articles_dir = r"c:\Users\angeh\Desktop\primera pagina\pages\articles"

# Contenido para los últimos 4 artículos
final_articles = {
    "articulo-nodejs-principiantes.html": """
    <main class="bg-gray-50 py-12">
        <div class="max-w-4xl mx-auto px-4">
            <article class="bg-white rounded-2xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-green-500 to-emerald-600 p-8 text-white">
                    <div class="flex items-center space-x-2 text-sm mb-4">
                        <a href="../../index.html" class="hover:underline">Inicio</a>
                        <span>›</span>
                        <a href="../noticias.html" class="hover:underline">Blog</a>
                        <span>›</span>
                        <span>Node.js para Principiantes</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold mb-4">Node.js: Guía Completa para Principiantes</h1>
                    <div class="flex items-center space-x-4 text-sm">
                        <span>📅 15 de Octubre, 2025</span>
                        <span>⏱️ 25 min lectura</span>
                    </div>
                </div>

                <div class="relative h-96 overflow-hidden">
                    <img src="../../imagenes/6.jpg" alt="Node.js" class="w-full h-full object-cover">
                </div>

                <div class="p-8 md:p-12">
                    <div class="bg-green-50 border-l-4 border-green-600 p-6 rounded-r-lg mb-8">
                        <p class="text-lg leading-relaxed text-gray-700">
                            <strong>Node.js</strong> permite ejecutar JavaScript en el servidor, creando aplicaciones backend 
                            rápidas y escalables. Aprende desde cero: instalación, módulos, Express, APIs REST y bases de datos.
                        </p>
                    </div>

                    <div class="bg-gray-50 p-6 rounded-xl mb-8">
                        <h2 class="text-2xl font-bold mb-4">📋 Contenido</h2>
                        <ul class="space-y-2">
                            <li><a href="#intro" class="text-green-600 hover:underline">1. ¿Qué es Node.js?</a></li>
                            <li><a href="#instalacion" class="text-green-600 hover:underline">2. Instalación y Setup</a></li>
                            <li><a href="#modulos" class="text-green-600 hover:underline">3. Módulos y NPM</a></li>
                            <li><a href="#express" class="text-green-600 hover:underline">4. Express Framework</a></li>
                            <li><a href="#api-rest" class="text-green-600 hover:underline">5. Crear una API REST</a></li>
                            <li><a href="#database" class="text-green-600 hover:underline">6. Conectar Base de Datos</a></li>
                        </ul>
                    </div>

                    <section id="intro" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🚀 ¿Qué es Node.js?</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Node.js es un entorno de ejecución de JavaScript construido sobre el motor V8 de Chrome. 
                            Permite ejecutar JavaScript fuera del navegador, en el servidor.
                        </p>

                        <div class="grid md:grid-cols-3 gap-6 mb-8">
                            <div class="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl text-center border-2 border-green-200">
                                <div class="text-4xl mb-3">⚡</div>
                                <h3 class="text-xl font-bold mb-2 text-green-900">Rápido</h3>
                                <p class="text-gray-700">Event-driven y asíncrono</p>
                            </div>
                            <div class="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl text-center border-2 border-blue-200">
                                <div class="text-4xl mb-3">📦</div>
                                <h3 class="text-xl font-bold mb-2 text-blue-900">NPM</h3>
                                <p class="text-gray-700">Millones de paquetes</p>
                            </div>
                            <div class="bg-gradient-to-br from-purple-50 to-purple-100 p-6 rounded-xl text-center border-2 border-purple-200">
                                <div class="text-4xl mb-3">🌐</div>
                                <h3 class="text-xl font-bold mb-2 text-purple-900">Full Stack</h3>
                                <p class="text-gray-700">JavaScript en todo</p>
                            </div>
                        </div>

                        <div class="bg-blue-50 p-6 rounded-xl">
                            <h3 class="text-xl font-bold mb-3 text-blue-900">💡 ¿Para qué sirve Node.js?</h3>
                            <ul class="space-y-2 text-gray-700">
                                <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> APIs REST y GraphQL</li>
                                <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Aplicaciones en tiempo real (chat, streaming)</li>
                                <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Microservicios</li>
                                <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Herramientas de línea de comandos</li>
                                <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Server-Side Rendering (SSR)</li>
                            </ul>
                        </div>
                    </section>

                    <section id="instalacion" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">💿 Instalación y Setup</h2>
                        
                        <div class="space-y-6">
                            <div class="bg-gray-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3">Paso 1: Descargar Node.js</h3>
                                <p class="text-gray-700 mb-3">Descarga desde <a href="https://nodejs.org" class="text-green-600 hover:underline">nodejs.org</a> (versión LTS recomendada)</p>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code># Verificar instalación
node --version  # v20.11.0
npm --version   # 10.2.4</code></pre>
                                </div>
                            </div>

                            <div class="bg-gray-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3">Paso 2: Primer Programa</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>// app.js
console.log('¡Hola desde Node.js!')

// Ejecutar
// node app.js</code></pre>
                                </div>
                            </div>

                            <div class="bg-gray-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3">Paso 3: Inicializar Proyecto</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>mkdir mi-proyecto
cd mi-proyecto
npm init -y  # Crea package.json</code></pre>
                                </div>
                            </div>
                        </div>
                    </section>

                    <section id="modulos" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📦 Módulos y NPM</h2>
                        
                        <h3 class="text-2xl font-bold mb-4">Módulos Nativos</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// Sistema de archivos
const fs = require('fs')

// Leer archivo
const contenido = fs.readFileSync('archivo.txt', 'utf-8')
console.log(contenido)

// Escribir archivo
fs.writeFileSync('nuevo.txt', 'Hola desde Node!')

// HTTP Server
const http = require('http')

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' })
  res.end('¡Hola Mundo!')
})

server.listen(3000, () => {
  console.log('Servidor en http://localhost:3000')
})</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Instalar Paquetes con NPM</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code># Instalar paquetes
npm install express
npm install nodemon --save-dev

# Paquetes populares
npm install mongoose      # MongoDB
npm install axios         # HTTP requests
npm install dotenv        # Variables de entorno
npm install bcrypt        # Encriptación
npm install jsonwebtoken  # JWT auth</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Crear tus Propios Módulos</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// utils/math.js
function suma(a, b) {
  return a + b
}

function resta(a, b) {
  return a - b
}

module.exports = { suma, resta }

// app.js
const { suma, resta } = require('./utils/math')

console.log(suma(5, 3))   // 8
console.log(resta(10, 4)) // 6</code></pre>
                        </div>
                    </section>

                    <section id="express" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🚂 Express Framework</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Express es el framework web más popular para Node.js. Simplifica la creación de servidores y APIs.
                        </p>

                        <h3 class="text-2xl font-bold mb-4">Servidor Básico con Express</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>const express = require('express')
const app = express()

// Middleware para parsear JSON
app.use(express.json())

// Ruta principal
app.get('/', (req, res) => {
  res.send('¡Hola desde Express!')
})

// Ruta con parámetros
app.get('/user/:id', (req, res) => {
  const userId = req.params.id
  res.json({ mensaje: `Usuario ${userId}` })
})

// Iniciar servidor
const PORT = 3000
app.listen(PORT, () => {
  console.log(`Servidor en http://localhost:${PORT}`)
})</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Middleware</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// Middleware de logging
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`)
  next() // Continuar al siguiente middleware
})

// Middleware de autenticación
const authMiddleware = (req, res, next) => {
  const token = req.headers.authorization
  
  if (!token) {
    return res.status(401).json({ error: 'No autorizado' })
  }
  
  // Verificar token aquí
  next()
}

// Usar middleware en ruta específica
app.get('/admin', authMiddleware, (req, res) => {
  res.json({ mensaje: 'Área de administrador' })
})</code></pre>
                        </div>
                    </section>

                    <section id="api-rest" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🔌 Crear una API REST Completa</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Vamos a crear una API REST para gestionar productos con todas las operaciones CRUD.
                        </p>

                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>const express = require('express')
const app = express()

app.use(express.json())

// Base de datos simulada
let productos = [
  { id: 1, nombre: 'Laptop', precio: 999 },
  { id: 2, nombre: 'Mouse', precio: 25 },
  { id: 3, nombre: 'Teclado', precio: 75 }
]

// GET - Obtener todos los productos
app.get('/api/productos', (req, res) => {
  res.json(productos)
})

// GET - Obtener un producto por ID
app.get('/api/productos/:id', (req, res) => {
  const producto = productos.find(p => p.id === parseInt(req.params.id))
  
  if (!producto) {
    return res.status(404).json({ error: 'Producto no encontrado' })
  }
  
  res.json(producto)
})

// POST - Crear nuevo producto
app.post('/api/productos', (req, res) => {
  const nuevoProducto = {
    id: productos.length + 1,
    nombre: req.body.nombre,
    precio: req.body.precio
  }
  
  productos.push(nuevoProducto)
  res.status(201).json(nuevoProducto)
})

// PUT - Actualizar producto
app.put('/api/productos/:id', (req, res) => {
  const producto = productos.find(p => p.id === parseInt(req.params.id))
  
  if (!producto) {
    return res.status(404).json({ error: 'Producto no encontrado' })
  }
  
  producto.nombre = req.body.nombre
  producto.precio = req.body.precio
  
  res.json(producto)
})

// DELETE - Eliminar producto
app.delete('/api/productos/:id', (req, res) => {
  const index = productos.findIndex(p => p.id === parseInt(req.params.id))
  
  if (index === -1) {
    return res.status(404).json({ error: 'Producto no encontrado' })
  }
  
  productos.splice(index, 1)
  res.json({ mensaje: 'Producto eliminado' })
})

app.listen(3000, () => {
  console.log('API REST corriendo en puerto 3000')
})</code></pre>
                        </div>

                        <div class="bg-blue-50 p-6 rounded-xl">
                            <h3 class="text-xl font-bold mb-3 text-blue-900">🧪 Probar la API</h3>
                            <div class="bg-gray-900 text-white p-4 rounded-lg">
                                <pre class="text-sm"><code># GET todos los productos
curl http://localhost:3000/api/productos

# POST crear producto
curl -X POST http://localhost:3000/api/productos \\
  -H "Content-Type: application/json" \\
  -d '{"nombre":"Monitor","precio":299}'

# PUT actualizar
curl -X PUT http://localhost:3000/api/productos/1 \\
  -H "Content-Type: application/json" \\
  -d '{"nombre":"Laptop Pro","precio":1299}'

# DELETE eliminar
curl -X DELETE http://localhost:3000/api/productos/2</code></pre>
                            </div>
                        </div>
                    </section>

                    <section id="database" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🗄️ Conectar Base de Datos</h2>
                        
                        <h3 class="text-2xl font-bold mb-4">MongoDB con Mongoose</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>const mongoose = require('mongoose')

// Conectar a MongoDB
mongoose.connect('mongodb://localhost/miapp', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})

// Definir Schema
const productoSchema = new mongoose.Schema({
  nombre: { type: String, required: true },
  precio: { type: Number, required: true },
  stock: { type: Number, default: 0 },
  createdAt: { type: Date, default: Date.now }
})

// Crear Modelo
const Producto = mongoose.model('Producto', productoSchema)

// Crear documento
const nuevoProducto = new Producto({
  nombre: 'Laptop',
  precio: 999,
  stock: 10
})

await nuevoProducto.save()

// Consultas
const productos = await Producto.find()
const laptop = await Producto.findOne({ nombre: 'Laptop' })
const caros = await Producto.find({ precio: { $gt: 500 } })

// Actualizar
await Producto.updateOne(
  { nombre: 'Laptop' },
  { $set: { precio: 899 } }
)

// Eliminar
await Producto.deleteOne({ nombre: 'Mouse' })</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">PostgreSQL con Prisma</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// schema.prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model Producto {
  id        Int      @id @default(autoincrement())
  nombre    String
  precio    Float
  stock     Int      @default(0)
  createdAt DateTime @default(now())
}

// app.js
const { PrismaClient } = require('@prisma/client')
const prisma = new PrismaClient()

// Crear
const producto = await prisma.producto.create({
  data: {
    nombre: 'Laptop',
    precio: 999,
    stock: 10
  }
})

// Leer
const productos = await prisma.producto.findMany()
const laptop = await prisma.producto.findUnique({
  where: { id: 1 }
})

// Actualizar
await prisma.producto.update({
  where: { id: 1 },
  data: { precio: 899 }
})

// Eliminar
await prisma.producto.delete({
  where: { id: 1 }
})</code></pre>
                        </div>
                    </section>

                    <div class="bg-purple-50 p-6 rounded-xl mb-12">
                        <h3 class="text-2xl font-bold mb-4 text-purple-900">📚 Recursos para Aprender Más</h3>
                        <ul class="space-y-2 text-gray-700">
                            <li class="flex items-start"><span class="text-purple-600 mr-2">📖</span> Documentación oficial: <a href="https://nodejs.org" class="text-purple-600 hover:underline">nodejs.org</a></li>
                            <li class="flex items-start"><span class="text-purple-600 mr-2">📖</span> Express: <a href="https://expressjs.com" class="text-purple-600 hover:underline">expressjs.com</a></li>
                            <li class="flex items-start"><span class="text-purple-600 mr-2">📖</span> NPM: <a href="https://npmjs.com" class="text-purple-600 hover:underline">npmjs.com</a></li>
                            <li class="flex items-start"><span class="text-purple-600 mr-2">📖</span> MongoDB: <a href="https://mongodb.com" class="text-purple-600 hover:underline">mongodb.com</a></li>
                        </ul>
                    </div>

                    <div class="bg-gradient-to-r from-green-500 to-emerald-600 p-8 rounded-xl text-white mt-12">
                        <h2 class="text-2xl font-bold mb-4">🎯 Conclusión</h2>
                        <p class="text-lg leading-relaxed">
                            Node.js te permite usar JavaScript en el backend, crear APIs REST potentes y aplicaciones escalables. 
                            Con Express, MongoDB/PostgreSQL y las herramientas del ecosistema NPM, puedes construir aplicaciones 
                            full-stack completas. ¡Comienza a crear tus propios proyectos hoy!
                        </p>
                    </div>

                    <div class="flex justify-between items-center mt-12 pt-8 border-t">
                        <a href="articulo-javascript-es6.html" class="text-green-600 hover:underline">← JavaScript ES6</a>
                        <a href="../noticias.html" class="text-gray-600 hover:text-green-600">Ver todos</a>
                        <a href="articulo-nextjs-15-2025.html" class="text-green-600 hover:underline">Next.js 15 →</a>
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

    "articulo-css-moderno.html": """
    <main class="bg-gray-50 py-12">
        <div class="max-w-4xl mx-auto px-4">
            <article class="bg-white rounded-2xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-pink-500 to-rose-600 p-8 text-white">
                    <div class="flex items-center space-x-2 text-sm mb-4">
                        <a href="../../index.html" class="hover:underline">Inicio</a>
                        <span>›</span>
                        <a href="../noticias.html" class="hover:underline">Blog</a>
                        <span>›</span>
                        <span>CSS Moderno</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold mb-4">CSS Moderno: Grid, Flexbox y Animaciones</h1>
                    <div class="flex items-center space-x-4 text-sm">
                        <span>📅 15 de Octubre, 2025</span>
                        <span>⏱️ 22 min lectura</span>
                    </div>
                </div>

                <div class="relative h-96 overflow-hidden">
                    <img src="../../imagenes/4.jpg" alt="CSS Moderno" class="w-full h-full object-cover">
                </div>

                <div class="p-8 md:p-12">
                    <div class="bg-pink-50 border-l-4 border-pink-600 p-6 rounded-r-lg mb-8">
                        <p class="text-lg leading-relaxed text-gray-700">
                            Domina las características modernas de CSS: <strong>Grid Layout</strong>, <strong>Flexbox</strong>, 
                            <strong>Custom Properties</strong>, animaciones y mucho más. Crea layouts profesionales y responsivos sin frameworks.
                        </p>
                    </div>

                    <div class="bg-gray-50 p-6 rounded-xl mb-8">
                        <h2 class="text-2xl font-bold mb-4">📋 Contenido</h2>
                        <ul class="space-y-2">
                            <li><a href="#flexbox" class="text-pink-600 hover:underline">1. Flexbox para Layouts</a></li>
                            <li><a href="#grid" class="text-pink-600 hover:underline">2. CSS Grid</a></li>
                            <li><a href="#variables" class="text-pink-600 hover:underline">3. Custom Properties (Variables)</a></li>
                            <li><a href="#animaciones" class="text-pink-600 hover:underline">4. Animaciones y Transitions</a></li>
                            <li><a href="#responsive" class="text-pink-600 hover:underline">5. Diseño Responsivo</a></li>
                        </ul>
                    </div>

                    <section id="flexbox" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📐 Flexbox: Layouts en Una Dimensión</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Flexbox es perfecto para layouts en una dirección (horizontal o vertical): navegaciones, 
                            centrado, distribución de espacios.
                        </p>

                        <h3 class="text-2xl font-bold mb-4">Conceptos Básicos</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>.contenedor {
  display: flex;
  justify-content: space-between; /* Eje principal */
  align-items: center;            /* Eje cruzado */
  gap: 1rem;                      /* Espacio entre items */
}

/* Dirección */
.vertical {
  flex-direction: column;
}

.horizontal {
  flex-direction: row;
}

/* Centrado perfecto */
.centrado {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Ejemplo: Navegación</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>/* HTML */
&lt;nav class="navbar"&gt;
  &lt;div class="logo"&gt;Mi Sitio&lt;/div&gt;
  &lt;ul class="menu"&gt;
    &lt;li&gt;&lt;a href="#"&gt;Inicio&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="#"&gt;Blog&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href="#"&gt;Contacto&lt;/a&gt;&lt;/li&gt;
  &lt;/ul&gt;
&lt;/nav&gt;

/* CSS */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: white;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.menu {
  display: flex;
  gap: 2rem;
  list-style: none;
}

.menu a {
  text-decoration: none;
  color: #333;
  transition: color 0.3s;
}

.menu a:hover {
  color: #3b82f6;
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Items Flexibles</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>.item {
  flex: 1;        /* Crece y se encoge igualmente */
}

.item-fijo {
  flex: 0 0 200px; /* No crece, no encoge, 200px fijo */
}

.item-crecer {
  flex-grow: 2;    /* Crece el doble que otros */
}

/* Ejemplo: Sidebar + Contenido */
.layout {
  display: flex;
}

.sidebar {
  flex: 0 0 250px;  /* Ancho fijo 250px */
}

.contenido {
  flex: 1;          /* Ocupa el espacio restante */
}</code></pre>
                        </div>
                    </section>

                    <section id="grid" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🎛️ CSS Grid: Layouts en Dos Dimensiones</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            CSS Grid es perfecto para layouts complejos en filas y columnas: galerías, dashboards, 
                            layouts de página completos.
                        </p>

                        <h3 class="text-2xl font-bold mb-4">Grid Básico</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 columnas iguales */
  gap: 2rem;
}

/* Columnas con tamaños específicos */
.grid-mixed {
  grid-template-columns: 250px 1fr 200px;
  /* Sidebar | Contenido | Ads */
}

/* Auto-fill: Responsive automático */
.galeria {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Layout Completo de Página</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>/* HTML */
&lt;div class="page-layout"&gt;
  &lt;header&gt;Header&lt;/header&gt;
  &lt;nav&gt;Navegación&lt;/nav&gt;
  &lt;main&gt;Contenido Principal&lt;/main&gt;
  &lt;aside&gt;Sidebar&lt;/aside&gt;
  &lt;footer&gt;Footer&lt;/footer&gt;
&lt;/div&gt;

/* CSS */
.page-layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "nav    main   aside"
    "footer footer footer";
  grid-template-columns: 200px 1fr 250px;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
  gap: 1rem;
}

header { grid-area: header; }
nav    { grid-area: nav; }
main   { grid-area: main; }
aside  { grid-area: aside; }
footer { grid-area: footer; }

/* Responsive */
@media (max-width: 768px) {
  .page-layout {
    grid-template-areas:
      "header"
      "nav"
      "main"
      "aside"
      "footer";
    grid-template-columns: 1fr;
  }
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Galería de Imágenes</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>.galeria {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.imagen-destacada {
  grid-column: span 2;  /* Ocupa 2 columnas */
  grid-row: span 2;     /* Ocupa 2 filas */
}

.galeria img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}</code></pre>
                        </div>
                    </section>

                    <section id="variables" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🎨 Custom Properties (Variables CSS)</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Las variables CSS permiten reutilizar valores y crear temas dinámicos de forma nativa.
                        </p>

                        <h3 class="text-2xl font-bold mb-4">Sistema de Colores</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>:root {
  /* Colores principales */
  --color-primary: #3b82f6;
  --color-secondary: #8b5cf6;
  --color-success: #10b981;
  --color-danger: #ef4444;
  
  /* Grises */
  --gray-50: #f9fafb;
  --gray-900: #111827;
  
  /* Espaciado */
  --spacing-xs: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 2rem;
  
  /* Tipografía */
  --font-sans: 'Inter', sans-serif;
  --font-mono: 'Fira Code', monospace;
}

/* Usar variables */
.btn-primary {
  background: var(--color-primary);
  padding: var(--spacing-md) var(--spacing-lg);
  font-family: var(--font-sans);
}

.card {
  background: var(--gray-50);
  color: var(--gray-900);
  margin: var(--spacing-lg);
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Dark Mode</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>:root {
  --bg-color: white;
  --text-color: #111827;
  --border-color: #e5e7eb;
}

[data-theme="dark"] {
  --bg-color: #111827;
  --text-color: #f9fafb;
  --border-color: #374151;
}

body {
  background: var(--bg-color);
  color: var(--text-color);
}

.card {
  border: 1px solid var(--border-color);
}

/* Toggle con JavaScript */
const toggle = document.querySelector('#theme-toggle')
toggle.addEventListener('click', () => {
  const theme = document.documentElement.getAttribute('data-theme')
  document.documentElement.setAttribute(
    'data-theme',
    theme === 'dark' ? 'light' : 'dark'
  )
})</code></pre>
                        </div>
                    </section>

                    <section id="animaciones" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">✨ Animaciones y Transitions</h2>
                        
                        <h3 class="text-2xl font-bold mb-4">Transitions</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>.button {
  background: #3b82f6;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  
  /* Transición suave */
  transition: all 0.3s ease;
}

.button:hover {
  background: #2563eb;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

.button:active {
  transform: translateY(0);
}

/* Múltiples propiedades */
.card {
  transition: 
    background-color 0.3s ease,
    transform 0.3s ease,
    box-shadow 0.3s ease;
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Keyframe Animations</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>/* Fade In */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.elemento {
  animation: fadeIn 0.6s ease-out;
}

/* Loading Spinner */
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f4f6;
  border-top-color: #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* Bounce */
@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

.icono {
  animation: bounce 2s ease-in-out infinite;
}</code></pre>
                        </div>
                    </section>

                    <section id="responsive" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📱 Diseño Responsivo</h2>
                        
                        <h3 class="text-2xl font-bold mb-4">Media Queries</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>/* Mobile First */
.container {
  padding: 1rem;
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
    max-width: 720px;
    margin: 0 auto;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
}

/* Grid responsivo */
.grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Container Queries (Nuevo)</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>.card-container {
  container-type: inline-size;
}

.card {
  padding: 1rem;
}

/* Basado en el contenedor, no en la ventana */
@container (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}</code></pre>
                        </div>
                    </section>

                    <div class="bg-gradient-to-r from-pink-500 to-rose-600 p-8 rounded-xl text-white mt-12">
                        <h2 class="text-2xl font-bold mb-4">🎯 Conclusión</h2>
                        <p class="text-lg leading-relaxed">
                            CSS moderno ofrece herramientas poderosas para crear layouts profesionales sin necesidad de frameworks. 
                            Flexbox, Grid, Custom Properties y animaciones te permiten construir interfaces hermosas y responsivas 
                            con código nativo y eficiente.
                        </p>
                    </div>

                    <div class="flex justify-between items-center mt-12 pt-8 border-t">
                        <a href="articulo-mobile-first.html" class="text-pink-600 hover:underline">← Mobile First</a>
                        <a href="../noticias.html" class="text-gray-600 hover:text-pink-600">Ver todos</a>
                        <a href="articulo-javascript-es6.html" class="text-pink-600 hover:underline">JavaScript ES6 →</a>
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
                new_full_content = nav_section + '\n' + content
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_full_content)
                
                print(f"✓ Actualizado: {filename}")
                return True
        
        print(f"✗ No se pudo encontrar la estructura en: {filename}")
        return False
        
    except Exception as e:
        print(f"✗ Error en {filename}: {str(e)}")
        return False

print("Actualizando Node.js y CSS Moderno...\n")

for filename, content in final_articles.items():
    update_article_content(filename, content)

print("\n✅ Completado!")
