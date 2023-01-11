<template>
  <div class="auth">
    <ErrorComponent v-if="this.error.occured" :alert="this.error.alert" :msg="this.error.msg" :closeOption="this.error.close"></ErrorComponent>
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.8.1/css/all.css"
      integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf"
      crossorigin="anonymous"
    />

    <div class="container" ref="container">
      <div class="form-container sign-up-container">
        <form action="#">
          <h1>Create Account</h1>
          <div class="social-container">
            <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
            <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
          </div>
          <span>or use your email for registration</span>
          <input type="text" placeholder="Name" ref="name"/>
          <input type="email" placeholder="Email" ref="email"/>
          <input type="text" placeholder="Username" ref="sUsername"/>
          <input type="password" placeholder="Password" ref="sPassword"/>
          <input type="text" placeholder="Favorite Artist" ref="fav_artist"/>
          <button @click.prevent="signup" class="s-button">Sign Up</button>
        </form>
      </div>
      <div class="form-container sign-in-container">
        <form action="#">
          <h1>Sign in</h1>
          <div class="social-container">
            <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
            <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
          </div>
          <span>or use your account</span>
          <form @submit.prevent="login">
          <input type="text" placeholder="Username" autocomplete="off" ref="username"/>
          <input type="password" placeholder="Password" autocomplete="off" ref="password"/>
          <a href="#"></a>
          <button type="submit">Sign In</button>
        </form>
        </form>
      </div>
      <div class="overlay-container">
        <div class="overlay">
          <div class="overlay-panel overlay-left text">
            <h1>Hello, Friend!</h1>
            <p>Enter your personal details and start Litsening and Download Music</p>
            <button class="ghost" @click.prevent="goToSignIn" ref="signIn">Sign In</button>
          </div>
          <div class="overlay-panel overlay-right text">
            <h1>Welcome Back!</h1>
            <p>Continue Litsening and Download Music</p>
            <button class="ghost" @click="goToSignUp" ref="signUp">Sign Up</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ErrorComponent from '../errors/ErrorComponent.vue';

