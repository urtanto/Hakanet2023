<template>
  <div class="flex flex-col min-h-screen">
    <SeoKit />
    <OgImageScreenshot />
    <header class="">
      <hack-navbar />
    </header>
    <main class="w-[1024px] mx-auto my-1">
      <slot />
    </main>
    <footer>
      <hack-contacts />
    </footer>
  </div>
</template>
