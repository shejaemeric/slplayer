<template>
  <div class="menu">
    <div class="menu-container">
      <div><img class="menu-logo" src="@/assets/others/logo.png" alt="" /></div>

      <div class="menu-list">
        <a class="menu-btn-selected" href=""
          ><img src="@/assets/others/home.png" alt="" />Home</a
        >
        <a class="menu-btn" href=""
          ><img src="@/assets/others/favorite.png" alt="" />Favorites</a
        >
        <a class="menu-btn" href=""
          ><img src="@/assets/others/account-icon.png" alt="" />Account</a
        >
      </div>

      <div class="menu-account clearfix">
        <div class="menu-account-img">
          <img src="@/assets/others/account.jpg" alt="" />
        </div>
        <p>Satoru Gojo</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MenuDiv",
  props: {
    data: String,
  },
};
</script>

<style scoped>
.menu {
  width: 25%; /*432px*/
  background-color: white;
  height: 100vh;
}

.menu-container {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  flex-wrap: nowrap;
  align-items: flex-start;
  align-content: flex-start;
}

.menu-list {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 76%;
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
  width: 73%;
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
</style>
