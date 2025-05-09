<script setup lang="ts">
import { convertTextToUnicode, convertUnicodeToText } from './text-to-unicode.service';
import { useCopy } from '@/composable/copy';
import showdown from 'showdown';
import { useI18n } from 'vue-i18n';
const { locale } = useI18n();
const markdownHtml = ref('');
const loadMarkdown = async () => {
  const mdContent = await import(`./language/text-to-unicode.${locale.value}.md?raw`);
  const converter = new showdown.Converter();
  markdownHtml.value = converter.makeHtml(mdContent.default);
};
watchEffect(() => {
  loadMarkdown();
});
const inputText = ref('');
const unicodeFromText = computed(() => (inputText.value.trim() === '' ? '' : convertTextToUnicode(inputText.value)));
const { copy: copyUnicode } = useCopy({ source: unicodeFromText });

const inputUnicode = ref('');
const textFromUnicode = computed(() =>
  inputUnicode.value.trim() === '' ? '' : convertUnicodeToText(inputUnicode.value),
);
const { copy: copyText } = useCopy({ source: textFromUnicode });
</script>

<template>
  <c-card title="Text to Unicode">
    <c-input-text v-model:value="inputText" multiline placeholder="e.g. 'Hello Avengers'"
      label="Enter text to convert to unicode" autosize autofocus raw-text test-id="text-to-unicode-input" />
    <c-input-text v-model:value="unicodeFromText" label="Unicode from your text" multiline raw-text readonly mt-2
      placeholder="The unicode representation of your text will be here" test-id="text-to-unicode-output" />
    <div mt-2 flex justify-center>
      <c-button :disabled="!unicodeFromText" @click="copyUnicode()">
        Copy unicode to clipboard
      </c-button>
    </div>
  </c-card>
  <c-card title="Unicode to Text">
    <c-input-text v-model:value="inputUnicode" multiline placeholder="Input Unicode"
      label="Enter unicode to convert to text" autosize raw-text test-id="unicode-to-text-input" />
    <c-input-text v-model:value="textFromUnicode" label="Text from your Unicode" multiline raw-text readonly mt-2
      placeholder="The text representation of your unicode will be here" test-id="unicode-to-text-output" />
    <div mt-2 flex justify-center>
      <c-button :disabled="!textFromUnicode" @click="copyText()">
        Copy text to clipboard
      </c-button>
    </div>
  </c-card>
  <c-card>
    <div v-html="markdownHtml" />
  </c-card>
</template>
