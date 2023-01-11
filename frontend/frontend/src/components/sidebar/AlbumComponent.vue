<template>
    <div class="album" @click="handleAlbumClick">
        <div class="album-img">
          <img :src="album.cover" alt="" />
        </div>
        <div class="album-info">
          <p>{{ album.artist }}</p>
          <p class="album-name">{{album.name}}</p>
        </div>
    </div>
</template>

<script>
    export default{
        name:"AlbumComponent",
        props:{
            album:Object,
        },
        emits:['selectAlbum'],
        methods:{
            handleAlbumClick(){
                var id = this.album.album_id
                console.log(id)
                this.$emit('selectAlbum',id)
            }
        }
    }
</script>

<style scoped>
.action {
  width: 23%; /*397px*/
}

.action-artist {
  display: flex;
  flex-direction: row;
}

.top-artist {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  gap: 3px;
}
.action-artist-img img {
  height: 30px;
  width: 30px;
  border-radius: 25px;
  float: left;
  margin-right: 10px;
  object-fit: cover;
}

.action-artist {
  background-color: #fefefe;
  padding: 7px 15px;
  border-radius: 25px;
  margin: 5px 3px;
  overflow: scroll;
  display: flex;
  align-items: center;
}

.action h1 {
  font-size: 24px;
  margin: 20px 0px;
}
.top-album {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  justify-content: start;
  gap: 5px;
}
.album {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: flex-start;
    margin: 16px 0px;
    align-content: unset;
    align-items: center;
}
.album-info {
  display: flex;
  flex-direction: column;
gap: 16px;
}

.album-img img {
  height: 38px;
  width: 38px;
  object-fit: cover;
  border-radius: 25px;
  float: left;
  margin-right: 12px;
  margin-top: -24px;
}

.album-name {
  font-size: 14px;
  color: #15111d73;
  font-weight: 400;
}

.album-info p {
    margin: -17px 30px 2px 2px;
    font-weight: 700;
    width: 180%;
}

form {
  display: flex;
  flex-direction: row;
}
</style>
