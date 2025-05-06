<script setup lang="ts">
import showdown from 'showdown'; // 新增showdown引入
const { t, locale } = useI18n();
const markdownHtml = ref('');
const loadMarkdown = async () => {
  const mdContent = await import(`./language/text-diff.${locale.value}.md?raw`);
  const converter = new showdown.Converter();
  markdownHtml.value = converter.makeHtml(mdContent.default);
};
watchEffect(() => {
  loadMarkdown();
});
</script>
<template>
  <c-card w-full important:flex-1 important:pa-0>
    <c-diff-editor />
  </c-card>
  <c-card>
    <div v-html="markdownHtml"></div>
  </c-card>
</template>