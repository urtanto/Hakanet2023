<template>
  <div class="flex flex-col min-h-screen">
    <SeoKit />
    <OgImageScreenshot />
    <header class="">
      <hack-navbar />
    </header>
    <main class="">
      <slot />
    </main>
    <footer>
      <hack-contacts />
    </footer>
  </div>
</template>
