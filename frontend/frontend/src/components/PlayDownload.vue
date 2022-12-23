<template>
  <div class="play-info">
    <!-- <div class="clearfix">

            <a>Download any Music</a>
            <img src="/src/others/music-icon.png" alt="">

        </div> -->

    <h1>Playing</h1>
    <div class="play-img">
      <div>
        <img :src="cover" height="100%" width="100%" />
      </div>
      <div class="overlay">
        <AudioPlayer
          :file=this.playUrl
          :selId="this.selId"
          @download="downloadTrack"
        ></AudioPlayer>
      </div>
    </div>
  </div>
</template>

<script>
import AudioPlayer from "./AudioPlayer.vue";
import axios from "axios";
export default {
  name: "PlayDownload",
  props: {
    cover: String,
    selId: String,
    playUrl:String
  },
  components: {
    AudioPlayer,
  },
  methods: {
    async downloadTrack() {
      var downloadUrl = "";
      var url = "http://localhost:5000/track/download/" + this.selId;
      var response =  await axios.get(url)
      url = response.data.url
      window.location.href = url;
    },

  },
};
</script>

<style scoped>
.play-img {
  display: flex;
  flex-direction: row;
}

.play-info .clearfix {
  margin-top: 16px;
}
.play-info img {
  width: 100%;
  height: 218px;
  object-fit: cover;
  object-position: center;
}

.play-img {
  background-size: cover;
  width: 100%;
  background-position: center;
  border-radius: 25px;
}

.play-img h1 {
  line-height: 2;
}

.play-download-btn {
  background-color: #15111f;
  color: white;
  padding: 8px 23px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  text-decoration: none;
  gap: 9px;
  align-items: center;
  font-size: 19px;
  width: max-content;
  border-radius: 25px;
  height: 42px;
}
.play-btn {
  display: flex;
  flex-direction: row;
  gap: 16px;
  margin-top: -24px;
}
.play-favorite-btn {
  background-color: #eaeaea;
  color: #15111fb3;
  padding: 8px 24px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  text-decoration: none;
  gap: 9px;
  align-items: center;
  font-size: 19px;
  width: max-content;
  border-radius: 25px;
  height: 42px;
}

.play-info h1 {
  margin-bottom: 16px;
  margin-left: 10px;
}
</style>
