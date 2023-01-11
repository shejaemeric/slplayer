<template>
  <div class="play-info">
    <!-- <div class="clearfix">

            <a>Download any Music</a>
            <img src="/src/others/music-icon.png" alt="">

        </div> -->
    <ErrorComponent v-if="this.error.occured" :alert="this.error.alert" :msg="this.error.msg"></ErrorComponent>
    <h1>Playing</h1>
    <div class="play-img">
      <div>
        <img :src="data.cover" height="100%" width="100%" />
      </div>
      <div class="overlay">

        <CustomAudioPlayer
          :loading = "this.currentLoading"
          :file=this.playUrl
          :data="data"
          @download="downloadTrack"
        ></CustomAudioPlayer>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CustomAudioPlayer from "./CustomAudioPlayer.vue";
import ErrorComponent from "../errors/ErrorComponent.vue";

export default {
  name: "CustomPlayer",
  props: {
    data: Object,
  },
  data(){
    return {
        playUrl:"",
        currentLoading:"",
        error:{
            occured:false,
            alert:'danger',
            msg:"An uknown error occured"
        }
    }
  },
  components: {
    CustomAudioPlayer,
    ErrorComponent
  },
  watch:{
    data(){
        console.log("select change")
        this.currentLoading = true;
        if (this.data.id != null){
            this.getPlayUrl(this.data.id);
        }
    },
  },
  async mounted() {
    console.log("created")
    this.currentLoading = true;
    if (this.data.id != null){
        this.getPlayUrl(this.data.id);
    }
  },
  methods: {
    async getPlayUrl(id){
        try {
            var url = "http://localhost:5000/track/play/" + id;
            var response = await axios.get(url)
            this.playUrl = response.data.url;
            this.currentLoading  = false

        } catch (error) {
            this.error.occured = true;
            this.error.msg = "Could not play the song"
        }
    },
    async downloadTrack() {
      var downloadUrl = "";
      try{
        var url = "http://localhost:5000/track/download/" + this.selId;
        var response =  await axios.get(url)
        url = response.data.url
        window.location.href = url;
      }catch{
        this.error.occured = true;
        this.error.msg = "Could not retrieve download link"
      }
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
/* .play-info img {
  width: 100%;
  height: 197px;
  object-fit: cover;
  object-position: center;
} */

.play-info img{
    width: 100%;
    height: 183px;
    -o-object-fit: cover;
    object-fit: cover;
    -o-object-position: center;
    object-position: center;
    margin-right: 13rem;
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
