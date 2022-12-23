<template>
  <div class="container">
    <MenuDiv></MenuDiv>
    <MainDiv class="search"></MainDiv>
    <ActionDiv></ActionDiv>>
  </div>
</template>

<script>
import MainDiv from "@/components/MainDiv.vue";
import ActionDiv from "@/components/ActionDiv.vue";
import MenuDiv from "@/components/MenuDiv.vue";
export default {
  name: "SearchView",
  props: {},
  components: {
    MainDiv,
    ActionDiv,
    MenuDiv,
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-content: flex-start;
  align-items: flex-start;
  flex-wrap: nowrap;
  background-color: #f5f5ff;
}
</style>
