<template>
  <div class="search">
    <CircleLoader
            :class="!initial_load ? 'hidden':''"
            v-if="initial_load">
    </CircleLoader>

    <SearchComponent
            :class="initial_load ? 'hidden':''"
            @searchTrack="search"
            :loading="this.tracks_loading"
            :tracks="this.tracks" >
    </SearchComponent>
    <SidebarComponent
            :class="initial_load ? 'hidden':''"
            @getRecognisedSong="search"
            :loading="this.album_loading"
            @selectAlbum="getAlbumTracks"
            :albums="albums">
    </SidebarComponent>

    <ErrorComponentVue v-if="this.error.occured" :alert="this.error.alert" :msg="this.error.msg"></ErrorComponentVue>

  </div>
</template>

<script>
import axios from 'axios';
import SearchComponent from "./SearchComponent.vue";
import SidebarComponent from "../sidebar/SidebarComponent.vue";
import ErrorComponentVue from "../errors/ErrorComponent.vue";
import CircleLoader from '../loaders/CircleLoader.vue';


export default {
  name: "MainComponent",
  props: {
  },
  components: { SearchComponent,SidebarComponent,ErrorComponentVue,CircleLoader },
  data (){
    return {
        tracks:null,
        albums:null,
        tracks_loading: true,
        album_loading: true,
        initial_load: true,
        error:{
            occured:false,
            alert:'danger',
            msg:"An uknown error occured"
        }
    }
  },
  methods:{
    async search(keyword) {
        this.tracks_loading = false

        var url = "http://localhost:5000/track/search/" + encodeURI(keyword);
        var jwt = localStorage.getItem('jwt')
        var headers = {headers:{Authorization:`Bearer ${jwt}`}}
        try {
            var response = await axios.get(url,headers)
            this.tracks = response.data.tracks
            this.tracks_loading = false
        } catch (error) {
            this.error.occured = true
            this.error.msg = "Server error-500"
        }
    },

    async getAlbumTracks(id){
        console.log("searching tracks....................")
        this.tracks_loading = false
        const jwt = localStorage.getItem('jwt')
        var headers = {headers:{Authorization: `Bearer ${jwt}`}}
        var url = "http://localhost:5000/albums/"+id+"/tracks"

        try {
            var response = await axios.get(url,headers)
            this.tracks = response.data.tracks
            this.tracks_loading = false
        } catch (error) {
            this.error.occured = true
            this.error.msg = "Server error-500"
        }

    }
  },
  async mounted() {

    const jwt = localStorage.getItem('jwt')
    const artist = localStorage.getItem('fav_artist')
    var headers = {headers:{Authorization: `Bearer ${jwt}`}}
    var tracks_url = "http://localhost:5000/track/search/" + encodeURI(artist);
    var albums_url = "http://localhost:5000/albums/top"


    try {
        // Get initial tracks
        var response = await axios.get(tracks_url,headers)
        this.tracks = response.data.tracks
        this.tracks_loading = true

        //Get top albums
        var response = await axios.get(albums_url,headers)
        this.albums = response.data.albums
        this.album_loading = false

        this.loading = false

    } catch (error) {
        this.error.occured = true
        this.error.msg = "Server error (mount)"
    }
    this.initial_load = false;
    // dummy albums
    // this.albums = [
    //     {"album_id":"3lS1y25WAhcqJDATJK70Mq",
    //     "artist":"Tylor Swift",
    //     "cover":"https://i.scdn.co/image/ab67616d00001e02e0b60c608586d88252b8fbc0",
    //     "name":"Midnights (3am Edition)"},
    //     {"album_id":"3nzuGtN3nXARvvecier4K0",
    //     "artist":"Alan Walker ",
    //     "cover":"https://i.scdn.co/image/ab67616d00001e02a108e07c661f9fc54de9c43a",
    //     "name":"Different World "},
    //     {"album_id":"46xdC4Qcvscfs3Ai2RIHcv","artist":"Nf","cover":"https://i.scdn.co/image/ab67616d00001e02942a0c9ac8f1def7c8805044","name":"The Search"},
    //     {"album_id":"5MS3MvWHJ3lOZPLiMxzOU6","artist":"Drake","cover":"https://i.scdn.co/image/ab67616d00001e0202854a7060fccc1a66a4b5ad","name":"Her Loss"}
    // ]
    // this.loading = false;

    // dummy tracks
    // var dummyData = {
    // "tracks": [
    //     {
    //         "album": "Bones",
    //         "artist": "Imagine Dragons",
    //         "cover": "https://i.scdn.co/image/ab67616d00001e02813713582dcc508e7d5073c4",
    //         "duration": "2:45",
    //         "id": "0HqZX76SFLDz2aW8aiqi7G",
    //         "name": "Bones"
    //     },
    //     {
    //         "album": "Mercury - Acts 1 & 2",
    //         "artist": "Imagine Dragons",
    //         "cover": "https://i.scdn.co/image/ab67616d00001e02fc915b69600dce2991a61f13",
    //         "duration": "2:45",
    //         "id": "54ipXppHLA8U4yqpOFTUhr",
    //         "name": "Bones"
    //     },
    //     {
    //         "album": "Night Visions",
    //         "artist": "Imagine Dragons",
    //         "cover": "https://i.scdn.co/image/ab67616d00001e02b2b2747c89d2157b0b29fb6a",
    //         "duration": "3:06",
    //         "id": "4G8gkOterJn0Ywt6uhqbhp",
    //         "name": "Radioactive"
    //     },
    //     {
    //         "album": "Evolve",
    //         "artist": "Imagine Dragons",
    //         "cover": "https://i.scdn.co/image/ab67616d00001e025675e83f707f1d7271e5cf8a",
    //         "duration": "3:24",
    //         "id": "0pqnGHJpmpxLKifKRmU6WP",
    //         "name": "Believer"
    //     },
    //     {
    //         "album": "Mercury - Acts 1 & 2",
    //         "artist": "Imagine Dragons",
    //         "cover": "https://i.scdn.co/image/ab67616d00001e02fc915b69600dce2991a61f13",
    //         "duration": "3:10",
    //         "id": "7sA2SKTo1QbTSSYn5YvJC4",
    //         "name": "Sharks"
    //     },
    // ]
    // }
    // this.tracks = dummyData.tracks

},
};
</script>

<style scoped>
.hidden{
    display: none;
}
.search-load{
    display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: 10%;
  width: 67%;
}

.search {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: 10%;
  width: auto;
}

.search-load{
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    gap: 28%;
}

.load{
    display: block;
    position: absolute;
    top:50%;
    right: 50%;
}
</style>
