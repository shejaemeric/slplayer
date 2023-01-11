<template>
  <div>
    <ErrorComponent v-if="this.error.occured" :alert="this.error.alert" :msg="this.error.msg" :closeOption="this.error.close"></ErrorComponent>
    <div class="container">
        <div class="title">Update account info</div>
        <form action="#">
            <div class="user__details">
            <div class="input__box">
                <span class="details">Name</span>
                <input type="text" v-model="name" required>
            </div>
            <div class="input__box">
                <span class="details">Username</span>
                <input type="text" v-model="username" required>
            </div>
            <div class="input__box">
                <span class="details">Email</span>
                <input type="email" v-model="email" required>

            </div>
                    <div class="input__box">
                <span class="details">Favorite Artist</span>
                <input type="email" v-model="fav_artist" required>

            </div>

            </div>
            <div class="button">
            <input type="submit" value="Update Info" @click="update">
            </div>
        </form>
        </div>
  </div>
</template>

<script>
import axios from 'axios';
import ErrorComponent from '../errors/ErrorComponent.vue';

export default {
    name:"UpdateComponent",
    props:{},
    components:{
        ErrorComponent
    },
    data(){
        return {
            email:'',
            name:'',
            username:'',
            fav_artist:'',
            error:{
                occured: false,
                msg:'An unkown error occured',
                alert:'danger',
                close:true
            }
        }
    },
    async mounted(){
        var username = localStorage.getItem("username");
        var url = "http://127.0.0.1:5000/user/"+username;

        var response = await axios.get(url);
        var user = response.data.user;
        this.username = user.username;
        this.email = user.email;
        this.name = user.name;
        this.fav_artist = user.fav_artist;
    },
    methods:{
        async update(event){
        event.preventDefault();
        var username = localStorage.getItem("username");
        var url = "http://127.0.0.1:5000/user/"+username
        console.log(this.fav_artist)
        var formData = new FormData()
        formData.append("username",this.username);
        formData.append("name",this.name);
        formData.append("email",this.email);
        formData.append("fav_artist",this.fav_artist);

        var response = await axios.put(url,formData)
        if(response.status === 200){
            this.error.occured = true,
            this.error.alert = 'success',
            this.error.msg = 'Account info Updated'
        }else{
            this.error.occured = true,
            this.error.alert = 'danger',
            this.error.msg = 'An error occured while updating'
        }

    }
    }

}
</script>


<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  --main-blue: #71b7e6;
  --main-purple: #9b59b6;
  --main-grey: #ccc;
  --sub-grey: #d9d9d9;
}

body {
  display: flex;
  height: 100vh;
  justify-content: center; /*center vertically */
  align-items: center; /* center horizontally */
  padding: 10px;
}
/* container and form */
.container {
  max-width: 700px;
  width: 100%;
  background: #fff;
  padding: 25px 30px;
  border-radius: 5px;
  margin: 15% 16%;
}
.container .title {
  font-size: 25px;
  font-weight: 500;
  position: relative;
}

.container .title::before {
  content: "";
  position: absolute;
  height: 3.5px;
  width: 30px;
  background: #0f2027;
  background: linear-gradient(to right, #0f2020, #203a43, #2c5364) no-repeat 0 0 /
    cover;
  left: 0;
  bottom: 0;
}

.container form .user__details {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 20px 0 12px 0;
}
/* inside the form user details */
form .user__details .input__box {
  width: calc(100% / 2 - 20px);
  margin-bottom: 15px;
}

.user__details .input__box .details {
  font-weight: 500;
  margin-bottom: 5px;
  display: block;
}
.user__details .input__box input {
  height: 45px;
  width: 100%;
  outline: none;
  border-radius: 5px !important;
  border: 1px solid #6f6c6c30 !important;
  padding-left: 15px;
  font-size: 16px;
  border-bottom-width: 2px !important;
  transition: all 0.3s ease;
}

.user__details .input__box input:focus,
.user__details .input__box input:valid {
  border-color: #2c5364;
}

/* inside the form gender details */



form input[type="radio"] {
  display: none;
}

/* submit button */
form .button {
  height: 45px;
  margin: 45px 0;
}

form .button input {
  height: 100%;
  width: 100%;
  outline: none;
  color: #fff;
  border: none;
  font-size: 18px;
  font-weight: 500;
  border-radius: 5px;
  background: #0f2027;
  background: linear-gradient(to right, #0f2027, #203a43, #2c5364) no-repeat 0 0 /
    cover;
  transition: all 0.3s ease;
}

form .button input:hover {
  background: #0f2027;
  background: linear-gradient(to right, #0f2020, #203a43, #2c5364) no-repeat 0 0 /
    cover;
}

@media only screen and (max-width: 584px) {
  .container {
    max-width: 100%;
  }

  form .user__details .input__box {
    margin-bottom: 15px;
    width: 100%;
  }

  form .gender__details .category {
    width: 100%;
  }

  .container form .user__details {
    max-height: 300px;
    overflow-y: scroll;
  }

  .user__details::-webkit-scrollbar {
    width: 0;
  }
}

</style>
