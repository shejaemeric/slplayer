<template>
  <div class="search">
    <SearchDiv></SearchDiv>
  </div>
</template>

<script>
import SearchDiv from "./SearchDiv.vue";
export default {
  name: "MainDiv",
  props: {
    data: String,
  },
  components: { SearchDiv },
};
</script>

<style scoped>
.search {
  width: 52%; /* previus 52% 899px*/
}
.search {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  padding-left: 3.5%;
  padding-right: 3.5%;
}
</style>
