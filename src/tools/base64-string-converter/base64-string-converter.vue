<script setup lang="ts">
import showdown from 'showdown'; // 新增showdown引入
import { useCopy } from '@/composable/copy';
import { base64ToText, isValidBase64, textToBase64 } from '@/utils/base64';
import { withDefaultOnError } from '@/utils/defaults';
const { t, locale } = useI18n();

// 添加输入长度限制
const MAX_INPUT_LENGTH = 1024 * 1024 * 5; // 5MB字符长度限制

const encodeUrlSafe = useStorage('base64-string-converter--encode-url-safe', false);
const decodeUrlSafe = useStorage('base64-string-converter--decode-url-safe', false);

const textInput = ref('');
const base64Output = computed(() => {
  // 添加长度校验
  if (textInput.value.length > MAX_INPUT_LENGTH) {
    message.warning(`输入长度超过 ${MAX_INPUT_LENGTH / 1024}KB 限制`);
    return '';
  }
  return textToBase64(textInput.value, { makeUrlSafe: encodeUrlSafe.value });
});

// 如果存在文件上传功能，添加文件大小限制（示例）
function handleFileUpload(event: Event) {
  const input = event.target as HTMLInputElement;
  const file = input.files?.[0];
  
  if (file && file.size > 1024 * 1024 * 10) { // 10MB文件限制
    message.error('文件大小超过10MB限制');
    return;
  }
  
  // 文件处理逻辑...
}

const { copy: copyTextBase64 } = useCopy({ source: base64Output, text: 'Base64 string copied to the clipboard' });

const base64Input = ref('');
const textOutput = computed(() =>
  withDefaultOnError(() => base64ToText(base64Input.value.trim(), { makeUrlSafe: decodeUrlSafe.value }), ''),
);
const { copy: copyText } = useCopy({ source: textOutput, text: 'String copied to the clipboard' });
const b64ValidationRules = [
  {
    message: 'Invalid base64 string',
    validator: (value: string) => isValidBase64(value.trim(), { makeUrlSafe: decodeUrlSafe.value }),
  },
];
const b64ValidationWatch = [decodeUrlSafe];
const markdownHtml = ref('');

const loadMarkdown = async () => {
  const mdContent = await import(`./language/base64-string-converter.${locale.value}.md?raw`);
  const converter = new showdown.Converter();
  markdownHtml.value = converter.makeHtml(mdContent.default);
};
watchEffect(() => {
  loadMarkdown();
});
</script>

<template>
  <c-card title="String to base64">
    <!-- 添加文件上传输入 -->
    <input 
      type="file"
      @change="handleFileUpload"
      style="margin-bottom: 1rem"
      hidden
      ref="fileInput"
    >
    <c-button @click="fileInput?.click()">
      选择文件（最大10MB）
    </c-button>
    <n-form-item label="Encode URL safe" label-placement="left">
      <n-switch v-model:value="encodeUrlSafe" />
    </n-form-item>
    <c-input-text v-model:value="textInput" multiline placeholder="Put your string here..." rows="5"
      label="String to encode" raw-text mb-5 />

    <c-input-text label="Base64 of string" :value="base64Output" multiline readonly
      placeholder="The base64 encoding of your string will be here" rows="5" mb-5 />

    <div flex justify-center>
      <c-button @click="copyTextBase64()">
        Copy base64
      </c-button>
    </div>
  </c-card>

  <c-card title="Base64 to string">
    <n-form-item label="Decode URL safe" label-placement="left">
      <n-switch v-model:value="decodeUrlSafe" />
    </n-form-item>
    <c-input-text v-model:value="base64Input" multiline placeholder="Your base64 string..." rows="5"
      :validation-rules="b64ValidationRules" :validation-watch="b64ValidationWatch" label="Base64 string to decode"
      mb-5 />

    <c-input-text v-model:value="textOutput" label="Decoded string" placeholder="The decoded string will be here"
      multiline rows="5" readonly mb-5 />

    <div flex justify-center>
      <c-button @click="copyText()">
        Copy decoded string
      </c-button>
    </div>
  </c-card>
  <c-card>
    <div v-html="markdownHtml" />
  </c-card>
</template>
