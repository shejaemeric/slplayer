<template>
  <div class="action">
    <!-- <h1>Top Artist</h1>

    <div class="top-artist">
      <div class="action-artist">
        <div class="action-artist-img">
          <img src="@/assets/artists/artist.jpg" alt="" />
        </div>
        Alan Walker
      </div>

      <div class="action-artist">
        <div class="action-artist-img">
          <img src="@/assets/artists/artist.jpg" alt="" />
        </div>
        Jay z
      </div>

      <div class="action-artist">
        <div class="action-artist-img">
          <img src="@/assets/artists/artist.jpg" alt="" />
        </div>
        Taylor Swift
      </div>

      <div class="action-artist">
        <div class="action-artist-img">
          <img src="@/assets/artists/artist.jpg" alt="" />
        </div>
        WizKid
      </div>

      <div class="action-artist">
        <div class="action-artist-img">
          <img src="@/assets/artists/artist.jpg" alt="" />
        </div>
        Chris Brown
      </div>
    </div> -->

    <div class="top-album">
      <h1>Top Albums</h1>
        <AlbumComponent
        v-for="album in albums"
        :album="album"
        :key="album.album_id"
        @selectAlbum="handleAlbumClick"
        >
    </AlbumComponent>
    <RecognizeSong @getRecognisedSong="getRecognisedSong"></RecognizeSong>
    </div>
  </div>
</template>

<script>
import AlbumComponent from './AlbumComponent.vue';
import RecognizeSong from '@/components/sidebar/RecognizeSong.vue';

export default {
  name: "SidebarComponent",
  components:{
    AlbumComponent,
    RecognizeSong
  },
  props:{
    albums:Array,
  },
  emits:['selectAlbum'],
  data(){
    return {
        results:null
    }
  },
  methods:{
        handleAlbumClick(id){
            console.log(id)
            this.$emit('selectAlbum',id)
        },
        getRecognisedSong(keyword){
            this.$emit('getRecognisedSong',keyword)
        }
    },
};
</script>

<style scoped>
.action {
    margin-top: 10%;
}

.action h1 {
    font-size: 25px;
    margin: 20px 0px;
    width: max-content;
}
.top-album {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  justify-content: start;
  gap: 5px;
}
</style>
