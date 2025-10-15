import os

articles_dir = r"c:\Users\angeh\Desktop\primera pagina\pages\articles"

# Últimos 2 artículos
last_articles = {
    "articulo-mobile-first.html": """
    <main class="bg-gray-50 py-12">
        <div class="max-w-4xl mx-auto px-4">
            <article class="bg-white rounded-2xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-cyan-500 to-blue-600 p-8 text-white">
                    <div class="flex items-center space-x-2 text-sm mb-4">
                        <a href="../../index.html" class="hover:underline">Inicio</a>
                        <span>›</span>
                        <a href="../noticias.html" class="hover:underline">Blog</a>
                        <span>›</span>
                        <span>Mobile First</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold mb-4">Mobile First: Diseño Responsivo Moderno</h1>
                    <div class="flex items-center space-x-4 text-sm">
                        <span>📅 15 de Octubre, 2025</span>
                        <span>⏱️ 18 min lectura</span>
                    </div>
                </div>

                <div class="relative h-96 overflow-hidden">
                    <img src="../../imagenes/5.jpg" alt="Mobile First" class="w-full h-full object-cover">
                </div>

                <div class="p-8 md:p-12">
                    <div class="bg-cyan-50 border-l-4 border-cyan-600 p-6 rounded-r-lg mb-8">
                        <p class="text-lg leading-relaxed text-gray-700">
                            El enfoque <strong>Mobile First</strong> consiste en diseñar primero para dispositivos móviles 
                            y luego escalar a pantallas más grandes. Aprende a crear experiencias perfectas en todos los dispositivos.
                        </p>
                    </div>

                    <div class="bg-gray-50 p-6 rounded-xl mb-8">
                        <h2 class="text-2xl font-bold mb-4">📋 Contenido</h2>
                        <ul class="space-y-2">
                            <li><a href="#que-es" class="text-cyan-600 hover:underline">1. ¿Qué es Mobile First?</a></li>
                            <li><a href="#viewport" class="text-cyan-600 hover:underline">2. Viewport y Meta Tags</a></li>
                            <li><a href="#breakpoints" class="text-cyan-600 hover:underline">3. Breakpoints Estratégicos</a></li>
                            <li><a href="#tecnicas" class="text-cyan-600 hover:underline">4. Técnicas Responsivas</a></li>
                            <li><a href="#performance" class="text-cyan-600 hover:underline">5. Performance Móvil</a></li>
                            <li><a href="#testing" class="text-cyan-600 hover:underline">6. Testing en Dispositivos</a></li>
                        </ul>
                    </div>

                    <section id="que-es" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📱 ¿Qué es Mobile First?</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Mobile First es una metodología de diseño web que prioriza la experiencia móvil desde el inicio 
                            del proyecto, en lugar de adaptar un diseño desktop a móvil posteriormente.
                        </p>

                        <div class="bg-blue-50 p-6 rounded-xl mb-6">
                            <h3 class="text-xl font-bold mb-3 text-blue-900">📊 Estadísticas Clave (2025)</h3>
                            <ul class="space-y-2 text-gray-700">
                                <li class="flex items-start"><span class="text-blue-600 mr-2">•</span> 68% del tráfico web proviene de dispositivos móviles</li>
                                <li class="flex items-start"><span class="text-blue-600 mr-2">•</span> Google usa Mobile-First Indexing desde 2019</li>
                                <li class="flex items-start"><span class="text-blue-600 mr-2">•</span> 53% de usuarios abandonan sitios que tardan +3 segundos en móvil</li>
                                <li class="flex items-start"><span class="text-blue-600 mr-2">•</span> 88% de usuarios no vuelven a un sitio con mala experiencia móvil</li>
                            </ul>
                        </div>

                        <div class="grid md:grid-cols-2 gap-6 mb-6">
                            <div class="bg-red-50 p-6 rounded-xl border-2 border-red-200">
                                <h3 class="text-xl font-bold mb-3 text-red-900">❌ Enfoque Desktop First</h3>
                                <ul class="space-y-2 text-gray-700">
                                    <li>1. Diseñar para desktop</li>
                                    <li>2. Reducir elementos para tablet</li>
                                    <li>3. Comprimir para móvil</li>
                                    <li>4. Problemas de usabilidad</li>
                                </ul>
                            </div>
                            <div class="bg-green-50 p-6 rounded-xl border-2 border-green-200">
                                <h3 class="text-xl font-bold mb-3 text-green-900">✅ Enfoque Mobile First</h3>
                                <ul class="space-y-2 text-gray-700">
                                    <li>1. Diseñar para móvil (esencial)</li>
                                    <li>2. Mejorar para tablet</li>
                                    <li>3. Expandir para desktop</li>
                                    <li>4. Experiencia optimizada</li>
                                </ul>
                            </div>
                        </div>
                    </section>

                    <section id="viewport" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🖼️ Viewport y Meta Tags</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            El viewport meta tag es esencial para que tu sitio se vea correctamente en dispositivos móviles.
                        </p>

                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="es"&gt;
&lt;head&gt;
  &lt;meta charset="UTF-8"&gt;
  
  &lt;!-- Viewport esencial --&gt;
  &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
  
  &lt;!-- Para iOS --&gt;
  &lt;meta name="apple-mobile-web-app-capable" content="yes"&gt;
  &lt;meta name="apple-mobile-web-app-status-bar-style" content="black"&gt;
  
  &lt;!-- Para Android --&gt;
  &lt;meta name="theme-color" content="#3b82f6"&gt;
  
  &lt;title&gt;Mi Sitio Mobile First&lt;/title&gt;
&lt;/head&gt;</code></pre>
                        </div>

                        <div class="bg-yellow-50 border-l-4 border-yellow-500 p-6 rounded-r-lg">
                            <h4 class="font-bold text-yellow-900 mb-2">⚠️ Evita Estos Errores</h4>
                            <div class="bg-gray-900 text-white p-4 rounded-lg mt-3">
                                <pre class="text-sm"><code>&lt;!-- ❌ NO hacer esto --&gt;
&lt;meta name="viewport" content="width=1024"&gt;
&lt;meta name="viewport" content="user-scalable=no"&gt;

&lt;!-- ✅ Correcto --&gt;
&lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;</code></pre>
                            </div>
                        </div>
                    </section>

                    <section id="breakpoints" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📏 Breakpoints Estratégicos</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            Los breakpoints definen dónde cambia el diseño según el tamaño de pantalla.
                        </p>

                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>/* Sistema de Breakpoints Moderno (2025) */

/* Mobile (base) - 320px a 639px */
.contenedor {
  padding: 1rem;
  font-size: 16px;
}

/* Tablet - 640px en adelante */
@media (min-width: 640px) {
  .contenedor {
    padding: 1.5rem;
    max-width: 640px;
    margin: 0 auto;
  }
}

/* Tablet grande - 768px en adelante */
@media (min-width: 768px) {
  .contenedor {
    max-width: 768px;
    padding: 2rem;
  }
}

/* Desktop - 1024px en adelante */
@media (min-width: 1024px) {
  .contenedor {
    max-width: 1024px;
    padding: 3rem;
  }
}

/* Desktop grande - 1280px en adelante */
@media (min-width: 1280px) {
  .contenedor {
    max-width: 1280px;
  }
}

/* Ultra wide - 1536px en adelante */
@media (min-width: 1536px) {
  .contenedor {
    max-width: 1536px;
  }
}</code></pre>
                        </div>

                        <div class="bg-purple-50 p-6 rounded-xl">
                            <h3 class="text-xl font-bold mb-3 text-purple-900">💡 Breakpoints Basados en Contenido</h3>
                            <p class="text-gray-700 mb-3">
                                En lugar de usar breakpoints fijos, considera breakpoints basados en cuándo el diseño necesita cambiar:
                            </p>
                            <div class="bg-gray-900 text-white p-4 rounded-lg">
                                <pre class="text-sm"><code>/* Cambia cuando el contenido lo necesite */
.navegacion {
  /* Móvil: menú vertical */
  flex-direction: column;
}

/* Cuando hay espacio para horizontal */
@media (min-width: 600px) {
  .navegacion {
    flex-direction: row;
  }
}</code></pre>
                            </div>
                        </div>
                    </section>

                    <section id="tecnicas" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🎨 Técnicas Responsivas</h2>
                        
                        <h3 class="text-2xl font-bold mb-4">1. Imágenes Responsivas</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>&lt;!-- Imágenes fluidas --&gt;
img {
  max-width: 100%;
  height: auto;
}

&lt;!-- Picture element para diferentes tamaños --&gt;
&lt;picture&gt;
  &lt;source media="(min-width: 1024px)" srcset="hero-large.jpg"&gt;
  &lt;source media="(min-width: 768px)" srcset="hero-medium.jpg"&gt;
  &lt;img src="hero-small.jpg" alt="Hero"&gt;
&lt;/picture&gt;

&lt;!-- Srcset para diferentes resoluciones --&gt;
&lt;img 
  src="logo.png"
  srcset="logo.png 1x, logo@2x.png 2x, logo@3x.png 3x"
  alt="Logo"
&gt;</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">2. Tipografía Fluida</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>/* Tamaño de fuente fluido con clamp() */
h1 {
  font-size: clamp(2rem, 5vw, 4rem);
  /* Mínimo 2rem, preferido 5vw, máximo 4rem */
}

p {
  font-size: clamp(1rem, 2.5vw, 1.125rem);
  line-height: 1.6;
}

/* Con calc() y vw */
.titulo {
  font-size: calc(1.5rem + 2vw);
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">3. Grid Responsivo</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>/* Grid que se adapta automáticamente */
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

/* Mobile: 1 columna, Tablet: 2, Desktop: 3 */
.grid-responsive {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 640px) {
  .grid-responsive {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid-responsive {
    grid-template-columns: repeat(3, 1fr);
  }
}</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">4. Menú Hamburguesa</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>&lt;!-- HTML --&gt;
&lt;nav class="navbar"&gt;
  &lt;div class="logo"&gt;Mi Sitio&lt;/div&gt;
  &lt;button class="menu-toggle" id="menuToggle"&gt;
    &lt;span&gt;&lt;/span&gt;
    &lt;span&gt;&lt;/span&gt;
    &lt;span&gt;&lt;/span&gt;
  &lt;/button&gt;
  &lt;ul class="menu" id="menu"&gt;
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
  padding: 1rem;
}

.menu {
  display: none; /* Oculto en móvil */
}

.menu.active {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 60px;
  left: 0;
  right: 0;
  background: white;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.menu-toggle {
  display: block;
}

/* Desktop */
@media (min-width: 768px) {
  .menu {
    display: flex !important;
    flex-direction: row;
    position: static;
    box-shadow: none;
    gap: 2rem;
  }
  
  .menu-toggle {
    display: none;
  }
}

// JavaScript
document.getElementById('menuToggle').addEventListener('click', () => {
  document.getElementById('menu').classList.toggle('active')
})</code></pre>
                        </div>
                    </section>

                    <section id="performance" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">⚡ Performance Móvil</h2>
                        
                        <div class="space-y-6">
                            <div class="bg-blue-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-blue-900">1. Optimizar Imágenes</h3>
                                <ul class="space-y-2 text-gray-700">
                                    <li class="flex items-start"><span class="text-blue-600 mr-2">✓</span> Usa formatos modernos (WebP, AVIF)</li>
                                    <li class="flex items-start"><span class="text-blue-600 mr-2">✓</span> Lazy loading para imágenes below the fold</li>
                                    <li class="flex items-start"><span class="text-blue-600 mr-2">✓</span> Comprime imágenes (TinyPNG, Squoosh)</li>
                                    <li class="flex items-start"><span class="text-blue-600 mr-2">✓</span> Usa CDN para servir imágenes</li>
                                </ul>
                                <div class="bg-gray-900 text-white p-4 rounded-lg mt-3">
                                    <pre class="text-sm"><code>&lt;img 
  src="imagen.webp" 
  loading="lazy"
  alt="Descripción"
&gt;</code></pre>
                                </div>
                            </div>

                            <div class="bg-purple-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-purple-900">2. Minimizar JavaScript</h3>
                                <ul class="space-y-2 text-gray-700">
                                    <li class="flex items-start"><span class="text-purple-600 mr-2">✓</span> Carga solo el JS necesario</li>
                                    <li class="flex items-start"><span class="text-purple-600 mr-2">✓</span> Code splitting por rutas</li>
                                    <li class="flex items-start"><span class="text-purple-600 mr-2">✓</span> Defer o async para scripts no críticos</li>
                                </ul>
                            </div>

                            <div class="bg-green-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-green-900">3. Critical CSS</h3>
                                <p class="text-gray-700 mb-3">Inline el CSS crítico para First Paint rápido:</p>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>&lt;head&gt;
  &lt;style&gt;
    /* CSS crítico inline */
    body { margin: 0; font-family: sans-serif; }
    .hero { min-height: 100vh; }
  &lt;/style&gt;
  
  &lt;!-- CSS completo diferido --&gt;
  &lt;link rel="preload" href="styles.css" as="style"&gt;
  &lt;link rel="stylesheet" href="styles.css" media="print" onload="this.media='all'"&gt;
&lt;/head&gt;</code></pre>
                                </div>
                            </div>
                        </div>
                    </section>

                    <section id="testing" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🧪 Testing en Dispositivos</h2>
                        
                        <div class="bg-gray-50 p-6 rounded-xl mb-6">
                            <h3 class="text-xl font-bold mb-3">Herramientas de Testing</h3>
                            <ul class="space-y-3">
                                <li class="flex items-start">
                                    <div class="bg-blue-500 text-white rounded-full p-2 mr-3 mt-1">🔧</div>
                                    <div>
                                        <strong>Chrome DevTools</strong>
                                        <p class="text-gray-600">F12 → Toggle device toolbar (Ctrl+Shift+M)</p>
                                    </div>
                                </li>
                                <li class="flex items-start">
                                    <div class="bg-green-500 text-white rounded-full p-2 mr-3 mt-1">📱</div>
                                    <div>
                                        <strong>BrowserStack</strong>
                                        <p class="text-gray-600">Prueba en dispositivos reales remotos</p>
                                    </div>
                                </li>
                                <li class="flex items-start">
                                    <div class="bg-purple-500 text-white rounded-full p-2 mr-3 mt-1">⚡</div>
                                    <div>
                                        <strong>Google Lighthouse</strong>
                                        <p class="text-gray-600">Auditoría de performance móvil</p>
                                    </div>
                                </li>
                                <li class="flex items-start">
                                    <div class="bg-orange-500 text-white rounded-full p-2 mr-3 mt-1">🎯</div>
                                    <div>
                                        <strong>Responsively App</strong>
                                        <p class="text-gray-600">Vista de múltiples dispositivos simultáneamente</p>
                                    </div>
                                </li>
                            </ul>
                        </div>

                        <div class="bg-yellow-50 border-l-4 border-yellow-500 p-6 rounded-r-lg">
                            <h4 class="font-bold text-yellow-900 mb-2">✅ Checklist Mobile First</h4>
                            <ul class="space-y-2 text-gray-700">
                                <li class="flex items-start"><input type="checkbox" class="mr-2 mt-1"> Viewport meta tag configurado</li>
                                <li class="flex items-start"><input type="checkbox" class="mr-2 mt-1"> Imágenes responsivas y optimizadas</li>
                                <li class="flex items-start"><input type="checkbox" class="mr-2 mt-1"> Texto legible sin zoom (16px mínimo)</li>
                                <li class="flex items-start"><input type="checkbox" class="mr-2 mt-1"> Botones táctiles de 44x44px mínimo</li>
                                <li class="flex items-start"><input type="checkbox" class="mr-2 mt-1"> Formularios optimizados para móvil</li>
                                <li class="flex items-start"><input type="checkbox" class="mr-2 mt-1"> Navegación touch-friendly</li>
                                <li class="flex items-start"><input type="checkbox" class="mr-2 mt-1"> Tiempo de carga &lt;3 segundos</li>
                                <li class="flex items-start"><input type="checkbox" class="mr-2 mt-1"> Lighthouse score &gt;90</li>
                            </ul>
                        </div>
                    </section>

                    <div class="bg-gradient-to-r from-cyan-500 to-blue-600 p-8 rounded-xl text-white mt-12">
                        <h2 class="text-2xl font-bold mb-4">🎯 Conclusión</h2>
                        <p class="text-lg leading-relaxed">
                            Mobile First no es solo una técnica, es una mentalidad que prioriza la mayoría de tus usuarios. 
                            Diseñar para móvil primero resulta en sitios más rápidos, accesibles y eficientes en todos los dispositivos. 
                            En 2025, no es opcional: es esencial.
                        </p>
                    </div>

                    <div class="flex justify-between items-center mt-12 pt-8 border-t">
                        <a href="articulo-ia-generativa-2025.html" class="text-cyan-600 hover:underline">← IA Generativa</a>
                        <a href="../noticias.html" class="text-gray-600 hover:text-cyan-600">Ver todos</a>
                        <a href="articulo-css-moderno.html" class="text-cyan-600 hover:underline">CSS Moderno →</a>
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

    "articulo-ia-generativa-2025.html": """
    <main class="bg-gray-50 py-12">
        <div class="max-w-4xl mx-auto px-4">
            <article class="bg-white rounded-2xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-violet-600 to-fuchsia-600 p-8 text-white">
                    <div class="flex items-center space-x-2 text-sm mb-4">
                        <a href="../../index.html" class="hover:underline">Inicio</a>
                        <span>›</span>
                        <a href="../noticias.html" class="hover:underline">Blog</a>
                        <span>›</span>
                        <span>IA Generativa 2025</span>
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold mb-4">IA Generativa 2025: Guía Completa para Desarrolladores</h1>
                    <div class="flex items-center space-x-4 text-sm">
                        <span>📅 15 de Octubre, 2025</span>
                        <span>⏱️ 30 min lectura</span>
                    </div>
                </div>

                <div class="relative h-96 overflow-hidden">
                    <img src="../../imagenes/6.jpg" alt="IA Generativa" class="w-full h-full object-cover">
                </div>

                <div class="p-8 md:p-12">
                    <div class="bg-violet-50 border-l-4 border-violet-600 p-6 rounded-r-lg mb-8">
                        <p class="text-lg leading-relaxed text-gray-700">
                            La <strong>Inteligencia Artificial Generativa</strong> está revolucionando el desarrollo de software. 
                            Aprende a integrar modelos de lenguaje, generación de imágenes y código en tus aplicaciones con GPT-4, 
                            Claude, Stable Diffusion y más.
                        </p>
                    </div>

                    <div class="bg-gray-50 p-6 rounded-xl mb-8">
                        <h2 class="text-2xl font-bold mb-4">📋 Contenido</h2>
                        <ul class="space-y-2">
                            <li><a href="#introduccion" class="text-violet-600 hover:underline">1. Introducción a IA Generativa</a></li>
                            <li><a href="#modelos" class="text-violet-600 hover:underline">2. Modelos Principales 2025</a></li>
                            <li><a href="#apis" class="text-violet-600 hover:underline">3. Integrar APIs de IA</a></li>
                            <li><a href="#prompts" class="text-violet-600 hover:underline">4. Prompt Engineering</a></li>
                            <li><a href="#casos-uso" class="text-violet-600 hover:underline">5. Casos de Uso Prácticos</a></li>
                            <li><a href="#etica" class="text-violet-600 hover:underline">6. Ética y Mejores Prácticas</a></li>
                        </ul>
                    </div>

                    <section id="introduccion" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🤖 ¿Qué es la IA Generativa?</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            La IA Generativa se refiere a sistemas de inteligencia artificial capaces de crear contenido nuevo: 
                            texto, código, imágenes, audio, video y más, a partir de instrucciones en lenguaje natural.
                        </p>

                        <div class="grid md:grid-cols-2 gap-6 mb-8">
                            <div class="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl border-2 border-blue-200">
                                <div class="text-4xl mb-3">💬</div>
                                <h3 class="text-xl font-bold mb-2 text-blue-900">LLMs (Large Language Models)</h3>
                                <p class="text-gray-700">GPT-4, Claude, Gemini - Texto, código, análisis</p>
                            </div>
                            <div class="bg-gradient-to-br from-purple-50 to-purple-100 p-6 rounded-xl border-2 border-purple-200">
                                <div class="text-4xl mb-3">🎨</div>
                                <h3 class="text-xl font-bold mb-2 text-purple-900">Generación de Imágenes</h3>
                                <p class="text-gray-700">Midjourney, DALL-E 3, Stable Diffusion</p>
                            </div>
                            <div class="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl border-2 border-green-200">
                                <div class="text-4xl mb-3">🎵</div>
                                <h3 class="text-xl font-bold mb-2 text-green-900">Audio y Música</h3>
                                <p class="text-gray-700">Suno, ElevenLabs - Voces, música generada</p>
                            </div>
                            <div class="bg-gradient-to-br from-orange-50 to-orange-100 p-6 rounded-xl border-2 border-orange-200">
                                <div class="text-4xl mb-3">🎥</div>
                                <h3 class="text-xl font-bold mb-2 text-orange-900">Video</h3>
                                <p class="text-gray-700">Runway, Sora - Generación de video</p>
                            </div>
                        </div>
                    </section>

                    <section id="modelos" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🌟 Modelos Principales 2025</h2>
                        
                        <div class="space-y-6">
                            <div class="bg-white p-6 rounded-xl border-2 border-gray-200">
                                <div class="flex items-center justify-between mb-4">
                                    <h3 class="text-2xl font-bold text-gray-800">GPT-4 Turbo (OpenAI)</h3>
                                    <span class="bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm font-bold">Líder</span>
                                </div>
                                <p class="text-gray-700 mb-4">
                                    Modelo más avanzado para texto y código. 128K tokens de contexto, multimodal (texto + imágenes).
                                </p>
                                <div class="grid md:grid-cols-3 gap-4 text-sm">
                                    <div class="bg-blue-50 p-3 rounded">
                                        <strong>Contexto:</strong> 128K tokens
                                    </div>
                                    <div class="bg-purple-50 p-3 rounded">
                                        <strong>Costo:</strong> $0.01/1K tokens
                                    </div>
                                    <div class="bg-green-50 p-3 rounded">
                                        <strong>Uso:</strong> Chatbots, análisis, código
                                    </div>
                                </div>
                            </div>

                            <div class="bg-white p-6 rounded-xl border-2 border-gray-200">
                                <div class="flex items-center justify-between mb-4">
                                    <h3 class="text-2xl font-bold text-gray-800">Claude 3 Opus (Anthropic)</h3>
                                    <span class="bg-purple-100 text-purple-800 px-3 py-1 rounded-full text-sm font-bold">Premium</span>
                                </div>
                                <p class="text-gray-700 mb-4">
                                    Excelente para razonamiento complejo y análisis largo. 200K tokens de contexto.
                                </p>
                                <div class="grid md:grid-cols-3 gap-4 text-sm">
                                    <div class="bg-blue-50 p-3 rounded">
                                        <strong>Contexto:</strong> 200K tokens
                                    </div>
                                    <div class="bg-purple-50 p-3 rounded">
                                        <strong>Costo:</strong> $0.015/1K tokens
                                    </div>
                                    <div class="bg-green-50 p-3 rounded">
                                        <strong>Uso:</strong> Análisis, investigación
                                    </div>
                                </div>
                            </div>

                            <div class="bg-white p-6 rounded-xl border-2 border-gray-200">
                                <div class="flex items-center justify-between mb-4">
                                    <h3 class="text-2xl font-bold text-gray-800">Gemini Ultra (Google)</h3>
                                    <span class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-bold">Multimodal</span>
                                </div>
                                <p class="text-gray-700 mb-4">
                                    Nativo multimodal: texto, imágenes, audio, video en un solo modelo.
                                </p>
                                <div class="grid md:grid-cols-3 gap-4 text-sm">
                                    <div class="bg-blue-50 p-3 rounded">
                                        <strong>Contexto:</strong> 1M tokens
                                    </div>
                                    <div class="bg-purple-50 p-3 rounded">
                                        <strong>Costo:</strong> $0.007/1K tokens
                                    </div>
                                    <div class="bg-green-50 p-3 rounded">
                                        <strong>Uso:</strong> Todo tipo de contenido
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <section id="apis" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">🔌 Integrar APIs de IA</h2>
                        
                        <h3 class="text-2xl font-bold mb-4">OpenAI API (GPT-4)</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>// Instalar SDK
npm install openai

// Usar la API
import OpenAI from 'openai'

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
})

