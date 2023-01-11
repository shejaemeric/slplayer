<template>
  <div @click="$emit('selectTrack')" class="one-result">
    <div class="results">
      <div class="result-item">
        <div class="res-img">
          <img :src="this.data.cover" alt="" />
        </div>

        <div class="res-name">
          <p>{{ this.data.name }}</p>
        </div>
        <div class="res-artist">
          <p>{{ this.data.artist }}</p>
        </div>
        <div class="res-duration">
          <p>{{ this.data.duration }}</p>
        </div>
        <div class="res-album">
          <p>{{ this.data.album }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "TrackComponent",
  props: {
    data: Object,
  },
  emits:['selectTrack'],
};
</script>

<style scoped>
.one-result {
  height: 56px;
}

.res-name p {
  width: 136px;
}

.res-artist p {
  width: 136px;
}

.res-duration {
  width: 44px;
}

.result-item p {
  color: #15111da2;
  font-weight: 500;
}

.result-item-selected p {
  color: #15111df6;
  font-weight: 500;
}
.results {
  margin-top: 0px;
}
.res-img {
  width: 32px;
}

.res-img img {
  width: 38px;
  height: 38px;
  border-radius: 25px;
  background-size: cover;
}
.result-item p {
  padding: 2px 5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 12ch;
}

.result-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0px 7px;
  gap: 32px;
  justify-content: flex-start;
}
</style>
