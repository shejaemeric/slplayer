<template>
    <div class="container">
      <MainComponent  :fav_artist="this.fav_artist" :class="this.tab == 'main' ? 'search':'hidden' "></MainComponent>
      <UpdateComponent :class="this.tab == 'update' ? 'search':'hidden'"> </UpdateComponent>
    </div>
  </template>

  <script>
  import MainComponent from "@/components/main/MainComponent.vue";
  import SidebarComponent from "@/components/sidebar/SidebarComponent.vue";
  import MenuComponent from "@/components/menu/MenuComponent.vue";
  import UpdateComponent from "@/components/update/UpdateComponent.vue"

  export default {
    name: "HomeComponent",
    data (){
      return{
          name: this.$route.params.name,
          fav_artist: this.$route.params.fav_artist,
      }
    },
    props:{
        tab:String,
    },
    components: {
      MainComponent,
      SidebarComponent,
      MenuComponent,
      UpdateComponent
    },
    methods:{
    }
  };
  </script>

  <style scoped>
  .hidden{
    display: none !important;
  }
  .container {
      display: flex;
      flex-direction: row;
      justify-content: flex-start;
      align-content: flex-start;
      align-items: flex-start;
      flex-wrap: nowrap;
      background-color: #f5f5ff;
      margin: 0px 0px;
      gap: 7%;
  }
  </style>
