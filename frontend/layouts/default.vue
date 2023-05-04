<template>
  <div class="flex flex-col min-h-screen">
    <SeoKit />
    <OgImageScreenshot />
    <header class="min-[460px]:h-20 h-32 p-1 box-content">
      <hack-navbar />
    </header>
    <main class="w-[1024px] mx-auto my-1">
      <slot />
    </main>
    <!-- <hack-footer class="mt-auto" /> -->
  </div>
</template>
