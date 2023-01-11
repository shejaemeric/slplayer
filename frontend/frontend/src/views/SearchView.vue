<template>
  <div class="container">
    <MenuComponent @changeTab="this.change" :name="this.name"></MenuComponent>
    <HomeComponent :tab="this.tab"></HomeComponent>
  </div>
</template>

<script>
import HomeComponent from "@/components/HomeComponent.vue"
import MenuComponent from "@/components/menu/MenuComponent.vue";

export default {
  name: "SearchView",
  created(){
    var token = localStorage.getItem('jwt')
    if (!token){
        this.$router.push({name:"auth"})
    }
  },
  beforeunload(event) {
    event.preventDefault();
  },
  data (){
    return{
        name: this.$route.params.name,
        fav_artist: this.$route.params.fav_artist,
        tab:"main"
    }
  },
  components: {
    HomeComponent,
    MenuComponent
  },
  methods:{
    change(data){
        this.tab = data.tab;
    }
  }
};
</script>

<style scoped>


.container[data-v-0a4933a7] {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-content: flex-start;
	align-items: flex-start;
	flex-wrap: nowrap;
	background-color: #f5f5ff;
	/* margin: 0px 0px; */
	/* gap: 7%; */
	/* align-self: stretch; */
	width: fit-content;
}
.container[data-v-0a4933a7][data-v-0a4933a7] {

    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-content: flex-start;
    align-items: flex-start;
    flex-wrap: nowrap;
    background-color: #f5f5ff;
    margin: 0px 0px;
    gap: 7%;
    align-self: stretch;
    width: -moz-fit-content;
    width: fit-content;

}
.container {
    width: max-content !important;
    margin: 0px 0px !important;
}
</style>
