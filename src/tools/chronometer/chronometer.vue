<script setup lang="ts">
import { useRafFn } from '@vueuse/core';
import showdown from 'showdown'; // 新增showdown引入

import { formatMs } from './chronometer.service';

const isRunning = ref(false);
const counter = ref(0);

let previousRafDate = Date.now();
const { pause: pauseRaf, resume: resumeRaf } = useRafFn(
  () => {
    const deltaMs = Date.now() - previousRafDate;
    previousRafDate = Date.now();
    counter.value += deltaMs;
  },
  { immediate: false },
);

function resume() {
  previousRafDate = Date.now();
  resumeRaf();
  isRunning.value = true;
}

function pause() {
  pauseRaf();
  isRunning.value = false;
}
const { t, locale } = useI18n();
const markdownHtml = ref('');
const loadMarkdown = async () => {
  const mdContent = await import(`./language/chronometer.${locale.value}.md?raw`);
  const converter = new showdown.Converter();
  markdownHtml.value = converter.makeHtml(mdContent.default);
};
watchEffect(() => {
  loadMarkdown();
});
</script>

<template>
  <div>
    <c-card>
      <div class="duration">
        {{ formatMs(counter) }}
      </div>
    </c-card>
    <div mt-5 flex justify-center gap-3>
      <c-button v-if="!isRunning" type="primary" @click="resume">
        Start
      </c-button>
      <c-button v-else type="warning" @click="pause">
        Stop
      </c-button>

      <c-button @click="counter = 0">
        Reset
      </c-button>
    </div>
    <c-card class="mt-5">
      <div v-html="markdownHtml"></div>
    </c-card>
  </div>

</template>

<style lang="less" scoped>
.duration {
  text-align: center;
  font-size: 40px;
  font-family: monospace;
  margin: 20px 0;
}
</style>
