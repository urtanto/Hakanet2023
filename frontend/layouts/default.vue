<template>
  <div class="flex flex-col min-h-screen">
    <SeoKit />
    <OgImageScreenshot />
    <header class="h-20 bg-blue-400 text-white flex items-center justify-center px-4">
      <Navbar />
    </header>
    <main class="max-w-5xl mx-auto my-1">
      <slot />
    </main>
    <Footer class="mt-auto" />
  </div>
</template>
