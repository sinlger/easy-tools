<script setup lang="ts">
import { evaluate } from 'mathjs';

import { withDefaultOnError } from '@/utils/defaults';
import showdown from 'showdown'; // 新增showdown引入
const { t, locale } = useI18n();
const markdownHtml = ref('');
const loadMarkdown = async () => {
  const mdContent = await import(`./language/math-evaluator.${locale.value}.md?raw`);
  const converter = new showdown.Converter();
  markdownHtml.value = converter.makeHtml(mdContent.default);
};
watchEffect(() => {
  loadMarkdown();
});
const expression = ref('');

const result = computed(() => withDefaultOnError(() => evaluate(expression.value) ?? '', ''));
</script>

<template>
  <div>
    <c-input-text
      v-model:value="expression"
      rows="1"
      multiline
      placeholder="Your math expression (ex: 2*sqrt(6) )..."
      raw-text
      monospace
      autofocus
      autosize
    />

    <c-card v-if="result !== ''" title="Result " mt-5>
      {{ result }}
    </c-card>
  </div>
  <c-card>
    <div v-html="markdownHtml"></div>
  </c-card>
</template>
