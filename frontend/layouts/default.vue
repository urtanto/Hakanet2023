<template>
  <div class="flex flex-col min-h-screen">
    <SeoKit />
    <OgImageScreenshot />
    <header class="h-20">
      <hack-navbar />
    </header>
    <main class="max-w-5xl mx-auto my-1">
      <slot />
    </main>
    <hack-footer class="mt-auto" />
  </div>
</template>