async function chat(mensaje) {
  const completion = await openai.chat.completions.create({
    model: "gpt-4-turbo",
    messages: [
      {
        role: "system",
        content: "Eres un asistente útil y profesional."
      },
      {
        role: "user",
        content: mensaje
      }
    ],
    temperature: 0.7,
    max_tokens: 500
  })
  
  return completion.choices[0].message.content
}

// Usar
const respuesta = await chat("Explica qué es React")
console.log(respuesta)</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Streaming de Respuestas</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>async function chatStream(mensaje) {
  const stream = await openai.chat.completions.create({
    model: "gpt-4-turbo",
    messages: [{ role: "user", content: mensaje }],
    stream: true
  })
  
  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content || ''
    process.stdout.write(content)
  }
}

await chatStream("Escribe un poema sobre JavaScript")</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Generación de Imágenes (DALL-E 3)</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>async function generarImagen(prompt) {
  const response = await openai.images.generate({
    model: "dall-e-3",
    prompt: prompt,
    size: "1024x1024",
    quality: "hd",
    n: 1
  })
  
  return response.data[0].url
}

const url = await generarImagen(
  "Un desarrollador programando en una oficina futurista, estilo cyberpunk"
)
console.log(url)</code></pre>
                        </div>

                        <h3 class="text-2xl font-bold mb-4">Análisis de Imágenes (Vision)</h3>
                        <div class="bg-gray-900 text-white p-6 rounded-xl mb-6">
                            <pre class="text-sm"><code>async function analizarImagen(imagenUrl, pregunta) {
  const response = await openai.chat.completions.create({
    model: "gpt-4-vision-preview",
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: pregunta },
          { type: "image_url", image_url: { url: imagenUrl } }
        ]
      }
    ]
  })
  
  return response.choices[0].message.content
}

