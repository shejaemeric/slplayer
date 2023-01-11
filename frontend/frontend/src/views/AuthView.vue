<template>
  <div class="container">
    <AuthComponent></AuthComponent>
  </div>
</template>

<script>
import AuthComponent from "@/components/auth/AuthComponent.vue";

export default {
  name: "AuthView",
  components: {
    AuthComponent,
  },
  created (){
    var token = localStorage.getItem('jwt')
    var name = localStorage.getItem('name')
    var fav_artist = localStorage.getItem('fav_artist')
    if (token){
        this.$router.push({name:"home",params:{
            name,
            fav_artist,
        }})
    }
  }
};
</script>

<style scoped>
body {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: nowrap;
  background-color: #f5f5ff;
  margin-top: 100px;
}
.container {
  margin: 100px 320px;
}
</style>
