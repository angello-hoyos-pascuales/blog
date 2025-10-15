import os

# Directorio de artículos
articles_dir = r"c:\Users\angeh\Desktop\primera pagina\pages\articles"

# Contenido documentado para cada artículo
articles_content = {
    "articulo-react-19-2025.html": """
    <main class="bg-gray-50 py-12">
        <div class="max-w-4xl mx-auto px-4">
            <article class="bg-white rounded-2xl shadow-xl overflow-hidden">
                <!-- Header del Artículo -->
                <div class="bg-gradient-to-r from-primary to-secondary p-8 text-white">
                    <div class="flex items-center space-x-2 text-sm mb-4">
                        <a href="../../index.html" class="hover:underline">Inicio</a>
                        <span>›</span>
                        <a href="../noticias.html" class="hover:underline">Blog</a>
                        <span>›</span>
                        <span>React 19</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold mb-4">React 19: Guía Completa de Server Components</h1>
                    <div class="flex items-center space-x-4 text-sm">
                        <span>📅 15 de Octubre, 2025</span>
                        <span>⏱️ 15 min lectura</span>
                        <span>👤 Por Admin</span>
                    </div>
                </div>

                <!-- Imagen Principal -->
                <div class="relative h-96 overflow-hidden">
                    <img src="../../imagenes/5.jpg" alt="React 19" class="w-full h-full object-cover">
                </div>

                <!-- Contenido del Artículo -->
                <div class="p-8 md:p-12">
                    
                    <!-- Introducción -->
                    <div class="bg-blue-50 border-l-4 border-primary p-6 rounded-r-lg mb-8">
                        <p class="text-lg leading-relaxed text-gray-700">
                            <strong>React 19</strong> representa la evolución más significativa del framework desde la introducción de Hooks. 
                            Con <strong>Server Components</strong>, optimización automática y nuevas APIs, React 19 redefine cómo construimos 
                            aplicaciones web modernas con mejor rendimiento y experiencia de usuario.
                        </p>
                    </div>

                    <!-- Tabla de Contenidos -->
                    <div class="bg-gray-50 p-6 rounded-xl mb-8">
                        <h2 class="text-2xl font-bold mb-4 text-gray-800">📋 Contenido</h2>
                        <ul class="space-y-2">
                            <li><a href="#novedades" class="text-primary hover:underline">1. Novedades Principales</a></li>
                            <li><a href="#server-components" class="text-primary hover:underline">2. Server Components</a></li>
                            <li><a href="#compiler" class="text-primary hover:underline">3. React Compiler</a></li>
                            <li><a href="#actions" class="text-primary hover:underline">4. Actions API</a></li>
                            <li><a href="#migracion" class="text-primary hover:underline">5. Guía de Migración</a></li>
                        </ul>
                    </div>

                    <!-- Sección 1: Novedades -->
                    <section id="novedades" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">🚀 Novedades Principales de React 19</h2>
                        
                        <div class="grid md:grid-cols-2 gap-6 mb-8">
                            <div class="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-blue-900">⚡ Server Components</h3>
                                <p class="text-gray-700">Renderiza componentes en el servidor, reduciendo el JavaScript en el cliente hasta un 50%.</p>
                            </div>
                            <div class="bg-gradient-to-br from-purple-50 to-purple-100 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-purple-900">🧠 React Compiler</h3>
                                <p class="text-gray-700">Optimización automática sin necesidad de useMemo o useCallback manuales.</p>
                            </div>
                            <div class="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-green-900">🔄 Actions</h3>
                                <p class="text-gray-700">Manejo simplificado de mutaciones y estados de carga con useActionState.</p>
                            </div>
                            <div class="bg-gradient-to-br from-orange-50 to-orange-100 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-orange-900">📊 use() Hook</h3>
                                <p class="text-gray-700">Lectura de recursos como promesas y contexto de forma condicional.</p>
                            </div>
                        </div>
                    </section>

                    <!-- Sección 2: Server Components -->
                    <section id="server-components" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">🖥️ Server Components en Detalle</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Los Server Components son la característica más revolucionaria de React 19. Permiten que componentes 
                            se ejecuten exclusivamente en el servidor, accediendo directamente a bases de datos y APIs sin exponer 
                            credenciales al cliente.
                        </p>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">💡 Ventajas Clave</h3>
                        <div class="space-y-4 mb-6">
                            <div class="flex items-start space-x-3">
                                <div class="bg-green-500 text-white rounded-full p-2 mt-1">✓</div>
                                <div>
                                    <h4 class="font-bold text-gray-800">Zero Bundle Size</h4>
                                    <p class="text-gray-600">No añaden JavaScript al cliente, solo HTML renderizado</p>
                                </div>
                            </div>
                            <div class="flex items-start space-x-3">
                                <div class="bg-green-500 text-white rounded-full p-2 mt-1">✓</div>
                                <div>
                                    <h4 class="font-bold text-gray-800">Acceso Directo a Datos</h4>
                                    <p class="text-gray-600">Consulta bases de datos directamente sin APIs intermedias</p>
                                </div>
                            </div>
                            <div class="flex items-start space-x-3">
                                <div class="bg-green-500 text-white rounded-full p-2 mt-1">✓</div>
                                <div>
                                    <h4 class="font-bold text-gray-800">Mejor SEO</h4>
                                    <p class="text-gray-600">HTML completamente renderizado para motores de búsqueda</p>
                                </div>
                            </div>
                        </div>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">📝 Ejemplo Práctico</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl overflow-x-auto mb-6">
                            <pre class="text-sm"><code>// app/productos/page.tsx - Server Component
import { db } from '@/lib/database'

export default async function ProductosPage() {
  // ✅ Acceso directo a la base de datos
  const productos = await db.producto.findMany({
    where: { activo: true },
    include: { categoria: true },
    orderBy: { createdAt: 'desc' }
  })

  return (
    &lt;div&gt;
      &lt;h1&gt;Nuestros Productos&lt;/h1&gt;
      &lt;div className="grid grid-cols-3 gap-4"&gt;
        {productos.map(producto => (
          &lt;ProductCard key={producto.id} {...producto} /&gt;
        ))}
      &lt;/div&gt;
    &lt;/div&gt;
  )
}</code></pre>
                        </div>
                    </section>

                    <!-- Sección 3: React Compiler -->
                    <section id="compiler" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">🔧 React Compiler: Optimización Automática</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            El React Compiler analiza tu código y aplica optimizaciones automáticamente. Ya no necesitas 
                            envolver todo en <code class="bg-gray-100 px-2 py-1 rounded">useMemo</code> o 
                            <code class="bg-gray-100 px-2 py-1 rounded">useCallback</code>.
                        </p>

                        <div class="bg-yellow-50 border-l-4 border-yellow-500 p-6 rounded-r-lg mb-6">
                            <h4 class="font-bold text-yellow-900 mb-2">⚡ Rendimiento Mejorado</h4>
                            <p class="text-yellow-800">El compiler puede mejorar el rendimiento hasta 3x en componentes complejos.</p>
                        </div>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">Antes vs Después</h3>
                        <div class="grid md:grid-cols-2 gap-6 mb-6">
                            <div>
                                <h4 class="font-bold mb-2 text-red-600">❌ React 18 (Manual)</h4>
                                <div class="bg-gray-900 text-white p-4 rounded-xl">
                                    <pre class="text-xs"><code>const filteredData = useMemo(() => {
  return data.filter(item => 
    item.active
  )
}, [data])

const handleClick = useCallback(() => {
  console.log(filteredData)
}, [filteredData])</code></pre>
                                </div>
                            </div>
                            <div>
                                <h4 class="font-bold mb-2 text-green-600">✅ React 19 (Automático)</h4>
                                <div class="bg-gray-900 text-white p-4 rounded-xl">
                                    <pre class="text-xs"><code>// El compiler optimiza automáticamente
const filteredData = data.filter(
  item => item.active
)

const handleClick = () => {
  console.log(filteredData)
}</code></pre>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Sección 4: Actions -->
                    <section id="actions" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">🔄 Actions: Mutaciones Simplificadas</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Actions simplifican el manejo de formularios y mutaciones de datos con estados de carga y error integrados.
                        </p>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">Ejemplo con useActionState</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl overflow-x-auto mb-6">
                            <pre class="text-sm"><code>// app/acciones.ts - Server Action
'use server'

export async function crearProducto(formData: FormData) {
  const nombre = formData.get('nombre')
  const precio = formData.get('precio')
  
  try {
    await db.producto.create({
      data: { nombre, precio: Number(precio) }
    })
    return { success: true, message: 'Producto creado' }
  } catch (error) {
    return { success: false, error: 'Error al crear' }
  }
}

// Componente del formulario
'use client'
import { useActionState } from 'react'

export function FormularioProducto() {
  const [state, action, isPending] = useActionState(
    crearProducto,
    { success: false }
  )

  return (
    &lt;form action={action}&gt;
      &lt;input name="nombre" required /&gt;
      &lt;input name="precio" type="number" required /&gt;
      &lt;button disabled={isPending}&gt;
        {isPending ? 'Guardando...' : 'Crear Producto'}
      &lt;/button&gt;
      {state.message && &lt;p&gt;{state.message}&lt;/p&gt;}
    &lt;/form&gt;
  )
}</code></pre>
                        </div>
                    </section>

                    <!-- Sección 5: Migración -->
                    <section id="migracion" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">📦 Guía de Migración</h2>
                        
                        <div class="space-y-6">
                            <div class="bg-blue-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-blue-900">Paso 1: Actualizar Dependencias</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>npm install react@19 react-dom@19
npm install next@15  # Si usas Next.js</code></pre>
                                </div>
                            </div>

                            <div class="bg-purple-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-purple-900">Paso 2: Actualizar Configuración</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>// next.config.js
module.exports = {
  experimental: {
    reactCompiler: true,
    serverActions: true
  }
}</code></pre>
                                </div>
                            </div>

                            <div class="bg-green-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-green-900">Paso 3: Migrar Componentes Gradualmente</h3>
                                <p class="text-gray-700">Comienza convirtiendo páginas estáticas a Server Components, luego optimiza componentes interactivos.</p>
                            </div>
                        </div>
                    </section>

                    <!-- Conclusión -->
                    <div class="bg-gradient-to-r from-primary to-secondary p-8 rounded-xl text-white mt-12">
                        <h2 class="text-2xl font-bold mb-4">🎯 Conclusión</h2>
                        <p class="text-lg leading-relaxed">
                            React 19 marca un antes y después en el desarrollo web moderno. Los Server Components, 
                            el compiler automático y las Actions simplifican el desarrollo mientras mejoran 
                            significativamente el rendimiento. Es el momento perfecto para comenzar a migrar tus proyectos.
                        </p>
                    </div>

                    <!-- Navegación de Artículos -->
                    <div class="flex justify-between items-center mt-12 pt-8 border-t">
                        <a href="articulo-nextjs-15-2025.html" class="text-primary hover:underline">← Next.js 15</a>
                        <a href="../noticias.html" class="text-gray-600 hover:text-primary">Ver todos los artículos</a>
                        <a href="articulo-typescript-53-2025.html" class="text-primary hover:underline">TypeScript 5.3 →</a>
                    </div>
                </div>
            </article>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12 mt-20">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <p class="text-gray-400">© 2025 Mi Blog. Todos los derechos reservados.</p>
        </div>
    </footer>

    <script>
        function toggleMenu() {
            const menu = document.getElementById('mobile-menu');
            menu.classList.toggle('hidden');
        }
    </script>
</body>
</html>
""",

    "articulo-typescript-53-2025.html": """
    <main class="bg-gray-50 py-12">
        <div class="max-w-4xl mx-auto px-4">
            <article class="bg-white rounded-2xl shadow-xl overflow-hidden">
                <!-- Header del Artículo -->
                <div class="bg-gradient-to-r from-blue-600 to-purple-600 p-8 text-white">
                    <div class="flex items-center space-x-2 text-sm mb-4">
                        <a href="../../index.html" class="hover:underline">Inicio</a>
                        <span>›</span>
                        <a href="../noticias.html" class="hover:underline">Blog</a>
                        <span>›</span>
                        <span>TypeScript 5.3</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold mb-4">TypeScript 5.3: Decorators y Pattern Matching</h1>
                    <div class="flex items-center space-x-4 text-sm">
                        <span>📅 15 de Octubre, 2025</span>
                        <span>⏱️ 12 min lectura</span>
                        <span>👤 Por Admin</span>
                    </div>
                </div>

                <!-- Imagen Principal -->
                <div class="relative h-96 overflow-hidden">
                    <img src="../../imagenes/6.jpg" alt="TypeScript 5.3" class="w-full h-full object-cover">
                </div>

                <!-- Contenido del Artículo -->
                <div class="p-8 md:p-12">
                    
                    <!-- Introducción -->
                    <div class="bg-purple-50 border-l-4 border-purple-600 p-6 rounded-r-lg mb-8">
                        <p class="text-lg leading-relaxed text-gray-700">
                            <strong>TypeScript 5.3</strong> introduce características que transforman JavaScript en un lenguaje 
                            de primera clase. Con <strong>Decorators estables</strong>, <strong>Pattern Matching</strong> y mejoras 
                            de rendimiento del 70%, esta versión eleva la seguridad y expresividad del código a nuevos niveles.
                        </p>
                    </div>

                    <!-- Tabla de Contenidos -->
                    <div class="bg-gray-50 p-6 rounded-xl mb-8">
                        <h2 class="text-2xl font-bold mb-4 text-gray-800">📋 Contenido</h2>
                        <ul class="space-y-2">
                            <li><a href="#novedades" class="text-purple-600 hover:underline">1. Novedades Principales</a></li>
                            <li><a href="#decorators" class="text-purple-600 hover:underline">2. Decorators Estables</a></li>
                            <li><a href="#pattern-matching" class="text-purple-600 hover:underline">3. Pattern Matching</a></li>
                            <li><a href="#branded-types" class="text-purple-600 hover:underline">4. Branded Types</a></li>
                            <li><a href="#mejores-practicas" class="text-purple-600 hover:underline">5. Mejores Prácticas</a></li>
                        </ul>
                    </div>

                    <!-- Sección 1: Novedades -->
                    <section id="novedades" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">🚀 Novedades de TypeScript 5.3</h2>
                        
                        <div class="grid md:grid-cols-2 gap-6 mb-8">
                            <div class="bg-gradient-to-br from-purple-50 to-purple-100 p-6 rounded-xl border-2 border-purple-200">
                                <h3 class="text-xl font-bold mb-3 text-purple-900">🎨 Decorators Stage 3</h3>
                                <p class="text-gray-700">Metaprogramación elegante con decorators completamente estables según el estándar ECMAScript.</p>
                            </div>
                            <div class="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl border-2 border-blue-200">
                                <h3 class="text-xl font-bold mb-3 text-blue-900">🔍 Pattern Matching</h3>
                                <p class="text-gray-700">Match expressions nativas para código más declarativo y legible.</p>
                            </div>
                            <div class="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl border-2 border-green-200">
                                <h3 class="text-xl font-bold mb-3 text-green-900">⚡ Performance 70%+</h3>
                                <p class="text-gray-700">Compilación y type checking hasta 70% más rápido que versiones anteriores.</p>
                            </div>
                            <div class="bg-gradient-to-br from-orange-50 to-orange-100 p-6 rounded-xl border-2 border-orange-200">
                                <h3 class="text-xl font-bold mb-3 text-orange-900">🛡️ Branded Types</h3>
                                <p class="text-gray-700">Tipos nominales para domain modeling más seguro y expresivo.</p>
                            </div>
                        </div>
                    </section>

                    <!-- Sección 2: Decorators -->
                    <section id="decorators" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">🎨 Decorators: Metaprogramación Elegante</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Los Decorators permiten modificar o extender el comportamiento de clases, métodos y propiedades 
                            de forma declarativa. Ahora son parte oficial del estándar ECMAScript Stage 3.
                        </p>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">📝 Ejemplo: Class Decorator</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl overflow-x-auto mb-6">
                            <pre class="text-sm"><code>// Decorator para logging automático
function Logged(target: any) {
  return class extends target {
    constructor(...args: any[]) {
      super(...args)
      console.log(\`Creando instancia de \${target.name}\`)
    }
  }
}

@Logged
class Usuario {
  constructor(public nombre: string) {}
}

// Al crear: "Creando instancia de Usuario"
const user = new Usuario('Ana')</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">🔧 Method Decorator para Validación</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl overflow-x-auto mb-6">
                            <pre class="text-sm"><code>function Validate(
  target: any,
  propertyKey: string,
  descriptor: PropertyDescriptor
) {
  const originalMethod = descriptor.value
  
  descriptor.value = function(...args: any[]) {
    // Validar que todos los args sean strings
    if (!args.every(arg => typeof arg === 'string')) {
      throw new Error('Todos los argumentos deben ser strings')
    }
    return originalMethod.apply(this, args)
  }
}

class ProductoService {
  @Validate
  crearProducto(nombre: string, categoria: string) {
    console.log(\`Creando: \${nombre} en \${categoria}\`)
  }
}

const service = new ProductoService()
service.crearProducto('Laptop', 'Electrónica') // ✅ OK
service.crearProducto('Laptop', 123) // ❌ Error!</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">💼 Caso de Uso Real: ORM con Decorators</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl overflow-x-auto mb-6">
                            <pre class="text-sm"><code>// Decorators para definir entidades
function Entity(tableName: string) {
  return function(target: any) {
    target.tableName = tableName
  }
}

function Column(type: string) {
  return function(target: any, propertyKey: string) {
    if (!target.columns) target.columns = {}
    target.columns[propertyKey] = type
  }
}

@Entity('usuarios')
class Usuario {
  @Column('INTEGER')
  id: number

  @Column('VARCHAR(100)')
  nombre: string

  @Column('VARCHAR(100)')
  email: string
}

// Metadata disponible automáticamente
console.log(Usuario.tableName) // 'usuarios'
console.log(Usuario.columns) 
// { id: 'INTEGER', nombre: 'VARCHAR(100)', email: 'VARCHAR(100)' }</code></pre>
                        </div>
                    </section>

                    <!-- Sección 3: Pattern Matching -->
                    <section id="pattern-matching" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">🔍 Pattern Matching Nativo</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Pattern Matching permite escribir lógica condicional de forma más declarativa y segura en tipos.
                        </p>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">Ejemplo Básico</h3>
                        <div class="grid md:grid-cols-2 gap-6 mb-6">
                            <div>
                                <h4 class="font-bold mb-2 text-red-600">❌ Forma Tradicional</h4>
                                <div class="bg-gray-900 text-white p-4 rounded-xl">
                                    <pre class="text-xs"><code>function getStatus(code: number) {
  if (code === 200) {
    return 'OK'
  } else if (code === 404) {
    return 'Not Found'
  } else if (code >= 500) {
    return 'Server Error'
  } else {
    return 'Unknown'
  }
}</code></pre>
                                </div>
                            </div>
                            <div>
                                <h4 class="font-bold mb-2 text-green-600">✅ Con Pattern Matching</h4>
                                <div class="bg-gray-900 text-white p-4 rounded-xl">
                                    <pre class="text-xs"><code>function getStatus(code: number) {
  return match (code) {
    200 => 'OK',
    404 => 'Not Found',
    >= 500 => 'Server Error',
    _ => 'Unknown'
  }
}</code></pre>
                                </div>
                            </div>
                        </div>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">Pattern Matching con Objetos</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl overflow-x-auto mb-6">
                            <pre class="text-sm"><code>type Evento = 
  | { type: 'click', x: number, y: number }
  | { type: 'keypress', key: string }
  | { type: 'scroll', delta: number }

function handleEvent(evento: Evento) {
  return match (evento) {
    { type: 'click', x, y } => \`Click en (\${x}, \${y})\`,
    { type: 'keypress', key: 'Enter' } => 'Enter presionado',
    { type: 'keypress' } => 'Otra tecla',
    { type: 'scroll', delta } when delta > 0 => 'Scroll abajo',
    { type: 'scroll' } => 'Scroll arriba',
    _ => 'Evento desconocido'
  }
}</code></pre>
                        </div>
                    </section>

                    <!-- Sección 4: Branded Types -->
                    <section id="branded-types" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">🛡️ Branded Types para Domain Modeling</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Branded Types permiten crear tipos nominales que previenen errores sutiles al diferenciar 
                            valores que estructuralmente son iguales pero semánticamente diferentes.
                        </p>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">Problema sin Branded Types</h3>
                        <div class="bg-red-50 border-l-4 border-red-500 p-6 rounded-r-lg mb-6">
                            <div class="bg-gray-900 text-white p-4 rounded-lg">
                                <pre class="text-sm"><code>type UserId = string
type ProductId = string

function getUser(id: UserId) { /* ... */ }
function getProduct(id: ProductId) { /* ... */ }

const userId: UserId = "user-123"
const productId: ProductId = "prod-456"

// ⚠️ TypeScript no detecta este error!
getUser(productId) // Debería ser error pero no lo es</code></pre>
                            </div>
                        </div>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">Solución con Branded Types</h3>
                        <div class="bg-green-50 border-l-4 border-green-500 p-6 rounded-r-lg mb-6">
                            <div class="bg-gray-900 text-white p-4 rounded-lg">
                                <pre class="text-sm"><code>// Definir branded types
type Brand&lt;K, T&gt; = K & { __brand: T }

type UserId = Brand&lt;string, 'UserId'&gt;
type ProductId = Brand&lt;string, 'ProductId'&gt;

// Funciones constructoras
function createUserId(id: string): UserId {
  return id as UserId
}

function createProductId(id: string): ProductId {
  return id as ProductId
}

// Funciones que usan los tipos
function getUser(id: UserId) { /* ... */ }
function getProduct(id: ProductId) { /* ... */ }

const userId = createUserId("user-123")
const productId = createProductId("prod-456")

getUser(userId) // ✅ OK
getUser(productId) // ❌ Error: Type 'ProductId' not assignable to 'UserId'</code></pre>
                            </div>
                        </div>

                        <h3 class="text-2xl font-bold mb-4 text-gray-800">Ejemplo Avanzado: Email Validado</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl overflow-x-auto mb-6">
                            <pre class="text-sm"><code>type ValidEmail = Brand&lt;string, 'ValidEmail'&gt;

function validateEmail(email: string): ValidEmail | null {
  const regex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/
  if (regex.test(email)) {
    return email as ValidEmail
  }
  return null
}

function sendEmail(to: ValidEmail, subject: string, body: string) {
  console.log(\`Enviando email a \${to}\`)
  // Garantizado que 'to' es un email válido
}

// Uso seguro
const email = validateEmail('user@example.com')
if (email) {
  sendEmail(email, 'Hola', 'Mensaje') // ✅ OK
}

// Esto no compila:
sendEmail('invalid-email', 'Test', 'Body') // ❌ Error de tipo</code></pre>
                        </div>
                    </section>

                    <!-- Sección 5: Mejores Prácticas -->
                    <section id="mejores-practicas" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6 text-gray-800">✨ Mejores Prácticas TypeScript 5.3</h2>
                        
                        <div class="space-y-6">
                            <div class="bg-blue-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-blue-900">1. Usa Decorators para Cross-Cutting Concerns</h3>
                                <p class="text-gray-700 mb-3">
                                    Logging, validación, caché, autenticación - todo lo que cruza múltiples capas.
                                </p>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>@Cache({ ttl: 300 })
@RequireAuth()
@Log()
async getUserData(userId: string) {
  return await db.user.findUnique({ where: { id: userId } })
}</code></pre>
                                </div>
                            </div>

                            <div class="bg-purple-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-purple-900">2. Pattern Matching para Reducir Complejidad</h3>
                                <p class="text-gray-700 mb-3">
                                    Reemplaza cadenas if-else complejas con pattern matching declarativo.
                                </p>
                            </div>

                            <div class="bg-green-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-green-900">3. Branded Types en Domain Layer</h3>
                                <p class="text-gray-700 mb-3">
                                    Usa branded types para IDs, emails, URLs y otros valores del dominio.
                                </p>
                            </div>

                            <div class="bg-orange-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-orange-900">4. Activa strict Mode Siempre</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg mt-3">
                                    <pre class="text-sm"><code>// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true
  }
}</code></pre>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Conclusión -->
                    <div class="bg-gradient-to-r from-blue-600 to-purple-600 p-8 rounded-xl text-white mt-12">
                        <h2 class="text-2xl font-bold mb-4">🎯 Conclusión</h2>
                        <p class="text-lg leading-relaxed">
                            TypeScript 5.3 eleva JavaScript a nuevas alturas de seguridad y expresividad. Los Decorators, 
                            Pattern Matching y Branded Types no solo hacen el código más elegante, sino también más robusto 
                            y mantenible. Es momento de actualizar y aprovechar estas poderosas características.
                        </p>
                    </div>

                    <!-- Navegación de Artículos -->
                    <div class="flex justify-between items-center mt-12 pt-8 border-t">
                        <a href="articulo-react-19-2025.html" class="text-purple-600 hover:underline">← React 19</a>
                        <a href="../noticias.html" class="text-gray-600 hover:text-purple-600">Ver todos los artículos</a>
                        <a href="articulo-ia-generativa-2025.html" class="text-purple-600 hover:underline">IA Generativa →</a>
                    </div>
                </div>
            </article>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12 mt-20">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <p class="text-gray-400">© 2025 Mi Blog. Todos los derechos reservados.</p>
        </div>
    </footer>

    <script>
        function toggleMenu() {
            const menu = document.getElementById('mobile-menu');
            menu.classList.toggle('hidden');
        }
    </script>
</body>
</html>
"""
}

# Función para actualizar un artículo específico
def update_article_content(filename, content):
    filepath = os.path.join(articles_dir, filename)
    
    try:
        # Leer el archivo actual
        with open(filepath, 'r', encoding='utf-8') as f:
            current_content = f.read()
        
        # Encontrar donde termina el nav (buscar el div espaciador)
        nav_end = current_content.find('<!-- Espaciador para el nav fijo -->')
        
        if nav_end != -1:
            # Encontrar el final del div espaciador
            content_start = current_content.find('</div>', nav_end)
            
            if content_start != -1:
                # Mantener head y nav, reemplazar todo lo demás
                nav_section = current_content[:content_start + 6]  # +6 para incluir </div>
                
                # Crear nuevo contenido completo
                new_full_content = nav_section + '\n' + content
                
                # Guardar
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_full_content)
                
                print(f"✓ Actualizado: {filename}")
                return True
        
        print(f"✗ No se pudo encontrar la estructura en: {filename}")
        return False
        
    except Exception as e:
        print(f"✗ Error en {filename}: {str(e)}")
        return False

# Procesar los artículos
print("Creando contenido documentado para artículos...\n")

for filename, content in articles_content.items():
    update_article_content(filename, content)

print("\n✅ Proceso completado!")