const analisis = await analizarImagen(
  "https://ejemplo.com/interfaz.png",
  "¿Qué problemas de UX tiene esta interfaz?"
)</code></pre>
                        </div>
                    </section>

                    <section id="prompts" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">📝 Prompt Engineering</h2>
                        
                        <p class="text-lg mb-6 text-gray-700">
                            El Prompt Engineering es el arte de escribir instrucciones efectivas para obtener los mejores resultados de los modelos de IA.
                        </p>

                        <h3 class="text-2xl font-bold mb-4">Técnicas Fundamentales</h3>
                        
                        <div class="space-y-6">
                            <div class="bg-blue-50 p-6 rounded-xl">
                                <h4 class="text-xl font-bold mb-3 text-blue-900">1. Ser Específico</h4>
                                <div class="grid md:grid-cols-2 gap-4">
                                    <div class="bg-red-50 p-4 rounded border-l-4 border-red-500">
                                        <p class="font-bold text-red-900 mb-2">❌ Vago</p>
                                        <p class="text-gray-700">"Crea una función"</p>
                                    </div>
                                    <div class="bg-green-50 p-4 rounded border-l-4 border-green-500">
                                        <p class="font-bold text-green-900 mb-2">✅ Específico</p>
                                        <p class="text-gray-700">"Crea una función en TypeScript que valide emails usando regex y retorne boolean"</p>
                                    </div>
                                </div>
                            </div>

                            <div class="bg-purple-50 p-6 rounded-xl">
                                <h4 class="text-xl font-bold mb-3 text-purple-900">2. Dar Contexto</h4>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>Eres un experto desarrollador senior con 10 años de experiencia en React.
