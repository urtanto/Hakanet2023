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
    <div id="aftermain"></div>
    <!-- <hack-footer class="mt-auto" /> -->
  </div>
</template>
