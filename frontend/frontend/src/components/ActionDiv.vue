<template>
  <div class="action">
    <h1>Top Artist</h1>

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
    </div>

    <div class="top-album">
      <h1>Top albums</h1>

      <div class="album">
        <div class="album-img">
          <img src="@/assets/albums/album.jpg" alt="" />
        </div>
        <div class="album-info">
          <p>Taylor Swift</p>
          <p class="album-name">After Hours</p>
        </div>
      </div>

      <div class="album">
        <div class="album-img">
          <img src="@/assets/albums/album.jpg" alt="" />
        </div>
        <div class="album-info">
          <p>Alan Walker</p>
          <p class="album-name">Different Worlds</p>
        </div>
      </div>

      <div class="album">
        <div class="album-img">
          <img src="@/assets/albums/album.jpg" alt="" />
        </div>
        <div class="album-info">
          <p>Drake</p>
          <p class="album-name">Certified(Special Edition)</p>
        </div>
      </div>

      <div class="album">
        <div class="album-img">
          <img src="@/assets/albums/album.jpg" alt="" />
        </div>
        <div class="album-info">
          <p>One Republic</p>
          <p class="album-name">Human</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ActionDiv",
  props: {
    data: String,
  },
};
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
  justify-content: start;
  margin: 8px 0px;
}
.album-info {
  display: flex;
  flex-direction: column;
}

.album-img img {
  height: 38px;
  width: 38px;
  object-fit: cover;
  border-radius: 25px;
  float: left;
  margin-right: 10px;
}

.album-name {
  font-size: 14px;
  color: #15111d73;
  font-weight: 400;
}

.album-info p {
  margin: 2px;
  font-weight: 700;
}

form {
  display: flex;
  flex-direction: row;
}
</style>
