<template>
    <footer>
        <p>VirtualisLab &copy; {{ year  }}</p>
    </footer>
</template>
<script>
import { computed } from 'vue'

export default {
  setup () {
    const year = computed(() => new Date().getFullYear())
    return { year }
  }
}
</script>

