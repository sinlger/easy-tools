<script setup lang="ts">
import { generateNumeronym } from './numeronym-generator.service';
import showdown from 'showdown'; // 新增showdown引入
const { t, locale } = useI18n();
const markdownHtml = ref('');
const loadMarkdown = async () => {
  const mdContent = await import(`./language/numeronym-generator.${locale.value}.md?raw`);
  const converter = new showdown.Converter();
  markdownHtml.value = converter.makeHtml(mdContent.default);
};
watchEffect(() => {
  loadMarkdown();
});
const word = ref('');

const numeronym = computed(() => generateNumeronym(word.value));
</script>

<template>
  <div flex flex-col items-center gap-4>
    <c-input-text v-model:value="word" placeholder="Enter a word, e.g. 'internationalization'" size="large" clearable test-id="word-input" />

    <icon-mdi-arrow-down text-30px />

    <input-copyable :value="numeronym" size="large" readonly placeholder="Your numeronym will be here, e.g. 'i18n'" test-id="numeronym" />
  </div>
    <c-card>
      <div v-html="markdownHtml"></div>
    </c-card>
</template>