Estoy construyendo una app de e-commerce con Next.js 15.
Necesito un componente de carrito de compras que:
- Maneje estado con Zustand
- Persista en localStorage
- Muestre total con descuentos
- Sea accesible (ARIA)

Genera el código completo con TypeScript y comentarios explicativos.</code></pre>
                                </div>
                            </div>

                            <div class="bg-green-50 p-6 rounded-xl">
                                <h4 class="text-xl font-bold mb-3 text-green-900">3. Few-Shot Learning</h4>
                                <p class="text-gray-700 mb-3">Proporciona ejemplos de lo que quieres:</p>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>Convierte estas descripciones en código SQL:

Ejemplo 1:
Input: "Usuarios que se registraron hoy"
Output: SELECT * FROM users WHERE DATE(created_at) = CURDATE()

Ejemplo 2:
Input: "Posts con más de 100 likes"
Output: SELECT * FROM posts WHERE likes > 100

Ahora hazlo con:
Input: "Productos sin stock ordenados por precio"
Output:</code></pre>
                                </div>
                            </div>

                            <div class="bg-orange-50 p-6 rounded-xl">
                                <h4 class="text-xl font-bold mb-3 text-orange-900">4. Chain of Thought</h4>
                                <p class="text-gray-700 mb-3">Pide que piense paso a paso:</p>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>Analiza este código y encuentra el bug.
