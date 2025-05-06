<script setup lang="ts">
import {
  camelCase,
  capitalCase,
  constantCase,
  dotCase,
  headerCase,
  noCase,
  paramCase,
  pascalCase,
  pathCase,
  sentenceCase,
  snakeCase,
} from 'change-case';
import InputCopyable from '../../components/InputCopyable.vue';
import showdown from 'showdown'; // 新增showdown引入

const baseConfig = {
  stripRegexp: /[^A-Za-zÀ-ÖØ-öø-ÿ]+/gi,
};

const input = ref('lorem ipsum dolor sit amet');

const formats = computed(() => [
  {
    label: 'Lowercase:',
    value: input.value.toLocaleLowerCase(),
  },
  {
    label: 'Uppercase:',
    value: input.value.toLocaleUpperCase(),
  },
  {
    label: 'Camelcase:',
    value: camelCase(input.value, baseConfig),
  },
  {
    label: 'Capitalcase:',
    value: capitalCase(input.value, baseConfig),
  },
  {
    label: 'Constantcase:',
    value: constantCase(input.value, baseConfig),
  },
  {
    label: 'Dotcase:',
    value: dotCase(input.value, baseConfig),
  },
  {
    label: 'Headercase:',
    value: headerCase(input.value, baseConfig),
  },
  {
    label: 'Nocase:',
    value: noCase(input.value, baseConfig),
  },
  {
    label: 'Paramcase:',
    value: paramCase(input.value, baseConfig),
  },
  {
    label: 'Pascalcase:',
    value: pascalCase(input.value, baseConfig),
  },
  {
    label: 'Pathcase:',
    value: pathCase(input.value, baseConfig),
  },
  {
    label: 'Sentencecase:',
    value: sentenceCase(input.value, baseConfig),
  },
  {
    label: 'Snakecase:',
    value: snakeCase(input.value, baseConfig),
  },
  {
    label: 'Mockingcase:',
    value: input.value
      .split('')
      .map((char, index) => (index % 2 === 0 ? char.toUpperCase() : char.toLowerCase()))
      .join(''),
  },
]);

const inputLabelAlignmentConfig = {
  labelPosition: 'left',
  labelWidth: '120px',
  labelAlign: 'right',
};
const { t, locale } = useI18n();
const markdownHtml = ref('');
const loadMarkdown = async () => {
  const mdContent = await import(`./language/case-converter.${locale.value}.md?raw`);
  const converter = new showdown.Converter();
  markdownHtml.value = converter.makeHtml(mdContent.default);
};
watchEffect(() => {
  loadMarkdown();
});
</script>

<template>
  <div class="container"> <!-- 新增容器 div -->
    <div class="card-wrapper">
      <c-card>
        <c-input-text v-model:value="input" label="Your string:" placeholder="Your string..." raw-text
          v-bind="inputLabelAlignmentConfig" />
        <div my-16px divider />
        <InputCopyable v-for="format in formats" :key="format.label" :value="format.value" :label="format.label"
          v-bind="inputLabelAlignmentConfig" mb-1 />
      </c-card>
    </div>

    <div class="card-wrapper"> <!-- 新增卡片包裹层 -->
      <c-card>
        <div v-html="markdownHtml"></div>
      </c-card>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 20px 0;
}

.card-wrapper {
  width: 100%;
  max-width: 600px;
}
</style>