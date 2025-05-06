<script setup lang="ts">
import { textToNatoAlphabet } from './text-to-nato-alphabet.service';
import { useCopy } from '@/composable/copy';
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
const input = ref('');
const natoText = computed(() => textToNatoAlphabet({ text: input.value }));
const { copy } = useCopy({ source: natoText, text: 'NATO alphabet string copied.' });
</script>

<template>
  <div>
    <c-input-text
      v-model:value="input"
      label="Your text to convert to NATO phonetic alphabet"
      placeholder="Put your text here..."
      clearable
      mb-5
    />

    <div v-if="natoText">
      <div mb-2>
        Your text in NATO phonetic alphabet
      </div>
      <c-card>
        {{ natoText }}
      </c-card>

      <div mt-3 flex justify-center>
        <c-button autofocus @click="copy()">
          Copy NATO string
        </c-button>
      </div>
    </div>
  </div>
</template>