Piensa paso a paso:
1. Identifica qué hace el código
2. Analiza cada línea
3. Encuentra posibles errores
4. Explica la solución

[código aquí]</code></pre>
                                </div>
                            </div>
                        </div>
                    </section>

                    <section id="casos-uso" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">💡 Casos de Uso Prácticos</h2>
                        
                        <div class="space-y-6">
                            <div class="bg-white p-6 rounded-xl border-2 border-gray-200">
                                <h3 class="text-xl font-bold mb-3">1. Chatbot de Soporte</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>const systemPrompt = \`
Eres un asistente de soporte técnico para nuestra app.
Base de conocimientos:
- Pricing: $19/mes básico, $49/mes pro
- Reset password: Click "Forgot password" en login
- Contact: support@miapp.com

Responde de forma amigable y concisa.
Si no sabes algo, deriva a soporte humano.
\`

async function handleSupportChat(userMessage) {
  const response = await openai.chat.completions.create({
    model: "gpt-4-turbo",
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: userMessage }
    ]
  })
  
  return response.choices[0].message.content
}</code></pre>
                                </div>
                            </div>

                            <div class="bg-white p-6 rounded-xl border-2 border-gray-200">
                                <h3 class="text-xl font-bold mb-3">2. Generador de Contenido SEO</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>async function generarArticuloSEO(keyword, outline) {
  const prompt = \`
Escribe un artículo de blog SEO-optimizado:

Keyword principal: "${keyword}"
Estructura: ${outline}

Requisitos:
- 1500 palabras mínimo
- H2 y H3 bien estructurados
- Meta descripción (150 caracteres)
- Keywords naturalmente integradas
- Tono profesional pero accesible
- Incluye llamados a la acción
  \`
  
  const article = await openai.chat.completions.create({
    model: "gpt-4-turbo",
    messages: [{ role: "user", content: prompt }],
    temperature: 0.7,
    max_tokens: 3000
  })
  
  return article.choices[0].message.content
}</code></pre>
                                </div>
                            </div>

                            <div class="bg-white p-6 rounded-xl border-2 border-gray-200">
                                <h3 class="text-xl font-bold mb-3">3. Code Review Automático</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>async function reviewCode(codigo) {
  const prompt = \`
Revisa este código y proporciona:
1. Bugs potenciales
2. Mejoras de performance
3. Seguridad
4. Best practices violadas
5. Sugerencias de refactoring

Código:
\`\`\`
${codigo}
\`\`\`

Formato de respuesta en JSON:
{
  "bugs": [],
  "performance": [],
  "security": [],
  "bestPractices": [],
  "suggestions": []
}
  \`
  
  const review = await openai.chat.completions.create({
    model: "gpt-4-turbo",
    messages: [{ role: "user", content: prompt }],
    response_format: { type: "json_object" }
  })
  
  return JSON.parse(review.choices[0].message.content)
}</code></pre>
                                </div>
                            </div>
                        </div>
                    </section>

                    <section id="etica" class="mb-12">
                        <h2 class="text-3xl font-bold mb-6">⚖️ Ética y Mejores Prácticas</h2>
                        
                        <div class="space-y-6">
                            <div class="bg-red-50 border-l-4 border-red-500 p-6 rounded-r-lg">
                                <h3 class="text-xl font-bold mb-3 text-red-900">🚫 Evita</h3>
                                <ul class="space-y-2 text-gray-700">
                                    <li class="flex items-start"><span class="text-red-600 mr-2">✗</span> Usar IA para generar desinformación</li>
                                    <li class="flex items-start"><span class="text-red-600 mr-2">✗</span> Procesar datos sensibles sin encriptación</li>
                                    <li class="flex items-start"><span class="text-red-600 mr-2">✗</span> Presentar contenido IA como humano sin disclosure</li>
                                    <li class="flex items-start"><span class="text-red-600 mr-2">✗</span> Reemplazar completamente el juicio humano en decisiones críticas</li>
                                </ul>
                            </div>

                            <div class="bg-green-50 border-l-4 border-green-500 p-6 rounded-r-lg">
                                <h3 class="text-xl font-bold mb-3 text-green-900">✅ Mejores Prácticas</h3>
                                <ul class="space-y-2 text-gray-700">
                                    <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Sé transparente sobre el uso de IA</li>
                                    <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Valida y verifica las respuestas de IA</li>
                                    <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Implementa rate limiting y moderación</li>
                                    <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Protege la privacidad del usuario</li>
                                    <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Monitorea costos y uso</li>
                                    <li class="flex items-start"><span class="text-green-600 mr-2">✓</span> Ten un plan de fallback si la API falla</li>
                                </ul>
                            </div>

                            <div class="bg-blue-50 p-6 rounded-xl">
                                <h3 class="text-xl font-bold mb-3 text-blue-900">💰 Optimización de Costos</h3>
                                <div class="bg-gray-900 text-white p-4 rounded-lg">
                                    <pre class="text-sm"><code>// Cache de respuestas
const cache = new Map()

async function chatWithCache(mensaje) {
  const cacheKey = mensaje.toLowerCase().trim()
  
  if (cache.has(cacheKey)) {
    return cache.get(cacheKey)
  }
  
  const respuesta = await chat(mensaje)
  cache.set(cacheKey, respuesta)
  
  return respuesta
}

// Limitar tokens
const response = await openai.chat.completions.create({
  model: "gpt-4-turbo",
  messages: messages,
  max_tokens: 500,  // Limita costo
  temperature: 0.7
})</code></pre>
                                </div>
                            </div>
                        </div>
                    </section>

                    <div class="bg-gradient-to-r from-violet-600 to-fuchsia-600 p-8 rounded-xl text-white mt-12">
                        <h2 class="text-2xl font-bold mb-4">🎯 Conclusión</h2>
                        <p class="text-lg leading-relaxed">
                            La IA Generativa está transformando el desarrollo de software. Desde chatbots hasta análisis de código, 
                            las posibilidades son infinitas. Lo importante es usarla éticamente, entender sus limitaciones y 
                            combinarla con el juicio humano. En 2025, dominar estas herramientas es esencial para cualquier desarrollador.
                        </p>
                    </div>

                    <div class="flex justify-between items-center mt-12 pt-8 border-t">
                        <a href="articulo-typescript-53-2025.html" class="text-violet-600 hover:underline">← TypeScript 5.3</a>
                        <a href="../noticias.html" class="text-gray-600 hover:text-violet-600">Ver todos</a>
                        <a href="articulo-mobile-first.html" class="text-violet-600 hover:underline">Mobile First →</a>
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

print("Actualizando Mobile First e IA Generativa...\n")

for filename, content in last_articles.items():
    update_article_content(filename, content)

print("\n🎉 ¡TODOS LOS ARTÍCULOS COMPLETADOS!")
