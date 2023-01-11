<template>
    <div class="container">
        <h2 class="title">Recognize A Song</h2>
        <div class="center">

                <div class="pulse-blue" v-if="!recording && !fetching">
                    <button  @click="startRecording">Start</button>
                </div>

                <div class="pulse-red" v-if="recording && !fetching">
                    <button  @click="stopRecording">Stop</button>
                </div>

                <div >
                    <PointLoader class="loader" v-if="fetching"></PointLoader>
                </div>


        </div>
        <ErrorComponent
         :msg="error.msg"
         :alert="error.alert"
         v-if="error.occured">
        </ErrorComponent>

    </div>
</template>

<script>
import RecordRTC from 'recordrtc';
import ErrorComponent from '../errors/ErrorComponent.vue';
import PointLoader from '../loaders/PointLoader.vue';


export default {
    name: "RecognizeSong",
    data(){
        return {
            recording:false,
            fetching:false,
            recorder:null,
            error:{
                occured:false,
                alert:'',
                msg:''
            }

        }
    },
    components:{ ErrorComponent, PointLoader },
    emits:['getRecognisedSong'],
    methods:{
        startRecording (){
            // Get recording stream of user device/browser
            const stream = navigator.mediaDevices.getUserMedia({audio: true})
            .then(stream => {
                //start recording
                this.recorder = new RecordRTC(stream,{
                    type:'audio',
                    mimeType:'audio/mp3'
                });
                this.recorder.startRecording();
            });
            this.recording = true;

        },

        async sendAudio(audioBlob){

            const axios = require("axios");

            this.fetching = true;

            //add blob to form
            const data = new FormData();
            data.append("upload_file",audioBlob);

            //request option
            const options = {
                method: 'POST',
                url: 'https://shazam-song-recognizer.p.rapidapi.com/recognize',
                headers: {
                    'X-RapidAPI-Key': '291956e6a0msh45c40c5ab4a881ep1bea65jsn220317b787e4',
                    'X-RapidAPI-Host': 'shazam-song-recognizer.p.rapidapi.com',
                },
                data: data
            };
            try{
                const response = await axios.request(options)
                if(response.data.result.title){
                    var name = response.data.result.title;
                    var artist = response.data.result.subtitle;
                    var keyword = name + artist;
                    this.$emit('getRecognisedSong',keyword);
                }else{
                    this.error.occured = true;
                    this.error.alert = 'info';
                    this.error.msg = 'Could not Find the Song';
                }

            }catch(err){
                    this.error.occured = true;
                    this.error.alert = 'info';
                    this.error.msg = 'Could not Find the Song';
            }
            this.fetching = false;
        },

        async stopRecording (){

            this.recorder.stopRecording( ()=>{
                //get the recorder audio as a blob
                const audioBlob = this.recorder.getBlob();
                // send audio
                this.sendAudio(audioBlob);
            })
            this.recording = false;
        }
    }
  }
</script>

<style scoped>
    .loader{
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 0px;
    }
    .title{
        margin-left: -12px;
    }
    .container{
        width: 168%;
        background-color: #ffffff00;
        margin-top: 8px;
    }
    .center{
        transform: translate(16%, -90%);
        margin-top: 8rem;
    }

    .pulse-red{
        width: 100px;
        height: 100px;
        background: #e41e1e;
        border-radius: 50%;
        color: #FFF;
        font-size: 20px;
        text-align: center;
        line-height: 100px;
        font-family: sans-serif;
        text-transform: uppercase;
        animation: animate-pulse-red 3s linear infinite;
        cursor: pointer
    }
    .pulse-blue{
        width: 100px;
        height: 100px;
        background: #4aa7ff;
        border-radius: 50%;
        color: #FFF;
        font-size: 20px;
        text-align: center;
        line-height: 100px;
        font-family: sans-serif;
        text-transform: uppercase;
        animation: animate-pulse-blue 3s linear infinite;
        cursor: pointer
    }
    @keyframes animate-pulse-red{
        0%{
            box-shadow: 0 0 0 0 #e41e1eb3,  0 0 0 0 #e41e1eb3;
        }
        40%{
            box-shadow: 0 0 0 50px #ff6d4a00,  0 0 0 0 #e41e1eb3;
        }
        80%{
            box-shadow: 0 0 0 50px #ff6d4a00,  0 0 0 30px #ff6d4a00;
        }
        100%{
            box-shadow: 0 0 0 0 #ff6d4a00,  0 0 0 30px #ff6d4a00;
        }

    }

    @keyframes animate-pulse-blue{
        0%{
            box-shadow: 0 0 0 0 #4aa7ffb3,  0 0 0 0 #4aaeffb3;
        }
        40%{
            box-shadow: 0 0 0 50px #ff6d4a00,  0 0 0 0 #4abdffb3;
        }
        80%{
            box-shadow: 0 0 0 50px #ff6d4a00,  0 0 0 30px #ff6d4a00;
        }
        100%{
            box-shadow: 0 0 0 0 #ff6d4a00,  0 0 0 30px #ff6d4a00;
        }

    }


</style>
