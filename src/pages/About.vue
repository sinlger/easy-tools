<script setup lang="ts">
import { useHead } from '@vueuse/head';

useHead({ title: 'About - A Toolio' });
</script>

<template>
  <c-markdown :markdown="$t('about.content')" mx-auto mt-50px max-w-600px />
</template>
