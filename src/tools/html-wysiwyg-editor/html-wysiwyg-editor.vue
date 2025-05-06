<script setup lang="ts">
import { format } from 'prettier';
import htmlParser from 'prettier/plugins/html';
import { useStorage } from '@vueuse/core';
import Editor from './editor/editor.vue';
import TextareaCopyable from '@/components/TextareaCopyable.vue';
import showdown from 'showdown'; // 新增showdown引入
const { t, locale } = useI18n();
const markdownHtml = ref('');
const loadMarkdown = async () => {
  const mdContent = await import(`./language/token-generator.${locale.value}.md?raw`);
  const converter = new showdown.Converter();
  markdownHtml.value = converter.makeHtml(mdContent.default);
};
watchEffect(() => {
  loadMarkdown();
});
const html = useStorage('html-wysiwyg-editor--html', '<h1>Hey!</h1><p>Welcome to this html wysiwyg editor</p>');

const formattedHtml = asyncComputed(() => format(html.value, { parser: 'html', plugins: [htmlParser] }), '');
</script>

<template>
  <Editor v-model:html="html" />
  <TextareaCopyable :value="formattedHtml" language="html" />
</template>
