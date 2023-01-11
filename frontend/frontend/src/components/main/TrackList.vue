<template>
  <div>
    <div class="search-results">
      <div class="titles">
        <div>
          <p>#</p>
          <p>Title</p>
        </div>
        <div class="artist">Artists</div>
        <div><p class="other-details">Other details</p></div>
      </div>
      <div class="all-result">
        <slot />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TrackList",
  props: {
    datas: Object,
  },
  components: {},
};
</script>

<style scoped>
.titles {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: 48px;
  margin-top: 20px;
  color: #cbccd1;
}
.search-results {
  height: 30px;
}
.titles p {
  display: inline;
  margin-right: 64px;
  color: #cbccd1;
  margin-left: 16px;
}

.all-result {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  overflow-y: scroll;
  margin-top: 24px;
  height: 37vh;
  gap:3%;
  width: 100%;
}
.other-details {
  margin-left: 40px;
  color: #cbccd1;
}
.artist {
  color: #cbccd1;
}
</style>
