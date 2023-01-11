<template>
  <div class="menu">
    <div class="menu-container">
      <div><img class="menu-logo" src="@/assets/others/logo.png" alt="" /></div>

      <div class="menu-list">
        <a class="menu-btn-selected" @click="goToMain" href=""
          ><img src="@/assets/others/home.png" alt="" />Search</a
        >
        <a class="menu-btn" @click="goToUpdateUser" href=""
          ><img src="@/assets/others/account-icon.png" alt="" />Update Account</a
        >
        <a class="menu-btn" @click="logOut" href=""
          ><img src="@/assets/icons8-open-pane-24.png" alt="" />Log Out</a
        >
      </div>

      <div class="menu-account clearfix">
        <div class="menu-account-img">
          <img src="@/assets/others/account.jpg" alt="" />
        </div>
        <p class="userName">{{this.name}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MenuComponent",
  props: {
  },
  data (){
    return{
        name:localStorage.getItem('name'),
    }
  },
  emits:["changeTab"],
  methods:{
    logOut(){
        localStorage.removeItem('jwt');
        localStorage.removeItem('name')
        localStorage.removeItem('fav_artist')
    },
    goToUpdateUser(event){
        event.preventDefault();
        this.$emit("changeTab",{tab:"update"});
    },
    goToMain(event){
        event.preventDefault()
        this.$emit("changeTab",{tab:"main"});
    }
  },
};
</script>

<style scoped>

.menu {
  background-color: white;
  height: 100vh;
}

.menu-container {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  flex-wrap: nowrap;
  align-items: center;
  align-content: flex-start;
}

.menu-list {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 88%;
}

.menu-btn-selected {
  background-color: #15111f;
  color: white;
  height: 70px;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-items: center;
  text-decoration: none;
  padding-left: 10px;
  gap: 12px;
  border-radius: 14px;
}

.menu-btn {
  height: 70px;
  color: #15111db3;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-items: center;
  text-decoration: none;
  padding-left: 10px;
  gap: 12px;
  border-radius: 14px;
}
.menu-container {
  width: 100%;
  height: 100%;
}
.menu-list img {
  float: left;
  width: 38px;
  height: 38px;
}

.menu-logo {
  width: 73%;
}
.menu-account {
  width: 94%;
  border-top: 2px solid #00000026;
  padding-top: 15px;
}
.menu-account img {
  float: left;
  border-radius: 51%;
  width: 53px;
  height: 53px;
  object-fit: cover;
  margin-right: 10px;
}
.userName{
    margin-top: 16px
}
</style>
