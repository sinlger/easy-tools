<script setup lang="ts">
import showdown from 'showdown'; // 新增showdown引入

import { normalizeEmail } from 'email-normalizer';
import { withDefaultOnError } from '@/utils/defaults';
import { useCopy } from '@/composable/copy';

const emails = ref('');
const normalizedEmails = computed(() => {
  if (!emails.value) {
    return '';
  }

  return emails.value
    .split('\n')
    .map((email) => {
      return withDefaultOnError(() => normalizeEmail({ email }), `Unable to parse email: ${email}`);
    })
    .join('\n');
});
const { t, locale } = useI18n();
const markdownHtml = ref('');
const loadMarkdown = async () => {
  const mdContent = await import(`./language/email-normalizer.${locale.value}.md?raw`);
  const converter = new showdown.Converter();
  markdownHtml.value = converter.makeHtml(mdContent.default);
};
watchEffect(() => {
  loadMarkdown();
});
const { copy } = useCopy({
  source: normalizedEmails,
  text: 'Normalized emails copied to the clipboard',
  createToast: true,
});
</script>

<template>
  <div>
    <div class="mb-2">
      Raw emails to normalize:
    </div>
    <c-input-text v-model:value="emails" placeholder="Put your emails here (one per line)..." rows="3" multiline
      autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" autofocus monospace />

    <div class="mb-2 mt-4">
      Normalized emails:
    </div>
    <c-input-text :value="normalizedEmails" placeholder="Normalized emails will appear here..." rows="3"
      autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" multiline readonly monospace />
    <div class="mt-4 flex justify-center gap-2">
      <c-button @click="emails = ''">
        Clear emails
      </c-button>
      <c-button :disabled="!normalizedEmails" @click="copy()">
        Copy normalized emails
      </c-button>
    </div>
  </div>
  <c-card>
    <div v-html="markdownHtml"></div>
  </c-card>
</template>