export default {
  name: "AuthComponent",
  props: {
    msg: String,
  },
  components:{
    ErrorComponent
  },
  data () {
       return {
        token:"",
        error:{
            occured:false,
            alert:'danger',
            msg:"An uknown error occured",
            close:false
        },

       }
    },
  methods: {
    goToSignIn(){
        this.$refs.container.classList.remove('right-panel-active')
    },
    goToSignUp(){
        this.$refs.container.classList.add('right-panel-active')
    },
    async signup(){
        var token
        var url = "http://localhost:5000/auth/signup"
        console.log(this.$refs.sUsername.value)
        if((
            this.$refs.sUsername.value === ""||
            this.$refs.name.value === ""||
            this.$refs.sPassword.value === ""||
            this.$refs.email.value === ""||
            this.$refs.fav_artist.value === "")){
                console.log("required fields not entered")
                this.error.occured = true;
                this.error.alert = "danger"
                this.error.msg = "Please enter misssing fields"
                return "error";
        }
        else{
                try {
                const formData = new FormData();
                formData.append("username",this.$refs.sUsername.value)
                formData.append("name",this.$refs.name.value)
                formData.append("password",this.$refs.sPassword.value)
                formData.append("email",this.$refs.email.value)
                formData.append("fav_artist",this.$refs.fav_artist.value)

                var response = await axios.post(url,formData);
                var token = response.data.token;
                var name = response.data.name;
                var fav_artist = response.data.fav_artist;
                var username = response.data.username
                console.log(username)
                localStorage.setItem('jwt',token);
                localStorage.setItem('name',name);
                localStorage.setItem('fav_artist',fav_artist);
                localStorage.setItem('username',username);
                this.$router.push({name:'home'});

            } catch (error) {
                this.error.occured = true;
                this.error.alert = "danger"
                this.error.msg = error.response.data.error + ' / ' + error.response.status
            }
        }
    },
    async login(){
        try{
            var url = "http://localhost:5000/auth/login";
            const formData = new FormData();
            formData.append("username",this.$refs.username.value);
            formData.append("password",this.$refs.password.value);
            var response = await axios.post(url,formData);
            localStorage.setItem('jwt',response.data.token);
            localStorage.setItem('name',response.data.name);
            localStorage.setItem('fav_artist',response.data.fav_artist);
            localStorage.setItem('username',response.data.username);
            console.log(response.data.username)
            this.$router.push({name:'home'});
        }catch(error){
            this.error.occured = true;
            this.error.alert = 'danger',
            this.error.msg = error.response.data.error
        }
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.content{
    padding: 0;
    position: absolute;
    top: 8px;
    right: 188px;
    opacity: 0.76;
    z-index: 232;
}

* {
  box-sizing: border-box;
}

body {
  font-family: "Montserrat", sans-serif;
  background: #f6f5f7;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: -20px 0 50px;
  margin-top: 20px;
}

h1 {
  font-weight: bold;
  margin: 0;
}

p {
  font-size: 14px;
  font-weight: 100;
  line-height: 20px;
  letter-spacing: 0.5px;
  margin: 20px 0 30px;
}

span {
  font-size: 12px;
}

a {
  color: #333;
  font-size: 14px;
  text-decoration: none;
  margin: 15px 0;
}

.container {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 14px 28px #00000033, 0 10px 10px #00000033;
  position: relative;
  overflow: hidden;
  width: 868px;
  max-width: 100%;
  min-height: 600px;
}

.form-container form {
  background: #fff;
  display: flex;
  flex-direction: column;
  padding: 22px 5px 64px 0px;
  height: 100%;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.social-container {
  margin: 20px 0;
}

.social-container a {
  border: 1px solid #ddd;
  border-radius: 50%;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 5px;
  height: 40px;
  width: 40px;
}

.form-container input {
  background: #eee;
  border: none;
  padding: 12px 15px;
  margin: 8px 0;
  width: 100%;
}
.s-button{
    margin-top: 32px;
}

button {
  border-radius: 20px;
  border: 1px solid #0f2027;
  background: #2c5364;
  color: #fff;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;

}

button:active {
  transform: scale(0.95);
}

button:focus {
  outline: none;
}

button.ghost {
  background: transparent;
  border-color: #fff;
}

.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}

.sign-in-container {
  left: 0;
  width: 50%;
  z-index: 2;
}

.sign-up-container {
  left: 0;
  width: 50%;
  z-index: 1;
  opacity: 0;
  padding: 45px;
}

.overlay-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}

.overlay {
  background: #0f2027;
  background: linear-gradient(to right, #0f2027, #203a43, #2c5364) no-repeat 0 0 /
    cover;
  color: #fff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateY(0);
  transition: transform 0.6s ease-in-out;
}

.overlay-panel {
  position: absolute;
  top: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0 40px;
  height: 100%;
  width: 50%;
  text-align: center;
  transform: translateY(0);
  transition: transform 0.6s ease-in-out;
}

.overlay-right {
  right: 0;
  transform: translateY(0);
}

.overlay-left {
  transform: translateY(-20%);
}

/* Move signin to right */
.container.right-panel-active .sign-in-container {
  transform: translateY(100%);
}

/* Move overlay to left */
.container.right-panel-active .overlay-container {
  transform: translateX(-100%);
}

/* Bring signup over signin */
.container.right-panel-active .sign-up-container {
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
}

/* Move overlay back to right */
.container.right-panel-active .overlay {
  transform: translateX(50%);
}

/* Bring back the text to center */
.container.right-panel-active .overlay-left {
  transform: translateY(0);
}

/* Same effect for right */
.container.right-panel-active .overlay-right {
  transform: translateY(20%);
}

.footer {
  margin-top: 25px;
  text-align: center;
}
.container {
  padding: 12px;
  margin-right: auto;
  margin-left: auto;
  margin: 2% 18%;
}

.icons {
  display: flex;
  width: 30px;
  height: 30px;
  letter-spacing: 15px;
  align-items: center;
}
.text p {
  color: #f6f5f7;
}
.text h1 {
  color: #f6f5f7;
}

.auth{
    margin: -7% -33%;
}
</style>
