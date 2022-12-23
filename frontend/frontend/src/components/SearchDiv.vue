<template>
  <div class="search-form">
    <form @submit="search">
      <div class="srch">
        <img src="@/assets/others/search.png" alt="" /><input
          type="text"
          class="search-input"
          placeholder="Search Artist, Songs, Tracks"
          ref="keyword"
        />
      </div>
    </form>
    <PlayDownload :playUrl="playUrl" :selId="selId" :cover="cover"></PlayDownload>
    <TracksDiv>
      <TrackDiv
        v-for="data in results"
        :key="data.id"
        :data="data"
        :class="data.id == selId ? 'selected-item' : ''"
        @selectTrack = "select(data.cover,data.id)"
      >
      </TrackDiv>
    </TracksDiv>
  </div>
</template>

<script>
/* eslint-disable */
import PlayDownload from "./PlayDownload.vue";
import TracksDiv from "./TracksDiv.vue";
import TrackDiv from "./TrackDiv.vue";
import axios from "axios";

export default {
  name: "SearchDiv",
  components: {
    PlayDownload,
    TracksDiv,
    TrackDiv
  },
  data() {
    return {
      keyword: "",
      results: null,
      cover: null,
      selId: null,
      playUrl: "https://p.scdn.co/mp3-preview/43288a26d88c84b0ac5938c6e547b0ad99c49f78?cid=d8a5ed958d274c2e8ee717e6a4b0971d",
    };
  },

  async mounted() {
    //var url = "http://localhost:5000/track/search/" + encodeURI("alan walker");
    //await axios.get(url).then((response) => {this.results = response.data.tracks}).catch(err => console.error(err));;
    var dummyData = {
    "tracks": [
        {
            "album": "Bones",
            "artist": "Imagine Dragons",
            "cover": "https://i.scdn.co/image/ab67616d00001e02813713582dcc508e7d5073c4",
            "duration": "2:45",
            "id": "0HqZX76SFLDz2aW8aiqi7G",
            "name": "Bones"
        },
        {
            "album": "Mercury - Acts 1 & 2",
            "artist": "Imagine Dragons",
            "cover": "https://i.scdn.co/image/ab67616d00001e02fc915b69600dce2991a61f13",
            "duration": "2:45",
            "id": "54ipXppHLA8U4yqpOFTUhr",
            "name": "Bones"
        },
        {
            "album": "Night Visions",
            "artist": "Imagine Dragons",
            "cover": "https://i.scdn.co/image/ab67616d00001e02b2b2747c89d2157b0b29fb6a",
            "duration": "3:06",
            "id": "4G8gkOterJn0Ywt6uhqbhp",
            "name": "Radioactive"
        },
        {
            "album": "Evolve",
            "artist": "Imagine Dragons",
            "cover": "https://i.scdn.co/image/ab67616d00001e025675e83f707f1d7271e5cf8a",
            "duration": "3:24",
            "id": "0pqnGHJpmpxLKifKRmU6WP",
            "name": "Believer"
        },
        {
            "album": "Mercury - Acts 1 & 2",
            "artist": "Imagine Dragons",
            "cover": "https://i.scdn.co/image/ab67616d00001e02fc915b69600dce2991a61f13",
            "duration": "3:10",
            "id": "7sA2SKTo1QbTSSYn5YvJC4",
            "name": "Sharks"
        },
    ]
    }
    this.results = dummyData.tracks
},
  watch:{
    results(){
        this.cover = (this.results)[1].cover;
        this.selId = (this.results)[1].id;
    },
  },

  methods: {
    async getPlayUrl(id){
        if (this.selId != null){
        var url = "http://localhost:5000/track/play/" + id;;
        return await (axios.get(url));
    }
    },
    search(event) {
        event.preventDefault();
        this.keyword = this.$refs.keyword.value
        var url = "http://localhost:5000/track/search/" + encodeURI(this.keyword);
        axios.get(url).then((response) => (this.results = response.data.tracks)).catch((exception)=>{
            console.log(exception);
        });
    },
    async select(cover,selId) {
        console.log("clicked"+this.selId);
        this.cover = cover;
        this.selId = selId;
        var response = await this.getPlayUrl(this.selId);
        this.playUrl = response.data.url;
    },
  },
};
</script>

<style scoped>
.selected-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 16px;
  padding: 22px 0px;
  background-color: #fff;
  box-shadow: 0 3px 1px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19) !important;
}

.selected-item p {
  color: #15111df6;
  font-weight: 500;
}

.search-input {
  background-color: #fff;
  font-size: 19px;
  border-radius: 0px 25px 25px 0px;
  height: 48px;
  outline: none;
  width: 100%;
  border: none;
  padding-left: 10px;
  color: #15111da9;
}

.search-form {
  width: 100%;
  margin-top: 15px;
}
.search-form img {
  float: left;
  height: 30px;
  padding-left: 16px;
  background-color: #fff;
  border-radius: 25px 0px 0px 25px;
}
.srch {
  height: 48px;
  background-color: #fff;
  border-radius: 25px;
  width: 100%;
  display: flex;
  flex-direction: row;
  gap: 10px;
  align-items: center;
}
form {
  display: flex;
  flex-direction: row;
}
</style>
