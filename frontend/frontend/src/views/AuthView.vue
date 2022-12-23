<template>
  <div class="container">
    <AuthDivVue></AuthDivVue>
  </div>
</template>

<script>
import AuthDivVue from "@/components/AuthDiv.vue";

export default {
  name: "AuthView",
  components: {
    AuthDivVue,
  },
};
</script>

<style scoped>
body {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: nowrap;
  background-color: #f5f5ff;
  margin-top: 100px;
}
.container {
  margin: 100px 320px;
}
</style>
