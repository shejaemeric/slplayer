<template :class="mountLoad ? 'ls' : ''">
<div>
  <div class="search-form">
    <form @submit.prevent="search">
      <div class="srch">
        <img src="@/assets/others/search.png" alt="" />
        <input
          type="text"
          class="search-input"
          placeholder="Search Artist, Songs, Tracks"
          v-model="keyword"
        />
      </div>
    </form>
    <div v-if="mountLoad" >
        <h1>Playing</h1>
        <div class="player-container">

                    <v-skeleton-loader type="card" width="40%" height="182px"></v-skeleton-loader>

                    <div class="player-text">
                        <v-skeleton-loader type="card" width="70%" height="20px"></v-skeleton-loader>
                        <v-skeleton-loader type="card" width="100%" height="20px"></v-skeleton-loader>
                        <v-skeleton-loader type="card" width="80%"  height="20px"></v-skeleton-loader>
                    </div>
        </div>
    </div>

    </div>
    <CustomPlayer v-if="selected != null" :data="selected"></CustomPlayer>
    <div class="loader-container" v-if="loading">
            <div v-for="i in 6" :key="i" class="loader">
                <v-skeleton-loader class="loader-avatar" type="avatar" :loading="true"/>
                <v-skeleton-loader class="loader-list" type="card" height="30px" width="90%" :loading="true"/>
            </div>
    </div>
    <TrackList>
            <TrackComponent
                v-if="!loading"
                v-for="data in (items ? items:tracks)"
                :key="data.id"
                :data="data"
                :class="data.id == selected.id ? 'selected-item' : ''"
                @selectTrack = "select(data)"
            >
            </TrackComponent>
    </TrackList>
</div>
</template>

<script>
import CustomPlayer from "./CustomPlayer.vue";
import TrackList from "./TrackList.vue";
import TrackComponent from "./TrackComponent.vue";
import { VSkeletonLoader } from "vuetify/lib";

export default {
  name: "SearchComponent",
  components: {
    CustomPlayer,
    TrackList,
    TrackComponent,
    VSkeletonLoader
  },
  props:{
    tracks:Array,
    tracks_loading:Boolean
  },

  data() {
    return {
      keyword: "",
      selected:null,
      items:this.tracks,
      loading:true,
      mountLoad:true
    };
  },

  watch:{
    tracks(){
        this.loading = false;
        this.mountLoad = false;
        this.selected = (this.tracks)[0];
    },
  },
  created(){
    this.loading = true;
    this.mountLoad = true
  },
  methods: {
    search(event) {
        this.loading = true
        this.$emit('searchTrack',this.keyword)
    },
    async select(data) {
        this.selected = data;
    },
  },
};
</script>


<style scoped>
.loader-container {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  overflow-y: scroll;
  margin-top: 24px;
  height: 37vh;
  gap:3%;
  width: 100%;
}

.player-text{
    width: 60%;
    padding: 28px 22px 11px 21px;
    display: flex;
    flex-direction: column;
    gap: 20%;
    background-color: rgba(255, 255, 255, 0.151);
}
.player-container{
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-content: center;
    margin-top:30px;
    width: 110%;
    border: 1px solid #e0e0e0;
    border-radius: 0px 6px 6px 0px;
    box-shadow: 0 5px 8px rgba(0, 0, 0, 0.15);
    color: #404040;
    line-height: 1.5625;
    box-sizing: content-box;

}
.loader{
    width: 100%;
    display: flex;
    justify-content: start;
    flex-direction: row;
    align-items: center;
    gap: 3%;
}
.track-loader{
    height: 25px;
    padding-bottom: 10px;
    background-color:#F5F5FF
}
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
  margin-top: 15px;
  width: 100%;
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
